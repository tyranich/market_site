import type { OfferFilters, Sort } from "../types/loanOffer";

const amounts = [10000, 30000, 50000, 100000];
const terms = [30, 90, 180, 365];
export function LoanFilters({ filters, onChange }: { filters: OfferFilters; onChange: (next: OfferFilters) => void }) {
  const set = <K extends keyof OfferFilters>(key: K, value: OfferFilters[K]) => onChange({ ...filters, [key]: filters[key] === value ? undefined : value });
  return <aside className="filters" aria-label="Фильтры предложений"><div><h3>Максимальная сумма</h3><div className="chips">{amounts.map(value => <button className={filters.max_amount === value ? "selected" : ""} onClick={() => set("max_amount", value)} key={value}>{value.toLocaleString("ru-RU")} ₽</button>)}</div></div><div><h3>Максимальный срок</h3><div className="chips">{terms.map(value => <button className={filters.max_term_days === value ? "selected" : ""} onClick={() => set("max_term_days", value)} key={value}>{value} дней</button>)}</div></div><label>Сортировка<select value={filters.sort} onChange={event => onChange({ ...filters, sort: event.target.value as Sort })}><option value="popularity">По популярности</option><option value="max_amount">По максимальной сумме</option><option value="max_term">По сроку</option></select></label></aside>;
}
