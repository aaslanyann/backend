from apps.company.models import Company, Industry, Competitor, company_competitor, company_industry
from datetime import datetime
from apps.extensions import db



def create_test_data(app):
    with app.app_context():
        # Clear existing data
        db.session.query(company_industry).delete()
        db.session.commit()

        db.session.query(company_competitor).delete()
        db.session.commit()

        # Удаление существующих данных из таблицы Competitor
        db.session.query(Competitor).delete()
        db.session.commit()

        # Удаление существующих данных из таблицы Company
        db.session.query(Company).delete()
        db.session.commit()

        # Get existing Industry records (assuming you already have data)
        saas = Industry.query.filter_by(name=Industry.IndustryEnum.SAAS).first()
        ai_ml = Industry.query.filter_by(name=Industry.IndustryEnum.AI_AND_ML).first()

        # Add test data for Competitor
        competitor_1 = Competitor(external_id="C1", value="Competitor 1")
        competitor_2 = Competitor(external_id="C2", value="Competitor 2")

        db.session.add_all([competitor_1, competitor_2])
        db.session.commit()

        # Add test data for Company with relationships to existing Industry records
        company_1 = Company(
            status=Company.StatusValuesEnum.DRAFT,
            progress_bar=50,
            company_name="Company 1",
            year_founded=2020,
            website_link="http://company1.com",
            pitchbook_link="http://pitchbook1.com",
            industry=[saas, ai_ml],  # Link to existing industries
            first_financing_date=datetime(2021, 1, 1),
            first_financing_deal_type=Company.DealTypes.VC,
            competitors=[competitor_1, competitor_2],  # Link to competitors
            number_competitors=2,
        )

        company_2 = Company(
            status=Company.StatusValuesEnum.CLOSED,
            progress_bar=80,
            company_name="Company 2",
            year_founded=2018,
            website_link="http://company2.com",
            pitchbook_link="http://pitchbook2.com",
            industry=[ai_ml],  # Link to existing industries
            first_financing_date=datetime(2019, 3, 15),
            first_financing_deal_type=Company.DealTypes.SEED,
            number_competitors=1,
        )

        db.session.add_all([company_1, company_2])
        db.session.commit()