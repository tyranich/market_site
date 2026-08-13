import { trackOfferClick } from "../api/offers";
import type { LoanOffer } from "../types/loanOffer";

const money = (value: number) => `${value.toLocaleString("ru-RU")} ₽`;
export function LoanOfferCard({ offer }: { offer: LoanOffer }) {
  const handleClick = () => { void trackOfferClick(offer.id).catch(() => undefined); };
  return <article className="offer-card"><div className="logo" aria-hidden="true">{offer.name.slice(0, 1)}</div><h3>{offer.name}</h3><p className="offer-description">{offer.description}</p><div className="terms"><div><strong>До {money(offer.max_amount)}</strong><span>Сумма</span></div><div><strong>до {offer.max_term_days} дней</strong><span>Срок</span></div></div><div className="rates"><p>Ставка от <strong>{offer.rate_from}%</strong></p><p>ПСК: {offer.apr_from}–{offer.apr_to}% годовых</p></div><ul>{offer.features.map(feature => <li key={feature}>✓ {feature}</li>)}</ul><a className="button outline" href={offer.external_url} target="_blank" rel="noopener noreferrer" onClick={handleClick}>Узнать условия <span>→</span></a>{offer.is_advertising && <small>Реклама</small>}</article>;
}
