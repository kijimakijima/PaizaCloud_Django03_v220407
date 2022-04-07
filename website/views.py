from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"]="Takeda Rena"
        return ctxt

class AboutView(TemplateView):
    template_name="about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"]=12345655
        ctxt["skills"]=[
            "Python",
            "Perl",
            "Java",
            "HTML",
            "CSS",
            "JQuery",
        ]
        return ctxt
