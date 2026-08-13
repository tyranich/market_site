import asyncio

from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models.loan_offer import LoanOffer

OFFERS = [
    {"name": "ФинПульс", "description": "Демонстрационное предложение для краткосрочных финансовых нужд.", "max_amount": 10000, "max_term_days": 30, "rate_from": 0, "apr_from": 0, "apr_to": 280, "popularity": 98, "features": ["Онлайн-оформление", "Решение определяет кредитор"], "external_url": "https://example.com/demo/finpulse", "is_advertising": True},
    {"name": "Север Капитал", "description": "Демонстрационное предложение с базовыми условиями для сравнения.", "max_amount": 30000, "max_term_days": 90, "rate_from": 0.5, "apr_from": 12, "apr_to": 292, "popularity": 91, "features": ["Онлайн-оформление", "Условия индивидуальны"], "external_url": "https://example.com/demo/north", "is_advertising": True},
    {"name": "Рубль Плюс", "description": "Демонстрационное предложение с увеличенным сроком.", "max_amount": 50000, "max_term_days": 180, "rate_from": 0.7, "apr_from": 18, "apr_to": 292, "popularity": 86, "features": ["Без посещения офиса", "Решение определяет кредитор"], "external_url": "https://example.com/demo/ruble", "is_advertising": True},
    {"name": "Баланс Лаб", "description": "Демонстрационное предложение для ознакомления с параметрами займа.", "max_amount": 100000, "max_term_days": 365, "rate_from": 0.9, "apr_from": 24, "apr_to": 292, "popularity": 79, "features": ["Онлайн-оформление", "Прозрачное сравнение"], "external_url": "https://example.com/demo/balance", "is_advertising": True},
    {"name": "Городской Резерв", "description": "Демонстрационное предложение с гибким сроком.", "max_amount": 50000, "max_term_days": 90, "rate_from": 0.6, "apr_from": 15, "apr_to": 290, "popularity": 74, "features": ["Условия индивидуальны", "Переход на сайт кредитора"], "external_url": "https://example.com/demo/reserve", "is_advertising": False},
    {"name": "Простой Выбор", "description": "Демонстрационное предложение для независимого сравнения.", "max_amount": 30000, "max_term_days": 30, "rate_from": 0.4, "apr_from": 10, "apr_to": 285, "popularity": 68, "features": ["Онлайн-оформление", "Без внутренней заявки"], "external_url": "https://example.com/demo/simple", "is_advertising": True},
]


async def seed() -> None:
    async with SessionLocal() as session:
        if await session.scalar(select(LoanOffer.id).limit(1)):
            print("Данные уже добавлены")
            return
        session.add_all(LoanOffer(**offer) for offer in OFFERS)
        await session.commit()
        print("Добавлено демонстрационных предложений:", len(OFFERS))


if __name__ == "__main__":
    asyncio.run(seed())
