from flask import render_template, redirect, url_for, request, abort

from app import app, db, forms
from app.models import Tenants, Apartments


@app.route("/")
def index():

    return render_template("layout.html", title="Главная")


@app.route("/register", methods=("POST", "GET"))
def register():
    tenant_form = forms.AddTenant()
    apartment_form = forms.AddApartment()
    tenant_delate_form = forms.DelateTenant()
    allform = forms.AllApartments()

    # Добавление арендарота
    if tenant_form.validate_on_submit():
        # здесь должна быть проверка корректности введенных данных
        try:
            tenant = Tenants(phone_number=request.form['phone_number'], full_name=request.form['full_name'])
            db.session.add(tenant)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('register'))

    # Добавление апартамента
    if apartment_form.validate_on_submit():
        apartment = Apartments(address=request.form['address'], price=request.form['price'])
        db.session.add(apartment)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('register'))

    if allform.validate_on_submit():
        apart = Apartments.query.filter_by(id=allform.apartments.data).first()
        ten = Tenants.query.filter_by(id=allform.tenants.data).first()
        apart.tenant.append(ten)
        db.session.commit()

    tenants = Tenants.query.all()
    apartments = Apartments.query.all()

    return render_template("tables.html", title="Добавить апартамент", allform=allform, tenant_form=tenant_form, apartment_form=apartment_form, tenant_delate_form=tenant_delate_form, tenants=tenants, apartments=apartments)


@app.route("/delete/<int:idsd>", methods=["POST"])
def delete(idsd):
    tenant = Tenants.query.get(idsd)
    if tenant is None:
        abort(404)
    db.session.delete(tenant)
    db.session.commit()
    return redirect(url_for("register"))


@app.route("/settings")
def settings():
    return render_template("tables.html")