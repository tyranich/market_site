import { useEffect, useState } from "react";
import { getOffers } from "../api/offers";
import type { LoanOffer, OfferFilters } from "../types/loanOffer";
import { LoanFilters } from "./LoanFilters";
import { LoanOfferCard } from "./LoanOfferCard";

export function LoanOffers() {
  const [filters, setFilters] = useState<OfferFilters>({ sort: "popularity" });
  const [offers, setOffers] = useState<LoanOffer[]>([]); const [loading, setLoading] = useState(true); const [error, setError] = useState(false);
  useEffect(() => { setLoading(true); setError(false); getOffers(filters).then(result => setOffers(result.items)).catch(() => setError(true)).finally(() => setLoading(false)); }, [filters]);
  return <section id="offers" className="offers section"><div className="section-intro"><p className="eyebrow">Витрина</p><h2>Предложения займов</h2><p>Сравните ключевые параметры. Окончательные условия определяет кредитор.</p></div><LoanFilters filters={filters} onChange={setFilters}/>{loading ? <div className="cards">{[1,2,3].map(item => <div className="skeleton" key={item}/>)}</div> : error ? <div className="state"><h3>Не удалось загрузить предложения</h3><p>Проверьте, что API запущен, и повторите попытку.</p><button className="button primary" onClick={() => setFilters({...filters})}>Повторить</button></div> : offers.length === 0 ? <div className="state"><h3>Подходящих предложений нет</h3><p>Попробуйте изменить параметры фильтра.</p></div> : <div className="cards">{offers.map(offer => <LoanOfferCard offer={offer} key={offer.id}/>)}</div>}</section>;
}
