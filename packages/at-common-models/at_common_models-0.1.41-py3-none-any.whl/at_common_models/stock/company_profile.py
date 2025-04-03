# app/models/user.py
from sqlalchemy import Column, String, DateTime
from at_common_models.base import BaseModel

class StockCompanyProfile(BaseModel):
    __tablename__ = "stock_company_profiles"

    symbol = Column(String(5), nullable=False, primary_key=True)
    name = Column(String(255), nullable=False)
    currency = Column(String(3), nullable=True)
    exchange = Column(String(16), nullable=False)
    sector = Column(String(255), nullable=True)
    industry = Column(String(255), nullable=True)
    description = Column(String(8196), nullable=True)
    country = Column(String(255), nullable=True)
    image = Column(String(2083), nullable=True)
    ipo_date = Column(DateTime, nullable=True)

    def __str__(self):
        return f"<StockCompanyProfile(exchange={self.exchange}, symbol={self.symbol})>"

    def __repr__(self):
        return f"<StockCompanyProfile(exchange={self.exchange}, symbol={self.symbol})>"
