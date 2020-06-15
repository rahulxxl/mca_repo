
const promos = [
  {
    html: 'Bus locations powered by <span style="font-weight: 500;">fused location provider</span> on Android',
    product: 'android'
  },
  {
    html: 'Predicted travel times from the <span style="font-weight: 500;">Google Maps Directions API</span>',
    product: 'google-maps'
  },
  {
    html: 'Locations snapped to the road with the <span style="font-weight: 500;">Google Maps Roads API</span>',
    product: 'google-maps'
  },
  {
    html: 'Styled map with the <span style="font-weight: 500;">Google Maps JavaScript API</span> showing routes and schedules',
    product: 'google-maps'
  },
  {
    html: 'Data synchronized in real time with <span style="font-weight: 500;">Firebase Realtime Database</span>',
    product: 'firebase'
  },
  {
    html: '<span style="font-weight: 500;">Node.js</span> and <span style="font-weight: 500;">Google Compute Engine</span> for backend processing',
    product: 'gce'
  }
];

exports.PromoChanger = class {
  constructor(promoRef) {
    this.promoRef = promoRef;
    this.promoIndex = 0;

    // Change the promo once every five seconds
    this.timeTimerId = setInterval(() => {
      this.promoAdvance();
    }, 10000);
  }

  promoAdvance() {
    const promo = promos[this.promoIndex];
    promo.position = this.promoIndex + 1;
    promo.totalCount = promos.length;
    this.promoRef.set(promo);
    this.promoIndex = (this.promoIndex + 1) % promos.length;
  }
};
