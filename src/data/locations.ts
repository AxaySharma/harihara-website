export interface LocationItem {
  id: string;
  titleKey: string;
  address: string;
  mapsQuery: string;
  mapsUrl?: string;
  isPrimary?: boolean;
}

/**
 * Single source of truth for the company's three official locations.
 * Address text matches the client's verbatim filings.
 * mapsQuery has been verified via Google Maps browser testing to resolve accurately.
 */
export const LOCATIONS: LocationItem[] = [
  {
    id: 'plant',
    titleKey: 'location.plant_title',
    // Verbatim address as provided by the client
    address: 'Village Manaba, Taluka Rapar, District Kachchh, Gujarat',
    // Verified on Google Maps: lands on Manaba village, Rapar taluka, Kachchh, Gujarat
    mapsQuery: 'Manaba, Rapar, Kachchh, Gujarat',
    mapsUrl: '', // Client to supply custom share pin link if desired
    isPrimary: true,
  },
  {
    id: 'corporate',
    titleKey: 'location.corp_title',
    // Verbatim address as provided by the client
    address: 'Plot No. 390, Shiv Residency, Shiv Aaradhana Society, Bhuj Bypass, Bhuj, Kachchh, Gujarat - 370001',
    // Client-supplied Google Maps place link for Corporate and Accounts Office
    mapsQuery: 'Plot No. 390, Shiv Residency, Shiv Aaradhana Society, Bhuj Bypass, Bhuj, Kachchh, Gujarat - 370001',
    mapsUrl: 'https://www.google.com/maps/place/Shiv+Aaradhna+Society,+Airport+Ring+Rd,+near+Shiv+Mandir,+Yogeswar+Nagar,+Bhuj,+Gujarat+370001/@23.2588477,69.638145,17z/data=!3m1!4b1!4m6!3m5!1s0x39511ddc94ea9a91:0x7ad80501dd62939e!8m2!3d23.2588477!4d69.6407146!16s%2Fg%2F11k446sbr9',
    isPrimary: false,
  },
  {
    id: 'registered',
    titleKey: 'location.reg_title',
    // Verbatim address as provided by the client
    address: '106, Ruby Monarch Arcade, Saki Vihar Road, Sakinaka, Andheri (East), Mumbai - 400072, Maharashtra',
    // Verified on Google Maps: lands on Ruby Monarch Arcade on Saki Vihar Road, Sakinaka, Andheri East, Mumbai 400072
    mapsQuery: 'Ruby Monarch Arcade, Saki Vihar Road, Sakinaka, Andheri East, Mumbai 400072',
    mapsUrl: '',
    isPrimary: false,
  },
];
