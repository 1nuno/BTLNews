from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Tabel 'dreapp_document'
class DreappDocument(Base):
    __tablename__ = 'dreapp_document'

    id = Column(Integer, primary_key=True)  # serial4
    doc_type = Column(String(128))  # varchar(128)
    number = Column(String(32))  # varchar(32)
    emiting_body = Column(String(2048))  # varchar(2048)
    source = Column(String(128))  # varchar(128)
    in_force = Column(Boolean)  # boolean
    conditional = Column(Boolean)  # boolean
    date = Column(Date)  # date
    notes = Column(String(20480))  # varchar(20480)
    dre_pdf = Column(String(200))  # varchar(200)
    timestamp = Column(DateTime(timezone=True))  # timestamptz
    dr_number = Column(String(16))  # varchar(16)
    series = Column(Integer)  # int4
    part = Column(String(2))  # varchar(2)



# Tabel dreapp_document_connects_to
class DreappDocumentConnectsTo(Base):
    __tablename__ = 'dreapp_document_connects_to'

    id = Column(Integer, primary_key=True)  # serial4
    from_document_id = Column(Integer,
                              ForeignKey('dreapp_document.id'))  # int4, ForeignKey para ligação com DreappDocument
    to_document_id = Column(Integer,
                            ForeignKey('dreapp_document.id'))  # int4, ForeignKey para ligação com DreappDocument



# Tabel dreapp_documenttext
class DreappDocumentText(Base):
    __tablename__ = 'dreapp_documenttext'

    id = Column(Integer, primary_key=True)  # serial4
    document_id = Column(Integer, ForeignKey('dreapp_document.id'))  # int4, ForeignKey para ligação com DreappDocument
    timestamp = Column(DateTime(timezone=True))  # timestamptz
    text_url = Column(String(200))  # varchar(200)
    text = Column(Text)  # text

