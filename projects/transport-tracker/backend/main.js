/*eslint-disable unknown-require */
const trackerConfig = require('./tracker_configuration.json');
const Promise = require('bluebird');
const admin = require('firebase-admin');
const serviceAccount = require('./serviceAccountKey.json');
const panelConfig = require('./panels_config.json');
const googleMapsClient = require('@google/maps').createClient({
  key: trackerConfig.mapsApiKey,
  Promise
});

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: trackerConfig.databaseURL
});

// Database references
const busLocationsRef = admin.database().ref('bus-locations');
const mapRef = admin.database().ref('map');
const panelsRef = admin.database().ref('panels');
const promoRef = admin.database().ref('promo');
const timeRef = admin.database().ref('current-time');

// Library classes
const {GTFS} = require('./gtfs.js');
const {HeartBeat} = require('./heart_beat.js');
const {PanelChanger} = require('./panel_changer.js');
const {PromoChanger} = require('./promo_changer.js');
const {TimeTable} = require('./time_table.js');

const gtfs = new GTFS();
new HeartBeat(timeRef, trackerConfig.simulation);
new TimeTable(timeRef, panelsRef, gtfs, panelConfig, googleMapsClient);
new PanelChanger(mapRef, panelConfig);
new PromoChanger(promoRef);
if (trackerConfig.simulation) {
  const {BusSimulator} = require('./bus_simulator.js');
  const generatedPaths = require('./paths.json');
  new BusSimulator(timeRef, gtfs, busLocationsRef, generatedPaths);
} else {
  // Exercise for the reader: integrate real bus location data
}
