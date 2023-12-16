import enum
from apps.extensions import db
from datetime import datetime



company_industry = db.Table('company_industry',
                            db.Column('id', db.Integer, primary_key=True),
                            db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
                            db.Column('industry_id', db.Integer, db.ForeignKey('industries.id'))
                            )

company_competitor = db.Table('company_competitor',
                              db.Column('id', db.Integer, primary_key=True),
                              db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
                              db.Column('competitor_id', db.Integer, db.ForeignKey('competitors.id'))
)

class Company(db.Model):
    __tablename__ = 'companies'

    class DealTypes(str, enum.Enum):
        VC = 'vc'
        SEED = 'seed'
        ACCELERATOR = 'accelerator'
        ANGEL = 'angel'
        GRANT = 'grant'

    class StatusValuesEnum(str, enum.Enum):
        DRAFT = 'draft'
        CALCULATING = 'calculating'
        REJECTED = "rejected"
        CLOSED = "closed"



    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Enum(StatusValuesEnum), nullable=False)
    progress_bar = db.Column(db.Integer, db.CheckConstraint('progress_bar >= 0 AND progress_bar <= 100'), nullable=False )
    company_name = db.Column(db.String(100), nullable=False)
    company_former_name = db.Column(db.String(100), nullable=True)
    year_founded = db.Column(db.Integer, nullable=False)
    website_link = db.Column(db.String(350), nullable=False)
    pitchbook_link = db.Column(db.String(300), nullable=False)
    industry = db.relationship('Industry', secondary='company_industry', backref='companies')
    first_financing_date = db.Column(db.Date, nullable=False)
    first_financing_deal_type = db.Column(db.Enum(DealTypes), nullable=False)
    competitors = db.relationship('Competitor', secondary='company_competitor', backref='companies')
    number_competitors = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=db.func.now())


class Industry(db.Model):
    __tablename__ = 'industries'

    class IndustryEnum(str, enum.Enum):
        SAAS = 'saas'
        AI_AND_ML = 'ai and ml'
        BIG_DATA = 'big data'
        FINTECH = 'fintech'
        ECOMMERCE = 'ecommerce'
        CYBERSECURITY = 'cybersecurity'
        HEALTHTECH = 'healthech'
        MOBILITY_TECH = 'mobility tech'
        LIFE_SCIENCES = 'life sciences'
        CLOUD_TECH = 'cloud tech'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Enum(IndustryEnum), nullable=False)


class Competitor(db.Model):
    __tablename__ = 'competitors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    external_id = db.Column(db.String)
    value = db.Column(db.String)