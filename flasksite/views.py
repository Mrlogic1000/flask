from flask import Blueprint, render_template


views = Blueprint(__name__, '/')


@views.route("/")
def home():
    return render_template("index.html",active='home')




educations = [{
    'year':'2019-2023',
    'title':'Higher National Diplomer in Computer Science',
    'school':'Polytechnic of Ibadan-Oyo state',
    'Relevant Coursework':[' Data Structure', 'Computer Networking', 'Web Development'],
    'Capstone Project':' AI-Powered Chatbot for Campus Navigation'
},
{
    'year':'2010-2013',
    'title':'Cisco Certified Internetwork Expert',
    'school':'CISCO Academy',
    'Relevant Coursework': [
        'CISCO Enterprise solutions', 
     'Dual-stack (IPv4 and IPv6) architecture', 
     'Routing protocols:OSPF,EIGRP, BGP, MPLS,IS-IS',
     'Network automation and programmability (Python, APIs, NetConf/YANG)',
     'Software-Defined Networking (SDN): Cisco DNA Center, SD-Access',
     'Infrastructure Security',
     'QoS (Quality of Service)',
     'Network Assurance and monitoring'
     ],
    'Capstone Project':'Repair and Assemble of Computer'
},
{
    'year':'2025',
    'title':'Cisco Certified Internetwork Expert',
    'school':'CISCO Academy',
    'Relevant Coursework': [
        'Covered ethical hacking methodology', 
     'penetration testing', 
     'vulnerability scanning',
     'social engineering',
     'exploitation of wired/wireless & application-based vulnerabilities',
     'post exploitation reporting'          
     ],
    'Capstone Project':'Repair and Assemble of Computer'
},
{
    'year':'2010-2013',
    'title':'Certificate of Competence in Computer Engineering',
    'school':'Federal Ministry Of Labour',
    'Relevant Coursework':['Repair of computer','Assemble of Computer'],
    'Capstone Project':'Repair and Assemble of Computer'
},

]


experiences = [
    {
        'year':'2011-2018',
        'title':'Remote Monitoring System Installer',
        'company':'LAWI Global Concept',
        'area':' Lagos',
        'description':[
            'Installed and configured remote monitoring systems (RMS) for industrial, commercial, and/or residential clients.',
            'Integrated sensors and control units for environmental, power, and equipment monitoring.',
            'Calibrated and tested sensors (e.g., temperature, humidity, vibration, voltage/current) to ensure accurate data acquisition.',
            'Set up communication systems using wired and wireless protocols (e.g., Wi-Fi, GSM, LoRa, Zigbee).',
            'Ensured secure connectivity between field devices and remote dashboards/cloud platforms.',
            'Conducted client training, system documentation, and post-installation support.'

        ]

    },
    {
        'year':'2012-2015',
        'title':'Remote Monitoring System Installer',
        'company':'AIO',
        'area':' Lagos',
        'description':[
            'Installed and configured remote monitoring systems (RMS) for industrial, commercial, and/or residential clients.',
             'Set up communication systems using wired and wireless protocols (e.g., Wi-Fi, GSM, LoRa, Zigbee).',
            'Integrated sensors and control units for environmental, power, and equipment monitoring.',
            'Calibrated and tested sensors (e.g., temperature, humidity, vibration, voltage/current) to ensure accurate data acquisition.',           
            'Ensured secure connectivity between field devices and remote dashboards/cloud platforms.',
            'Conducted client training, system documentation, and post-installation support.'

        ]

    },
    {
        'year':'2014-2020',
        'title':'Site Manager',
        'company':'GALOOLI',
        'area':' Lagos',
        'description':[
            'Ensured secure connectivity between field devices and remote dashboards/cloud platforms.',
            'Installed and configured remote monitoring systems (RMS) for industrial, commercial, and/or residential clients.',
            'Integrated sensors and control units for environmental, power, and equipment monitoring.',
            'Calibrated and tested sensors (e.g., temperature, humidity, vibration, voltage/current) to ensure accurate data acquisition.',
            'Set up communication systems using wired and wireless protocols (e.g., Wi-Fi, GSM, LoRa, Zigbee).',            
            'Conducted client training, system documentation, and post-installation support.'

        ]

    },
    {
        'year':'2020-Till',
        'title':'Network Administrator Manager',
        'company':'Golden Tulip Ibadan',
        'area':' Ibadan',
        'description':[
            'Led a team of network administrators and technicians managing enterprise-wide network infrastructure.',
            'Designed, implemented, and maintained LAN/WAN architecture, firewalls, routers, switches, and VPNs.',
            'Oversaw security protocols, access control policies, and regular vulnerability assessments to ensure data integrity.',
            'Managed vendor relationships, network procurement, and third-party service contracts.',
            'Developed disaster recovery strategies, network documentation, and operational procedures.',            
            'Ensured 24/7 uptime and minimal network disruption through monitoring tools and proactive maintenance.'

        ]

    },
]

works = [
    {
        'title':'Network Design & Implementation',
        'icon':'fa-share-alt',
        'option':[
            'Design of LAN, WAN, and WLAN architectures',
                  'Structured cabling planning and implementation',
                  'Network hardware configuration (routers, switches, firewalls)',
                  ]
    },
    {
        'title':'IT Infrastructure Design & Deployment',
        'icon':'fa-server',
        'option':['Network architecture (LAN/WAN)',
                  'Server setup (Windows/Linux)',
                  'Cloud infrastructure (AWS, Azure, GCP)',
                  ]
    },
    {
        'title':'System Administration & Support',
        'icon':'fa-database',
        'option':['Routine maintenance and patching',
                  'User and permissions management',
                  'Monitoring and incident response',
                  ]
    },
    {
        'title':'Custom Website Developments',
        'icon':'fa-code',
        'option':['Responsive, mobile-first design',
                  'HTML5, CSS3, JavaScript, and modern frameworks (React, Vue, etc.)',
                  'SEO-friendly, fast-loading websites',
                  ]
    },
    {
        'title':'Cybersecurity Solutions',
        'icon':'fa-globe',
        'option':['Vulnerability assessment',
                  'Firewall & endpoint security configuration',
                  'Security policy development',
                  ]
    },
    {
        'title':'Technical Consulting & IT Project Management',
        'icon':'fa-thumbs-up',
        'option':[
            'IT roadmapping and budgeting',
                  'Vendor and stakeholder coordination',
                  'Documentation & reporting',
                  ]
    },
    {
        'title':'Network Security & Firewall Configuration',
        'icon':'fa-cloud',
        'option':[
            'Firewall setup and rule management (Cisco ASA, pfSense, Fortinet)',
                  'VPN configuration (IPSec, SSL, Site-to-Site)',
                  'Intrusion Detection/Prevention Systems (IDS/IPS)',
                  ]
    },
    {
        'title':'Server & Network Infrastructure Management',
        'icon':'fa-desktop',
        'option':[
            'Installation and administration of Windows & Linux servers',
                  'Active Directory, DHCP, DNS, and file server management',
                  'Virtualization (VMware, Hyper-V, Proxmox)',
                  ]
    },
    {
        'title':'Renewable Energy Solutions',
        'icon':'fa-plug',
        'option':[
            'Solar PV system design & integration',
                  'Battery storage systems',
                  'Grid-tied and off-grid systems',
                  ]
    },
    
]

@views.route("/about")
def about():
    return render_template("about.html",active='about', educations=educations, experiences = experiences)

@views.route("/contact")
def contact():
    return render_template("contact.html",active='contact')

@views.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",active='portfolio')

@views.route("/services")
def services():
    return render_template("services.html",active='services', works=works)