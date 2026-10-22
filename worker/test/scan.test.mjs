import { test } from "node:test";
import assert from "node:assert/strict";
import gtfsBindings from "gtfs-realtime-bindings";
import {
  parseVehiclePositions,
  parseTripUpdates,
  identifyGhostTrips,
} from "../src/scan.js";

const FeedMessage = gtfsBindings.transit_realtime.FeedMessage;

function encodeFeed(entity) {
  return FeedMessage.encode(
    FeedMessage.create({
      header: { gtfsRealtimeVersion: "2.0", incrementality: 0, timestamp: 1792695208 },
      entity,
    }),
  ).finish();
}

test("descriptor-less vehicle with a trip is kept (NYCT subway shape)", () => {
  const bytes = encodeFeed([
    {
      id: "000002",
      vehicle: {
        trip: { tripId: "083650_5..S", routeId: "5" },
        currentStopSequence: 17,
        timestamp: 1792695208,
      },
    },
    // No descriptor and no trip: still skipped, no identity to correlate.
    { id: "000003", vehicle: { currentStopSequence: 3 } },
  ]);
  const { vehicles } = parseVehiclePositions(bytes);
  assert.equal(vehicles.length, 1);
  assert.equal(vehicles[0].vehicle_id, "000002");
  assert.equal(vehicles[0].trip_id, "083650_5..S");
  assert.equal(vehicles[0].latitude, null);
});

test("descriptor-less vehicles clear ghost status by trip id", () => {
  const vp = encodeFeed([
    { id: "000002", vehicle: { trip: { tripId: "T1", routeId: "5" } } },
  ]);
  const tu = encodeFeed([
    { id: "a", tripUpdate: { trip: { tripId: "T1", routeId: "5" }, stopTimeUpdate: [] } },
    { id: "b", tripUpdate: { trip: { tripId: "T2", routeId: "5" }, stopTimeUpdate: [] } },
  ]);
  const { vehicles } = parseVehiclePositions(vp);
  const { trips } = parseTripUpdates(tu);
  const result = identifyGhostTrips(trips, vehicles);
  assert.equal(result.find((t) => t.trip_id === "T1").is_ghost, false);
  assert.equal(result.find((t) => t.trip_id === "T2").is_ghost, true);
});
