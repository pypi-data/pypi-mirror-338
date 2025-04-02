# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. All rights reserved.
#  Desarrollado por CQ Inversiones SAS.
#  Copyright ©. 2019 - 2025. Todos los derechos reservados.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ****************************************************************
# IDE: PyCharm
# Developed by: JhonyAlexanderGonzal
# Date: 3/12/2022 9:43 a. m.
# Project: Djangocms-pruebas
# Module Name: organization
# ****************************************************************

from rest_framework_gis import serializers
from djangocms_zb_organizations.models import Organization


class OrganizationSerializer(serializers.GeoFeatureModelSerializer):
    polygon = serializers.GeometrySerializerMethodField()

    @staticmethod
    def get_polygon(instance):
        return instance.geo_organization.polygon

    class Meta:
        model = Organization
        fields = ["id", "name", "polygon"]
        geo_field = "polygon"
