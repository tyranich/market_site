export type Sort = "popularity" | "max_amount" | "max_term";

export interface LoanOffer {
  id: number; name: string; description: string; logo_url: string | null;
  max_amount: number; max_term_days: number; rate_from: number;
  apr_from: number; apr_to: number; popularity: number; features: string[];
  external_url: string; is_advertising: boolean;
}

export interface LoanOfferListResponse { items: LoanOffer[]; total: number; }
export interface OfferFilters { max_amount?: number; max_term_days?: number; sort: Sort; }
