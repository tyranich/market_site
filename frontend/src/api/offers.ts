import axios from "axios";
import type { LoanOfferListResponse, OfferFilters } from "../types/loanOffer";

const client = axios.create({ baseURL: import.meta.env.VITE_API_URL ?? "http://localhost:8000/api/v1" });

export async function getOffers(filters: OfferFilters): Promise<LoanOfferListResponse> {
  const { data } = await client.get<LoanOfferListResponse>("/offers", { params: filters });
  return data;
}

export async function trackOfferClick(offerId: number): Promise<void> {
  await client.post(`/offers/${offerId}/click`);
}
