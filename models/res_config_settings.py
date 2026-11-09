# -*- coding: utf-8 -*-
"""Parâmetros TotalPass (ir.config_parameter).

Conexão Asaas (API key, ambiente, token do webhook, taxas do cartão) é a mesma conta do
Wellhub: lida das chaves ``afr_wellhub.*`` e configurada em Configurações → Wellhub / Asaas.
"""

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    totalpass_default_subscription_value = fields.Float(
        string="Valor padrão da assinatura",
        default=0.0,
    )
    totalpass_default_billing_type = fields.Selection(
        selection=[
            ("UNDEFINED", "Indefinido"),
            ("BOLETO", "Boleto"),
            ("CREDIT_CARD", "Cartão de crédito"),
            ("PIX", "Pix"),
        ],
        string="Forma de pagamento padrão",
        config_parameter="afr_totalpass.default_billing_type",
        default="PIX",
    )
    totalpass_default_cycle = fields.Selection(
        selection=[
            ("WEEKLY", "Semanal"),
            ("BIWEEKLY", "Quinzenal"),
            ("MONTHLY", "Mensal"),
            ("BIMONTHLY", "Bimestral"),
            ("QUARTERLY", "Trimestral"),
            ("SEMIANNUALLY", "Semestral"),
            ("YEARLY", "Anual"),
        ],
        string="Periodicidade padrão",
        config_parameter="afr_totalpass.default_cycle",
        default="MONTHLY",
    )
    totalpass_asaas_timeout = fields.Integer(
        string="Timeout HTTP (s)",
        default=30,
    )
    totalpass_notification_package_fee = fields.Float(
        string="Pacote notif. e-mail + SMS (R$)",
        default=0.99,
        help="Referência pública Asaas: pacote de notificações por e-mail e SMS cobrado por "
        "cobrança paga (tabela em https://www.asaas.com/precos-e-taxas ). "
        "Taxas aplicáveis também em https://docs.asaas.com/docs/notificacoes — confira em Minha conta > Taxas.",
    )
    _portal_billing_selection = [
        ("", "Igual ao padrão geral (Assinaturas)"),
        ("UNDEFINED", "Indefinido"),
        ("BOLETO", "Boleto"),
        ("CREDIT_CARD", "Cartão de crédito"),
        ("PIX", "Pix"),
    ]
    _portal_cycle_selection = [
        ("", "Igual ao padrão geral (Assinaturas)"),
        ("WEEKLY", "Semanal"),
        ("BIWEEKLY", "Quinzenal"),
        ("MONTHLY", "Mensal"),
        ("BIMONTHLY", "Bimestral"),
        ("QUARTERLY", "Trimestral"),
        ("SEMIANNUALLY", "Semestral"),
        ("YEARLY", "Anual"),
    ]
    totalpass_portal_default_subscription_value = fields.Float(
        string="Valor assinatura (portal)",
        default=0.0,
        help="Se maior que zero, usado na inscrição pelo site e na ativação por e-mail. "
        "Se zero, usa o 'Valor padrão da assinatura' do bloco Assinaturas (padrão).",
    )
    totalpass_portal_default_billing_type = fields.Selection(
        selection=_portal_billing_selection,
        string="Forma de pagamento (portal)",
        default="",
        help="Vazio = mesmo padrão do bloco 'Assinaturas (padrão)'. Defina aqui para forçar "
        "Pix, Boleto ou Cartão nos colaboradores vindos do formulário público.",
    )
    totalpass_portal_default_cycle = fields.Selection(
        selection=_portal_cycle_selection,
        string="Periodicidade (portal)",
        default="",
        help="Vazio = mesmo padrão do bloco 'Assinaturas (padrão)'.",
    )
    totalpass_portal_pass_notification_email_sms_fee = fields.Boolean(
        string="Portal: repassar pacote e-mail/SMS",
        default=True,
        help="Aplicado ao criar/atualizar inscrição pelo site e ao confirmar o link do e-mail.",
    )
    totalpass_portal_pass_credit_card_fee_to_customer = fields.Boolean(
        string="Portal: repassar taxa do cartão",
        default=True,
        help="Aplicado ao criar/atualizar inscrição pelo site e ao confirmar o link do e-mail.",
    )
    # --- Juros, multa e desconto (Assinaturas padrão) — aplicados a novos colaboradores no backend. ---
    totalpass_default_asaas_discount_type = fields.Selection(
        selection=[
            ("none", "Sem desconto"),
            ("PERCENTAGE", "Percentual sobre a cobrança"),
            ("FIXED", "Valor fixo (R$)"),
        ],
        string="Tipo de desconto (padrão)",
        default="none",
    )
    totalpass_default_asaas_discount_value = fields.Float(
        string="Valor do desconto (padrão)",
        default=0.0,
    )
    totalpass_default_asaas_discount_due_date_limit_days = fields.Integer(
        string="Desconto: dias antes do vencimento (padrão)",
        default=0,
    )
    totalpass_default_asaas_interest_monthly_percent = fields.Float(
        string="Juros ao mês % (padrão)",
        default=0.0,
    )
    totalpass_default_asaas_fine_type = fields.Selection(
        selection=[
            ("none", "Sem multa"),
            ("PERCENTAGE", "Percentual sobre a cobrança"),
            ("FIXED", "Valor fixo (R$)"),
        ],
        string="Tipo de multa (padrão)",
        default="none",
    )
    totalpass_default_asaas_fine_value = fields.Float(
        string="Valor da multa (padrão)",
        default=0.0,
    )
    # --- Portal: sobrescreve o bloco acima quando não for "Igual ao padrão". ---
    _inherit_discount_selection = [
        ("inherit", "Igual ao padrão (Assinaturas)"),
        ("none", "Sem desconto"),
        ("PERCENTAGE", "Percentual sobre a cobrança"),
        ("FIXED", "Valor fixo (R$)"),
    ]
    _inherit_fine_selection = [
        ("inherit", "Igual ao padrão (Assinaturas)"),
        ("none", "Sem multa"),
        ("PERCENTAGE", "Percentual sobre a cobrança"),
        ("FIXED", "Valor fixo (R$)"),
    ]
    totalpass_portal_asaas_discount_type = fields.Selection(
        selection=_inherit_discount_selection,
        string="Tipo de desconto (portal)",
        default="inherit",
    )
    totalpass_portal_asaas_discount_value = fields.Float(
        string="Valor do desconto (portal)",
        default=0.0,
        help="Usado quando o tipo no portal não for 'Igual ao padrão'. Se zero e tipo explícito, pode falhar validação — informe conforme o tipo.",
    )
    totalpass_portal_asaas_discount_due_date_limit_days = fields.Integer(
        string="Desconto: dias antes do venc. (portal)",
        default=0,
    )
    totalpass_portal_asaas_interest_mode = fields.Selection(
        selection=[
            ("inherit", "Igual ao padrão (Assinaturas)"),
            ("custom", "Definir juros ao mês abaixo"),
        ],
        string="Juros ao mês (portal)",
        default="inherit",
    )
    totalpass_portal_asaas_interest_monthly_percent = fields.Float(
        string="Juros ao mês % (portal)",
        default=0.0,
        help="Somente quando 'Definir juros ao mês abaixo' está selecionado.",
    )
    totalpass_portal_asaas_fine_type = fields.Selection(
        selection=_inherit_fine_selection,
        string="Tipo de multa (portal)",
        default="inherit",
    )
    totalpass_portal_asaas_fine_value = fields.Float(
        string="Valor da multa (portal)",
        default=0.0,
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        icp = self.env["ir.config_parameter"].sudo()
        res["totalpass_default_subscription_value"] = float(
            icp.get_param("afr_totalpass.default_subscription_value", "0") or 0
        )
        res["totalpass_asaas_timeout"] = int(
            icp.get_param("afr_totalpass.asaas_timeout", "30") or 30
        )
        res["totalpass_notification_package_fee"] = float(
            icp.get_param("afr_totalpass.notification_package_fee", "0.99") or 0
        )
        res["totalpass_portal_default_subscription_value"] = float(
            icp.get_param("afr_totalpass.portal_default_subscription_value", "0") or 0
        )
        res["totalpass_portal_default_billing_type"] = (
            icp.get_param("afr_totalpass.portal_default_billing_type", "") or ""
        )
        res["totalpass_portal_default_cycle"] = (
            icp.get_param("afr_totalpass.portal_default_cycle", "") or ""
        )
        res["totalpass_portal_pass_notification_email_sms_fee"] = (
            icp.get_param(
                "afr_totalpass.portal_pass_notification_email_sms_fee", "true"
            )
            or "true"
        ).lower() in ("1", "true", "yes", "on")
        res["totalpass_portal_pass_credit_card_fee_to_customer"] = (
            icp.get_param(
                "afr_totalpass.portal_pass_credit_card_fee_to_customer", "true"
            )
            or "true"
        ).lower() in ("1", "true", "yes", "on")
        res["totalpass_default_asaas_discount_type"] = (
            icp.get_param("afr_totalpass.default_asaas_discount_type", "none") or "none"
        )
        res["totalpass_default_asaas_discount_value"] = float(
            icp.get_param("afr_totalpass.default_asaas_discount_value", "0") or 0
        )
        res["totalpass_default_asaas_discount_due_date_limit_days"] = int(
            float(icp.get_param("afr_totalpass.default_asaas_discount_due_date_limit_days", "0") or 0)
        )
        res["totalpass_default_asaas_interest_monthly_percent"] = float(
            icp.get_param("afr_totalpass.default_asaas_interest_monthly_percent", "0") or 0
        )
        res["totalpass_default_asaas_fine_type"] = (
            icp.get_param("afr_totalpass.default_asaas_fine_type", "none") or "none"
        )
        res["totalpass_default_asaas_fine_value"] = float(
            icp.get_param("afr_totalpass.default_asaas_fine_value", "0") or 0
        )
        res["totalpass_portal_asaas_discount_type"] = (
            icp.get_param("afr_totalpass.portal_asaas_discount_type", "inherit") or "inherit"
        )
        res["totalpass_portal_asaas_discount_value"] = float(
            icp.get_param("afr_totalpass.portal_asaas_discount_value", "0") or 0
        )
        res["totalpass_portal_asaas_discount_due_date_limit_days"] = int(
            float(icp.get_param("afr_totalpass.portal_asaas_discount_due_date_limit_days", "0") or 0)
        )
        res["totalpass_portal_asaas_interest_mode"] = (
            icp.get_param("afr_totalpass.portal_asaas_interest_mode", "inherit") or "inherit"
        )
        res["totalpass_portal_asaas_interest_monthly_percent"] = float(
            icp.get_param("afr_totalpass.portal_asaas_interest_monthly_percent", "0") or 0
        )
        res["totalpass_portal_asaas_fine_type"] = (
            icp.get_param("afr_totalpass.portal_asaas_fine_type", "inherit") or "inherit"
        )
        res["totalpass_portal_asaas_fine_value"] = float(
            icp.get_param("afr_totalpass.portal_asaas_fine_value", "0") or 0
        )
        return res

    def set_values(self):
        super().set_values()
        icp = self.env["ir.config_parameter"].sudo()
        icp.set_param(
            "afr_totalpass.default_subscription_value",
            str(float(self.totalpass_default_subscription_value or 0)),
        )
        icp.set_param(
            "afr_totalpass.asaas_timeout",
            str(int(self.totalpass_asaas_timeout or 30)),
        )
        icp.set_param(
            "afr_totalpass.notification_package_fee",
            str(float(self.totalpass_notification_package_fee or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_default_subscription_value",
            str(float(self.totalpass_portal_default_subscription_value or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_default_billing_type",
            (self.totalpass_portal_default_billing_type or "").strip(),
        )
        icp.set_param(
            "afr_totalpass.portal_default_cycle",
            (self.totalpass_portal_default_cycle or "").strip(),
        )
        icp.set_param(
            "afr_totalpass.portal_pass_notification_email_sms_fee",
            "true" if self.totalpass_portal_pass_notification_email_sms_fee else "false",
        )
        icp.set_param(
            "afr_totalpass.portal_pass_credit_card_fee_to_customer",
            "true" if self.totalpass_portal_pass_credit_card_fee_to_customer else "false",
        )
        icp.set_param(
            "afr_totalpass.default_asaas_discount_type",
            self.totalpass_default_asaas_discount_type or "none",
        )
        icp.set_param(
            "afr_totalpass.default_asaas_discount_value",
            str(float(self.totalpass_default_asaas_discount_value or 0)),
        )
        icp.set_param(
            "afr_totalpass.default_asaas_discount_due_date_limit_days",
            str(int(self.totalpass_default_asaas_discount_due_date_limit_days or 0)),
        )
        icp.set_param(
            "afr_totalpass.default_asaas_interest_monthly_percent",
            str(float(self.totalpass_default_asaas_interest_monthly_percent or 0)),
        )
        icp.set_param(
            "afr_totalpass.default_asaas_fine_type",
            self.totalpass_default_asaas_fine_type or "none",
        )
        icp.set_param(
            "afr_totalpass.default_asaas_fine_value",
            str(float(self.totalpass_default_asaas_fine_value or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_discount_type",
            self.totalpass_portal_asaas_discount_type or "inherit",
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_discount_value",
            str(float(self.totalpass_portal_asaas_discount_value or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_discount_due_date_limit_days",
            str(int(self.totalpass_portal_asaas_discount_due_date_limit_days or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_interest_mode",
            self.totalpass_portal_asaas_interest_mode or "inherit",
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_interest_monthly_percent",
            str(float(self.totalpass_portal_asaas_interest_monthly_percent or 0)),
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_fine_type",
            self.totalpass_portal_asaas_fine_type or "inherit",
        )
        icp.set_param(
            "afr_totalpass.portal_asaas_fine_value",
            str(float(self.totalpass_portal_asaas_fine_value or 0)),
        )
