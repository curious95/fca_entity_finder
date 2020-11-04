from flask import Flask, render_template, jsonify, request, redirect, url_for, Response
from sqlalchemy import exc
from jinja2 import Template
from datetime import datetime
from render_html import render_html
from render_pdf import render_pdf
from entity_finder import find_fac_entities

import logging
import traceback
import glob

app = Flask(__name__)

# logging.basicConfig(filename=f"/home/groot/workspace/customer_manager/app/logs/{datetime.today().strftime('%Y-%m-%d')}.log",
#                     level=logging.DEBUG,
#                     format=' %(asctime)s %(levelname)s %(name)s %(threadName)s: %(message)s')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/web')
def parse_web():
    if 'url' not in request.args:
        return "{'message': 'url param was not provided'}"

    url = request.args.get('url', type=str)

    resp = dict()

    resp['status'] = 102
    resp['message'] = 'model is being trained'

    return resp
    # return find_fac_entities(render_html(url))


@app.route('/pdf')
def parse_pdf():
    if 'url' not in request.args:
        return "{'message': 'url param was not provided'}"

    url = request.args.get('url', type=str)

    resp = dict()

    resp['status'] = 102
    resp['message'] = 'model is being trained'

    return resp
    # return find_fac_entities(render_pdf(url))

# @app.route('/addCustomer')
# def add_customer():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     company_name = request.args.get('company_name', type=str)
#     owner_name = request.args.get('owner_name', type=str)
#     email = request.args.get('email', type=str)
#     state = request.args.get('state', type=str)
#     phone = request.args.get('phone', type=str)
#
#     try:
#         customer = Customers(company_name, owner_name, email, state, phone)
#         session.add(customer)
#         session.commit()
#
#         return Response(f'{company_name} was added', status=200, mimetype='text/plain; charset=utf-8')
#     except exc.IntegrityError:
#         return Response(f'Either customer present or check your request params', status=403, mimetype='text/plain; charset=utf-8')
#     except:
#         print(traceback.print_exc())
#         return Response(f'Unexpected Error', status=403, mimetype='text/plain; charset=utf-8')
#     finally:
#         session.close()
#
#
# @app.route('/getCustomers')
# def get_customers():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     customers_array = []
#
#     fetched_customers = session.query(Customers).all()
#
#     for customer in fetched_customers:
#         temp_customer = dict()
#         temp_customer['company_name'] = customer.company_name
#         temp_customer['phone'] = customer.phone
#         temp_customer['email'] = customer.email
#         temp_customer['date_added'] = customer.created_at
#
#         customers_array.append(temp_customer)
#
#     session.close()
#
#     return jsonify(customers_array)
#
#
# @app.route('/logReminder')
# def log_reminder():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     company_name = request.args.get('company_name', type=str)
#     phone = request.args.get('phone', type=str)
#     sms_template = request.args.get('sms_template', type=str)
#     sms_status = request.args.get('sms_status', type=str)
#     scheduled_sms = request.args.get('scheduled_sms', type=str)
#     voice_template = request.args.get('voice_template', type=str)
#     voice_status = request.args.get('voice_status', type=str)
#     scheduled_voice = request.args.get('scheduled_voice', type=str)
#
#     try:
#         history = History(company_name, phone, sms_template, sms_status, scheduled_sms, voice_template, voice_status,
#                           scheduled_voice)
#         session.add(history)
#         session.commit()
#
#         return Response(f'Reminder for {company_name} was logged', status=200, mimetype='text/plain; charset=utf-8')
#     except:
#         print(traceback.print_exc())
#         return Response(f'Logging Failure', status=403, mimetype='text/plain; charset=utf-8')
#     finally:
#         session.close()
#
#
# @app.route('/reminderHistory')
# def get_reminder_history():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     history_array = []
#
#     fetched_history = session.query(History).all()
#
#     for history in fetched_history:
#         temp_history = dict()
#         temp_history['company_name'] = history.company_name
#         temp_history['phone'] = history.phone
#         temp_history['logged_at'] = history.logged_at
#         temp_history['sms_template'] = history.sms_template
#         temp_history['sms_status'] = history.sms_status
#         temp_history['scheduled_sms'] = history.scheduled_sms
#         temp_history['voice_template'] = history.voice_template
#         temp_history['voice_status'] = history.voice_status
#         temp_history['scheduled_voice'] = history.scheduled_voice
#
#         history_array.append(temp_history)
#
#     session.close()
#
#     return jsonify(history_array)
#
#
# @app.route('/reminder')
# def add_update_reminder():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     company_name = request.args.get('company_name', type=str)
#     phone = request.args.get('phone', type=str)
#     sms_template = request.args.get('sms_template', type=str)
#     scheduled_sms = request.args.get('scheduled_sms', type=str)
#     voice_template = request.args.get('voice_template', type=str)
#     scheduled_voice = request.args.get('scheduled_voice', type=str)
#
#     try:
#         reminder = Reminders(company_name, phone, sms_template, scheduled_sms, voice_template, scheduled_voice)
#         session.add(reminder)
#         session.commit()
#
#         return Response(f'Reminder for {company_name} was added', status=200, mimetype='text/plain; charset=utf-8')
#     except:
#         return Response(f'Error in adding reminder', status=403, mimetype='text/plain; charset=utf-8')
#     finally:
#         session.close()
#
#
# @app.route('/getReminders')
# def get_reminders():
#     Base.metadata.create_all(engine)
#     session = Session()
#
#     reminder_array = []
#
#     fetched_reminders = session.query(Reminders).all()
#
#     for reminder in fetched_reminders:
#         temp_reminder = dict()
#         temp_reminder['company_name'] = reminder.company_name
#         temp_reminder['phone'] = reminder.phone
#         temp_reminder['sms_template'] = reminder.sms_template
#         temp_reminder['scheduled_sms'] = reminder.scheduled_sms
#         temp_reminder['voice_template'] = reminder.voice_template
#         temp_reminder['scheduled_voice'] = reminder.scheduled_voice
#
#         reminder_array.append(temp_reminder)
#
#     session.close()
#
#     return jsonify(reminder_array)
#
#
# @app.route('/sms_templates')
# def sms_templates():
#     templates = glob.glob(config.sms_templates)
#
#     response = {}
#     for template in templates:
#         response[template] = template
#
#     return jsonify(response)
#
#
# @app.route('/voice_templates')
# def voice_templates():
#     templates = glob.glob(config.voice_templates)
#
#     response = {}
#     for template in templates:
#         response[template] = template
#
#     return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)