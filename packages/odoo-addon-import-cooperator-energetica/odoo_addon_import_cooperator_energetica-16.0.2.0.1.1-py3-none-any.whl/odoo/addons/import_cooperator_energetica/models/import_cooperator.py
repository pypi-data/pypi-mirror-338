import logging

from odoo import _, fields, models

logger = logging.getLogger(__name__)


class ImportCooperator(models.Model):
    _name = "import.cooperator"
    _description = "Import Cooperator"

    numero_cooperativista = fields.Char()
    estado = fields.Char()
    fechacreacion = fields.Char()
    fechamodificacion = fields.Char()
    observaciones = fields.Char()
    es_persona_juridica = fields.Char()
    nombre = fields.Char()
    primer_apellido = fields.Char()
    segundo_apellido = fields.Char()
    nif_nie = fields.Char()
    genero = fields.Char()
    razon_social = fields.Char()
    cif = fields.Char()
    nombre_apellidos_representante = fields.Char()
    nif_representante = fields.Char()
    email = fields.Char()
    password = fields.Char()
    direccion = fields.Char()
    codigo_postal = fields.Char()
    provincia = fields.Char()
    municipio = fields.Char()
    telefono1 = fields.Char()
    telefono2 = fields.Char()
    iban = fields.Char()
    subscription_request_id = fields.Many2one("subscription.request")
    partner_id = fields.Many2one("res.partner")

    def get_gender(self):
        if self.genero == "1":
            return "male"
        elif self.genero == "2":
            return "female"
        else:
            return "other"

    def get_lastname(self):
        return "{} {}".format(self.primer_apellido, self.segundo_apellido)

    def get_representative_firstname(self):
        full_name = self.nombre_apellidos_representante.split(" ", 1)
        return full_name[0]

    def get_representative_lastname(self):
        full_name = self.nombre_apellidos_representante.split(" ", 1)
        if len(full_name) > 1:
            return full_name[1]
        else:
            return ""

    def get_phone(self):
        if self.telefono2:
            return "{}, {}".format(self.telefono1, self.telefono2)
        else:
            return self.telefono1

    def get_cooperator_vals(self, partner):
        values = {
            "date": partner.fechacreacion,
            "creation_date": partner.fechacreacion,
            "modification_date": partner.fechamodificacion,
            "firstname": partner.nombre,
            "lastname": partner.get_lastname(),
            "gender": partner.get_gender(),
            "email": partner.email,
            "address": partner.direccion,
            "zip_code": partner.codigo_postal,
            "city": partner.municipio,
            "country_id": 68,
            "lang": "es_ES",
            "phone": partner.get_phone(),
            "iban": partner.iban,
            "vat": partner.nif_nie,
            "share_product_id": 1,
            "notes": partner.observaciones,
        }
        return values

    def get_cooperator_company_vals(self, partner):
        values = {
            "is_company": True,
            "date": partner.fechacreacion,
            "creation_date": partner.fechacreacion,
            "modification_date": partner.fechamodificacion,
            "firstname": partner.get_representative_firstname(),
            "lastname": partner.get_representative_lastname(),
            "gender": partner.get_gender(),
            "email": partner.email,
            "company_email": "{} (copia)".format(partner.email),
            "address": partner.direccion,
            "zip_code": partner.codigo_postal,
            "city": partner.municipio,
            "country_id": 68,
            "lang": "es_ES",
            "phone": partner.get_phone(),
            "iban": partner.iban,
            "company_name": partner.razon_social,
            "vat": partner.cif,
            "share_product_id": 1,
            "company_register_number": partner.cif,
            "notes": partner.observaciones,
            "representative_vat": partner.nif_representante,
        }
        return values

    def get_partner_vals(self, partner):
        values = {
            "company_type": "person",
            "date": partner.fechacreacion,
            "creation_date": partner.fechacreacion,
            "modification_date": partner.fechamodificacion,
            "firstname": partner.nombre,
            "lastname": partner.get_lastname(),
            "gender": partner.get_gender(),
            "email": partner.email,
            "street": partner.direccion,
            "zip": partner.codigo_postal,
            "city": partner.municipio,
            "country_id": 68,
            "lang": "es_ES",
            "phone": partner.telefono1,
            "mobile": partner.telefono2,
            "vat": partner.nif_nie,
            "comment": partner.observaciones,
        }
        return values

    def get_partner_company_vals(self, partner):
        values = {
            "is_company": True,
            "company_type": "company",
            "date": partner.fechacreacion,
            "creation_date": partner.fechacreacion,
            "modification_date": partner.fechamodificacion,
            "gender": partner.get_gender(),
            "email": partner.email,
            "street": partner.direccion,
            "zip": partner.codigo_postal,
            "city": partner.municipio,
            "country_id": 68,
            "lang": "es_ES",
            "phone": partner.telefono1,
            "mobile": partner.telefono2,
            "name": partner.razon_social,
            "vat": partner.cif,
            "comment": partner.observaciones,
            "representative_vat": partner.nif_representante,
        }
        return values

    def create_subscription_request_or_partner(self):
        partners = self.env["import.cooperator"].browse(self.env.context["active_ids"])
        for partner in partners:
            logger.info("IMPORT PARTNER: {}".format(partner.id))
            is_partner = self.env["res.partner"].search(
                [
                    ("vat", "!=", False),
                    "|",
                    ("vat", "=", partner.cif),
                    ("vat", "=", partner.nif_nie),
                ]
            )
            is_cooperator = self.env["subscription.request"].search(
                [
                    ("vat", "!=", False),
                    "|",
                    ("vat", "=", partner.cif),
                    ("vat", "=", partner.nif_nie),
                ]
            )
            if is_partner or is_cooperator:
                continue
            if (
                partner.numero_cooperativista != "0"
                and partner.es_persona_juridica == "1"
            ):
                values = self.get_cooperator_company_vals(partner)
                job = self.env["subscription.request"].with_delay().create(values)
                logger.info(
                    "Created Job for coop company: {} {}".format(partner.id, job)
                )
            elif (
                partner.numero_cooperativista != "0"
                and partner.es_persona_juridica == "0"
            ):
                values = self.get_cooperator_vals(partner)
                job = self.env["subscription.request"].with_delay().create(values)
                logger.info(
                    "Created Job for coop person: {} {}".format(partner.id, job)
                )
            elif (
                partner.numero_cooperativista == "0"
                and partner.es_persona_juridica == "1"
            ):
                values = self.get_partner_company_vals(partner)
                job = self.env["res.partner"].with_delay().create(values)
                logger.info(
                    "Created Job for partner company: {} {}".format(partner.id, job)
                )
            else:
                values = self.get_partner_vals(partner)
                job = self.env["res.partner"].with_delay().create(values)
                logger.info(
                    "Created Job for partner person: {} {}".format(partner.id, job)
                )

    def validate(self):
        import_coops = self.env["import.cooperator"].search(
            [("subscription_request_id", "!=", False)]
        )
        sorted_import_coops = import_coops.sorted(key="fechacreacion")

        for import_coop in sorted_import_coops:
            import_coop.subscription_request_id.validate_subscription_request()
            partner = self.env["res_partner"].search([("vat", "=", import_coop.vat)])
            partner.write({"effective_date": import_coop.fechacreacion})
            invoice = self.env["account.move"].search([("partner_id", "=", partner.id)])
            invoice.write({"invoice_date": import_coop.fechacreacion})


