"""
Firebase Firestore client implementation.
"""

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from typing import Dict, List, Any, Optional, Tuple
from kalx.utils.logger import get_logger
from kalx.utils.config import get_config

logger = get_logger(__name__)

class FirestoreClient:
    """Handles Firestore database operations."""
    
    _instance = None
    
    def __new__(cls):
        """Ensure singleton pattern."""
        if cls._instance is None:
            cls._instance = super(FirestoreClient, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize Firestore client."""
        if self._initialized:
            return
            
        try:
            config = get_config()
            cred_path = config.get('firebase', 'credentials_path')
            
            if not firebase_admin._apps:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            
            self.db = firestore.client()
            self._initialized = True
            logger.info("Firestore client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Firestore client: {str(e)}")
            raise
    
    def add_document(self, collection: str, doc_id: str, data: Dict) -> bool:
        """
        Add a document to a collection.
        
        Args:
            collection: Collection name
            doc_id: Document ID
            data: Document data
            
        Returns:
            bool: Success status
        """
        try:
            self.db.collection(collection).document(doc_id).set(data)
            logger.debug(f"Added document {doc_id} to {collection}")
            return True
        except Exception as e:
            logger.error(f"Failed to add document: {str(e)}")
            return False
    
    def get_document(self, collection: str, doc_id: str) -> Optional[Dict]:
        """
        Get a document by ID.
        
        Args:
            collection: Collection name
            doc_id: Document ID
            
        Returns:
            Optional[Dict]: Document data or None
        """
        try:
            doc = self.db.collection(collection).document(doc_id).get()
            if doc.exists:
                return doc.to_dict()
            return None
        except Exception as e:
            logger.error(f"Failed to get document: {str(e)}")
            return None
    
    def update_document(self, collection: str, doc_id: str, data: Dict) -> bool:
        """
        Update a document.
        
        Args:
            collection: Collection name
            doc_id: Document ID
            data: Update data
            
        Returns:
            bool: Success status
        """
        try:
            self.db.collection(collection).document(doc_id).update(data)
            logger.debug(f"Updated document {doc_id} in {collection}")
            return True
        except Exception as e:
            logger.error(f"Failed to update document: {str(e)}")
            return False
    
    def delete_document(self, collection: str, doc_id: str) -> bool:
        """
        Delete a document.
        
        Args:
            collection: Collection name
            doc_id: Document ID
            
        Returns:
            bool: Success status
        """
        try:
            self.db.collection(collection).document(doc_id).delete()
            logger.debug(f"Deleted document {doc_id} from {collection}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete document: {str(e)}")
            return False
    
    def get_all_documents(self, collection: str) -> List[Dict]:
        """
        Get all documents in a collection.
        
        Args:
            collection: Collection name
            
        Returns:
            List[Dict]: List of documents
        """
        try:
            docs = self.db.collection(collection).stream()
            return [doc.to_dict() for doc in docs]
        except Exception as e:
            logger.error(f"Failed to get documents: {str(e)}")
            return []
    
    def query_documents(self, collection: str, filters: List[Tuple[str, str, Any]]) -> List[Dict]:
        """
        Query documents with filters.
        
        Args:
            collection: Collection name
            filters: List of tuples (field, operator, value)
            
        Returns:
            List[Dict]: Matching documents, including document IDs
        """
        try:
            query = self.db.collection(collection)
            for field, operator, value in filters:
                query = query.where(filter=firestore.FieldFilter(field, operator, value))  # Use FieldFilter for filtering
            docs = query.stream()
            return [{"id": doc.id, **doc.to_dict()} for doc in docs]  # Include document ID
        except ValueError as e:
            logger.error(f"Invalid filter format: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Failed to query documents: {str(e)}")
            return []
