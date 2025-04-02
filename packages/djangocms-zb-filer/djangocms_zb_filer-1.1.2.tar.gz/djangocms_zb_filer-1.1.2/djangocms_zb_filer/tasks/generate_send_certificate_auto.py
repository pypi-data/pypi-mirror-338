# -*- coding: utf-8 -*-
#  Developed by CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. All rights reserved.
#  Desarrollado por CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. Todos los derechos reservados.
import os
from datetime import timedelta
from celery import shared_task
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from typing import Any
from zibanu.django.lib.utils import Email

from djangocms_zb_filer.lib.choices import TypeGenerateSendCertificate
from djangocms_zb_filer.lib.utils import CertificateGenerator
from djangocms_zb_filer.models import Publication, Certificate


@shared_task(bind=True)
def generate_send_certificate_auto(app: Any):
    """
    Task that generates and sends publication certificates.
    Returns
    -------
    None
    """
    try:
        date_now = timezone.now()
        date_filter = date_now.today() - timedelta(days=1)
        publications = Publication.objects.filter(auto_send=True, certificate_sent_auto=False,
                                                  publish_end_at__date=date_filter)
        certificate = CertificateGenerator()
        for publication in publications:
            context = {
                'publication': publication,
                'date_now': date_now,
                'domain': settings.DOMAIN,
            }
            url_file = certificate.generate_from_template(template_name=publication.category.certificate.template,
                                                          folder=publication.category.name, context=context)
            if url_file is not None:
                certificate_instance = Certificate.objects.create(created_at=date_now, file_path=url_file,
                                                                  publication_id=publication.id)
                if certificate_instance is not None:
                    certificate_instance.type_generate = TypeGenerateSendCertificate.AUTOMATIC
                    certificate_instance.save()
                    # Set mail context
                    path_filename = os.path.join(settings.BASE_DIR, certificate_instance.file_path[1:])
                    if not os.path.exists(path_filename):
                        raise ObjectDoesNotExist(_("Document file does not exist."))
                    email_context = {
                        "publication_title": certificate_instance.publication.title,
                        "description": certificate_instance.publication.description,
                        "created_at": certificate_instance.created_at
                    }
                    email = Email(
                        subject=_("Certificate of publication %(title)s") % {
                            "title": certificate_instance.publication.title},
                        to=certificate_instance.publication.notification)
                    email.set_text_template("djangocms_zb_filer/mail/send_certificate.txt", context=email_context)
                    email.attach_file(path_filename)
                    email.send()
                    publication.certificate_sent_auto = True
                    publication.save()
                    certificate_instance.type_send = TypeGenerateSendCertificate.AUTOMATIC
                    certificate_instance.save()
    except DatabaseError as exc:
        raise DatabaseError from exc
    except Exception as exc:
        raise Exception from exc
