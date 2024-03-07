from enum import Enum
from jinja2 import Template
from common.notification_service.summary_email_html import get_summary_email_html

class EmailTemplate(Enum):
    SUMMARY_EMAIL = "summary_email"

def generete_email_body(template_id, email_data):
    email_template = {
        EmailTemplate.SUMMARY_EMAIL: get_summary_email_html()
    }
    template = email_template.get(template_id)
    if template is None:
        raise ValueError(f"Template {template_id} not found")
    template = Template(template)
    email_content = template.render(email_data) 

    return email_content