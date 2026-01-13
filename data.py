# Todos os dados do portfólio centralizados para fácil manutenção
USER_DATA = {
    "name": "Luiz Felipe Souza da Silva Meneses",
    "role": "Desenvolvedor Full Stack & Estagiário de TI",
    "location": "Vicente Pires, Brasília - DF",
    "bio": "Graduando em Sistemas de Informação pela UniEURO (8º semestre). Desenvolvedor Full Stack especializado em Python/Flask com experiência em sistemas governamentais corporativos. Expertise em integração LDAP/Active Directory, arquitetura MVC, análise de dados e automação de processos. Focado em criar soluções escaláveis e seguras.",
    "email": "luiz.felipe.menesez@gmail.com",
    "social": {
        "github": "https://github.com/LuizBigs",
        "linkedin": "https://www.linkedin.com/in/luiz-felipe-ss-meneses",
        "twitter": "https://twitter.com/luizfelipe"
    },
    "skills": {
        "Backend": ["Python", "Flask", "SQLAlchemy", "MySQL", "LDAP/AD", "ETL"],
        "Frontend": ["JavaScript", "jQuery", "Bootstrap", "Tailwind CSS", "Chart.js"],
        "Ferramentas": ["Git", "VSCode", "Zabbix", "JIRA", "DataTables"],
        "Práticas": ["Arquitetura MVC", "Design Patterns", "Metodologias Ágeis", "QA", "Security Best Practices"]
    },
    "experience": [
        {
            "company": "SEJUS - Secretaria de Estado de Justiça",
            "role": "Estagiário de TI",
            "period": "Junho 2024 - Dezembro 2025",
            "description": "Desenvolvimento de sistemas web com Python/Flask, análise e ETL de dados corporativos, automação de processos, monitoramento de infraestrutura com Zabbix, suporte técnico e QA. Atuação com metodologias ágeis em ambiente governamental."
        }
    ],
    "projects": [
        {
            "title": "Sistema de Monitoramento SUBSIS",
            "description": "Sistema web de monitoramento e verificação do andamento de obras nas unidades de internação da Subsecretaria do Sistema Penitenciário. Controle completo com registro fotográfico, assinaturas digitais, geração automatizada de relatórios em PDF/Excel e dashboards analíticos com Chart.js. Integração LDAP/AD com perfis granulares de acesso.",
            "tech": ["Python", "Flask", "SQLAlchemy", "LDAP3", "MySQL", "Chart.js", "wkhtmltopdf"],
            "image": "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&w=800&q=80",
            "link": "https://monitoramentosubsis.sejus.df.gov.br/"
        },
        {
            "title": "Central de Serviços - Suporte SEJUS",
            "description": "Sistema corporativo de gestão de chamados e serviços que digitaliza o fluxo completo de solicitações internas. Implementa autenticação SSO via Active Directory, notificações em tempo real com polling otimizado, chat integrado com anexos, formulários dinâmicos configuráveis e dual database binding. Redução de 80% no tempo de abertura de chamados.",
            "tech": ["Python", "Flask", "LDAP", "MySQL", "jQuery", "Bootstrap", "DataTables"],
            "image": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80",
            "link": "http://suporte.sejus.df.gov.br/"
        },
        {
            "title": "DITRANS - Gestão de Frota (SUAG)",
            "description": "Módulo de gestão de frota veicular com conformidade ao Decreto 16.109/1994. Sistema completo de registro de movimentações, empréstimo de veículos, inspeção obrigatória, documentação fotográfica e rastreabilidade total. Implementa controle de permissões granular (Admin/Unit Admin/User) e soft delete para auditoria completa.",
            "tech": ["Python", "Flask", "SQLAlchemy", "MySQL", "Tailwind CSS", "JavaScript"],
            "image": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=800&q=80",
            "link": "http://suag.sejus.df.gov.br/"
        }
    ]
}