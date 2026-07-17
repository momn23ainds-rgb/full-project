
from sqlalchemy import *
from app.database import Base

class DocumentVersion(Base):
    __tablename__="document_versions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)

class Node(Base):
    __tablename__="nodes"
    id = Column(Integer, primary_key=True)
    heading = Column(String)
    body = Column(Text)
    level = Column(Integer)
    parent_id = Column(Integer, nullable=True)
    content_hash = Column(String)
    logical_id = Column(String)
    document_version_id = Column(Integer)

class Selection(Base):
    __tablename__="selections"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class GeneratedCase(Base):
    __tablename__="generated_cases"
    id = Column(Integer, primary_key=True)
    selection_id = Column(Integer)
    output = Column(Text)
    hash_snapshot = Column(String)
