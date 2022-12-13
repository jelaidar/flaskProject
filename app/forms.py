from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from app.models import Apartments, Tenants


class AddApartment(FlaskForm):
    address = StringField('Адрес', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    submit = SubmitField("Сохранить")


class AddTenant(FlaskForm):
    phone_number = StringField('Номер телефона', validators=[DataRequired()])
    full_name = StringField('ФИО', validators=[DataRequired()])
    submit = SubmitField("Сохранить")


class DelateTenant(FlaskForm):
    submit = SubmitField("Удалить")


class AllApartments(FlaskForm):
    apartments = SelectField("Group", choices=[], coerce=int, validate_choice=True)
    tenants = SelectField("Group", choices=[], coerce=int, validate_choice=True)
    submit = SubmitField("Сохранить")

    def __init__(self, *args, **kwargs):
        super(AllApartments, self).__init__(*args, **kwargs)
        self.apartments.choices = [(apartment.id, apartment.address) for apartment in Apartments.query.all()]
        self.tenants.choices = [(tenant.id, tenant.full_name) for tenant in Tenants.query.all()]


