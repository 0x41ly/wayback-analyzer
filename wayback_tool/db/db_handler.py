from pymongo import MongoClient
import os
import logging

logger = logging.getLogger(__name__)

class MongoHandler:
    def __init__(self, uri=None, db_name="wayback_recon"):
        """
        Initialize the MongoHandler class to manage MongoDB connection.
        """
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.client = None
        self.db_name = db_name
        self.db = None
        self._connect()

    def _connect(self):
        """
        Establish connection to MongoDB and select the database.
        """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            logger.info("🗃️ Connected to MongoDB")
        except Exception as e:
            logger.error(f"❌ Failed to connect to MongoDB: {e}")
            raise

    def close(self):
        """
        Close the MongoDB connection.
        """
        if self.client:
            self.client.close()
            logger.info("🔒 MongoDB connection closed")

    def get_collection(self, collection_name):
        """
        Get the collection from the MongoDB database.
        """
        return self.db[collection_name]

# Singleton pattern: Create a single MongoHandler instance globally
mongo_handler = MongoHandler()
