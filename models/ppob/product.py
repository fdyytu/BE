from typing import Dict, Any, Optional
from datetime import datetime
from .base.product_interface import IProduct
from .category import Category
from .price import Price
from .tax import Tax
from .discount import Discount

class Product(IProduct):
    """Enhanced product base class."""
    
    def __init__(self, 
                 name: str,
                 code: str,
                 category: Category,
                 price: Price,
                 description: str = ""):
        self.name = name
        self.code = code
        self.category = category
        self.base_price = price
        self.description = description
        self.taxes: List[Tax] = []
        self.discounts: List[Discount] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.is_active = True
        
    def get_price(self) -> float:
        """Calculate final price including taxes and discounts."""
        final_price = self.base_price.amount
        
        # Apply taxes
        for tax in self.taxes:
            if tax.is_applicable(self):
                final_price += tax.calculate(final_price)
        
        # Apply discounts
        for discount in self.discounts:
            if discount.is_applicable(self):
                final_price -= discount.calculate(final_price)
                
        return max(0.0, final_price)
    
    def get_details(self) -> Dict[str, Any]:
        """Get complete product details."""
        return {
            'name': self.name,
            'code': self.code,
            'category': self.category.name,
            'base_price': self.base_price.amount,
            'final_price': self.get_price(),
            'description': self.description,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def is_available(self) -> bool:
        """Check if product is available."""
        return self.is_active
    
    def validate(self) -> bool:
        """Validate product data."""
        return all([
            self.name and len(self.name.strip()) > 0,
            self.code and len(self.code.strip()) > 0,
            self.category is not None,
            self.base_price is not None,
            self.base_price.amount >= 0
        ])
    
    def add_tax(self, tax: Tax) -> None:
        """Add tax to product."""
        if tax not in self.taxes:
            self.taxes.append(tax)
            self.updated_at = datetime.utcnow()
    
    def add_discount(self, discount: Discount) -> None:
        """Add discount to product."""
        if discount not in self.discounts:
            self.discounts.append(discount)
            self.updated_at = datetime.utcnow()
    
    def update_price(self, new_price: Price) -> None:
        """Update product price."""
        self.base_price = new_price
        self.updated_at = datetime.utcnow()