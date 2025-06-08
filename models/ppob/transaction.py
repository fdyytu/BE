from typing import Dict, Any, Optional
from datetime import datetime
from uuid import uuid4
from .product import Product
from .digital_product import DigitalProduct

class Transaction:
    """PPOB transaction handler."""
    
    def __init__(self,
                 product: Product,
                 customer_id: str,
                 reference_number: Optional[str] = None):
        self.id = str(uuid4())
        self.product = product
        self.customer_id = customer_id
        self.reference_number = reference_number or self.id
        self.amount = product.get_price()
        self.status = "PENDING"
        self.created_at = datetime.utcnow()
        self.completed_at: Optional[datetime] = None
        self.response_data: Dict[str, Any] = {}
        
    async def process(self) -> bool:
        """Process the transaction."""
        try:
            if isinstance(self.product, DigitalProduct):
                # Handle digital product transaction
                result = await self._process_digital()
            else:
                # Handle other product types
                result = await self._process_regular()
                
            self.completed_at = datetime.utcnow()
            return result
            
        except Exception as e:
            self.status = "FAILED"
            self.response_data['error'] = str(e)
            return False
    
    async def _process_digital(self) -> bool:
        """Process digital product transaction."""
        # Implement digital product transaction logic
        pass
    
    async def _process_regular(self) -> bool:
        """Process regular product transaction."""
        # Implement regular product transaction logic
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Get transaction status and details."""
        return {
            'id': self.id,
            'reference_number': self.reference_number,
            'product': self.product.get_details(),
            'customer_id': self.customer_id,
            'amount': self.amount,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'response_data': self.response_data
        }