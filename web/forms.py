from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired

class LegalShareholderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    reg_code = StringField('Registration Code', validators=[DataRequired()])
    founder = BooleanField('Founder')
    shares = DecimalField('Shares', validators=[DataRequired()])

class NaturalShareholderForm(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    social_insurance_number = StringField('Social Insurance Number', validators=[DataRequired()])
    founder = BooleanField('Founder')
    shares = DecimalField('Shares', validators=[DataRequired()])

class CompanyForm(FlaskForm):
    name = StringField('Desired Name:', validators=[DataRequired()])
    reg_code = StringField('Registration Code:', validators=[DataRequired()])
    start_date = DateField('Start Date:', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital:', validators=[DataRequired()])
    legal_shareholders = FieldList(FormField(LegalShareholderForm))
    natural_shareholders = FieldList(FormField(NaturalShareholderForm))