class SubscriptionRequest(models.Model):
    _inherit = "subscription.request"

    def create(self, vals_list):
        req_set = super().create(vals_list)
        import_coop = self.env["import.cooperator"].search(
            ["|", ("cif", "=", req_set.vat), ("nif_nie", "=", req_set.vat)]
        )
        if not import_coop:
            return
        import_coop.subscription_request_id = req_set


class ResPartner(models.Model):
    _inherit = "res.partner"

    def create(self, vals_list):
        req_set = super().create(vals_list)
        if req_set.parent_id:
            return
        import_coop = self.env["import.cooperator"].search(
            ["|", ("cif", "=", req_set.vat), ("nif_nie", "=", req_set.vat)]
        )
        if not import_coop:
            return
        import_coop.partner_id = req_set
        if (
            import_coop.numero_cooperativista == "0"
            and import_coop.es_persona_juridica == "1"
        ):
            contact = self.env["res.partner"].create(
                {
                    "parent_id": req_set.id,
                    "firstname": import_coop.get_representative_firstname(),
                    "lastname": import_coop.get_representative_lastname(),
                    "type": "contact",
                    "email": import_coop.email,
                }
            )
        if import_coop.iban:
            self.env["res.partner.bank"].create(
                {"partner_id": req_set.id, "acc_number": import_coop.iban}
            )
