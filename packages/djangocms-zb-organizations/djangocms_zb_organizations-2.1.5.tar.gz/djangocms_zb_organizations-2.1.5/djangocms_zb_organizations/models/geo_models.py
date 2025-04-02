# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. All rights reserved.
#  Desarrollado por CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. Todos los derechos reservados.

# ****************************************************************
# IDE: PyCharm
# Developed by: JhonyAlexanderGonzal
# Date: 5/10/2022 2:07 p. m.
# Project: Djangocms-pruebas
# Module Name: geo_models
# ****************************************************************

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_zb_organizations.models import Organization
from djangocms_zb_organizations.lib import managers


class GeoOrganization(models.Model):
    organization = models.OneToOneField(Organization, null=False, blank=False, on_delete=models.CASCADE,
                                        related_name="geo_organization", related_query_name="organization",
                                        verbose_name=_("Organization"))
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=_('Polygons'),
                                       help_text=_('Location Area Coordinates'))

    objects = managers.GeoOrganizationManager()