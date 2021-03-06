from django.core.management.base import BaseCommand, CommandError
from products.models import Item

class Command(BaseCommand):
    help = "Adds test items to database"

    def handle(self, *args, **options):
        #item = Item(name='', description='''''', price="", category="", image="images/.jpg")
        #item.save()
        
        #motherboards
        item = Item(name='GIGABYTE Z390 AORUS XTREME LGA 1151 (300 Series) Intel Z390 HDMI THUNDERBOLT 3 USB 3.1 Extended ATX Intel Motherboard', description='''
•Supports Intel 8th & 9th Gen Core i9/i7/i5/i3, Celeron, and Pentium Processors
•Dual Channel Non-ECC Unbuffered DDR4, 4 DIMMs
•Intel Optane Memory Ready
•16 Phases IR Digital VRM Solution with PowIRstage
•Thermal Design with Fins-Array Heatsink, Direct Touch Heatpipe, NanoCarbon Baseplate
•Onboard Intel CNVI 802.11 ac 2x2 Wave 2 Wi-Fi with All new AORUS Antenna
•AMP-UP Audio with High-End ESS SABRE 9018K2M DAC
•AQUANTIA 10GbE BASE-T LAN and Intel Gigabit LAN with cFosSpeed
•Intel Thunderbolt 3 onboard
•Exclusive RGB FAN COMMANDER and OC Touch
•USB TurboCharger for mobile device fast charge support
•RGB FUSION with Multi-Zone Addressable LED Light Show design
•Smart Fan 5 features Multiple Temperature Sensors
•Front USB 3.1 Gen 2 Type-C Header
•Triple Ultra-Fast M.2 with Triple Thermal Guards''', price="549.99", category="Motherboards", image="images/Motherboard1.jpg")
        item.save()
        item = Item(name='ASUS ROG Dominus Extreme Intel LGA 3647 for Xeon W-3175X (C621) 12 DIMM DDR4 DIMM.2 U.2 EEB Performance Motherboard with Aquantia 10G LAN, USB 3.1', description='''
•LGA 3647 socket, engineered to overclock Intel Xeon W-3175X processors
•Designed for extreme performance, dual 24-pin, quad 8-pin and dual 6-pin 12V power connectors that deliver industry-leading power efficiency
•Quad strength graphic power featuring 4-Way PCIe 3.0 link supporting NVIDIA GeForce SLI, NVIDIA NVLink and AMD CrossFireX
•Built for high performance networking: Onboard Aquantia AQC-107 10G LAN, Intel I219-LM Gigabit LAN, Intel Wireless AC-9260 Wi-Fi (802.11 ac) and ROG GameFirst technology
•5-Way Optimization featuring Auto-Tuning and FanXpert 4 provides automatic overclocking profiles for maximum OC performance, plus 14 PWM fan headers to support dynamic system cooling''', price="1799.99", category='Motherboards', image="images/Motherboard2.jpg")
        item.save()
        item = Item(name='MSI MEG Z390 ACE LGA 1151 (300 Series) Intel Z390 SATA 6Gb/s USB 3.1 ATX Intel Motherboard', description='''
•Intel Z390
•Supports 9th/8th Gen Intel Core / Pentium Gold / Celeron processors for LGA 1151 socket
•* Not backward compatible with older generation of LGA 1151 CPUs
•DDR4 4500(OC)/ 4400(OC)/ 4300(OC)/ 4266(OC)/ 4200(OC)/ 4133(OC)/ 4000(OC)/ 3866(OC)/ 3733(OC)/ 3600(OC)/ 3466(OC)/ 3400(OC)/ 3333(OC)/ 3300(OC)/ 3200(OC)/ 3000(OC)/ 2800(OC)/ 2666/ 2400/ 2133''', price="289.99", category='Motherboards', image="images/Motherboard3.jpg")
        item.save()
        item = Item(name='ASRock Z390 Phantom Gaming 9 LGA 1151 (300 Series) Intel Z390 HDMI SATA 6Gb/s USB 3.1 ATX Intel Motherboards', description='''
•Intel Z390
•Supports 9th and 8th Gen Intel Core processors (Socket 1151)
•* Not backward compatible with older generation of LGA 1151 CPUs
•On board LAN support 10/100/1000/2500Mbps + Dual 10/100/1000Mbps
•DDR4 4200+(OC)*/ 4133(OC)/ 4000(OC)/ 3866(OC)/ 3800(OC)/ 3733(OC)/ 3600(OC)/ 3200(OC)/ 2933(OC)/ 2800(OC)/ 2666/ 2400/ 2133
•* Please refer to Memory Support List on ASRock's website for more information. (http://www.asrock.com/)''', price="268.99", category='Motherboards', image="images/Motherboard4.jpg")
        item.save()
        item = Item(name='EVGA 123-CS-E397-KR LGA 1151 (300 Series) Intel Z390 SATA 6Gb/s ATX Intel Motherboard', description='''
•Intel Z390
•Supports 8th/9th Generation Intel Processsor Family for LGA1151 socket
•* Not backward compatible with older generation of LGA 1151 CPUs
•DDR4 4133 +''', price="229.99", category='Motherboards', image="images/Motherboard5.jpg")
        item.save()
        item = Item(name='EVGA X299 FTW K, 142-SX-E297-KR, LGA 2066, Intel X299, SATA 6Gb/s, USB 3.1, USB 3.0, EATX, Intel Motherboard', description='''
•Intel X299 Chipset - supports Intel Core X-Series 7th Generation Processor Family for 2066 socket.
•EATX Form Factor. Supports up to 3-Way SLI.
•8 DIMM Quad-Channel DDR4 up to 128GB 4000MHz+ Skylake-X, and 64GB 4133MHz+ Kaby Lake-X. 2 x USB 3.1 (Type-A/Type-C), 8 x USB 3.0, and 4 x USB 2.0.
•8 SATA III 6Gb/s ports, 2 x M.2 Key-M - 1 x 110mm, 1 x 80mm (up to 32Gbps), 1 x M.2 Key-E 32mm, Intel Optane Memory Ready. 2 x U.2 Ports.
•Killer E2500 + Intel i219v Gigabit NIC. Highly-Efficient 14 Phase Digital VRM. RGB LED I/O cover, PCH Heatsink, and fan header support.''', price="349.00", category='Motherboards', image="images/Motherboard6.jpg")
        item.save()
        
        #CPUs
        item = Item(name='AMD Ryzen 5 2600 Processor with Wraith Stealth Cooler - YD2600BBAFBOX', description='''
•6 Cores/12 Threads UNLOCKED
•Frequency: 3.9 GHz Max Boost. Includes Wraith Stealth Cooler
•19MB of Combined Cache. Maximum temperature: 95°C
•Compatibility : Windows 10 - 64-Bit Edition , RHEL x86 64-Bit , Ubuntu x86 64-Bit
•Supported technologies are amd storemi technology, amd sensemi technology, amd ryzen master utility and amd ryzen vr-ready premium''', price="199.00", category="CPU", image="images/CPU1.jpg")
        item.save()
        item = Item(name='AMD Ryzen 7 2700X Processor with Wraith Prism LED Cooler - YD270XBGAFBOX', description='''
•8 Cores/16 Threads UNLOCKED
•Frequency: 4.3 GHz Max Boost
•Compatibility : Windows 10 - 64-Bit Edition , RHEL x86 64-Bit , Ubuntu x86 64-Bit
•20MB of Combined Cache
•Socket AM4 Motherboard Required''', price="329.00", category="CPU", image="images/CPU2.jpg")
        item.save()
        item = Item(name='Intel Core i7-9700K Desktop Processor 8 Cores up to 4.9 GHz Turbo Unlocked LGA1151 300 Series 95W', description='''
•8 Cores / 8 Threads
•3.60 GHz up to 4.90 GHz / 12 MB Cache
•Compatible only with Motherboards based on Intel 300 Series Chipsets
•Intel Optane Memory Supported
•Intel UHD Graphics 630''', price="409.99", category="CPU", image="images/CPU3.jpg")
        item.save()
        item = Item(name='Intel Core i7-8700K Desktop Processor 6 Cores up to 4.7GHz Turbo Unlocked LGA1151 300 Series 95W', description='''
•Intel UHD Graphics 630
•Compatible only with Motherboards based on Intel 300 Series Chipsets
•6 Cores / 12 Threads
•3.70 GHz up to 4.70 GHz Max Turbo Frequency / 12 MB Cache
•Intel Optane Memory Supported''', price="375.99", category="CPU", image="images/CPU4.jpg")
        item.save()
        item = Item(name='Intel Core i9-9900K Desktop Processor 8 Cores up to 5.0 GHz Turbo Unlocked LGA1151 300 Series 95W', description='''
•8 Cores / 16 Threads
•3.60 GHz up to 5.00 GHz / 16 MB Cache
•Compatible only with Motherboards based on Intel 300 Series Chipsets
•Intel Optane Memory Supported
•Intel UHD Graphics 630''', price="524.99", category="CPU", image="images/CPU5.jpg")
        item.save()
        item = Item(name='AMD Ryzen 3 2200G Processor with Radeon Vega 8 Graphics', description='''
•Built-In Radeon Vega 8 Graphics
•4 Cores UNLOCKED
•Frequency: 3.7 GHz Max Boost
•Socket Type: AM4. Max System Memory Speed : 2667MHz
•Thermal Solution: Wraith Stealth Cooler''', price="99.57", category="CPU", image="images/CPU6.jpg")
        item.save()
        
        #GPUs
        item = Item(name='XFX Radeon RX 580 GTS XXX Edition 1386MHz OC+, 8GB GDDR5, VR Ready, Dual BIOS, 3xDP HDMI DVI, AMD Graphics Card (RX-580P8DFD6)', description='''
•The XFX RX 580 series graphics card feature the latest Polaris architecture which includes the 4th Gen GCN graphics cores, a brand new display engine, new multimedia cores, all on the revolutionary Next FinFET 14 process technology for enhanced performance and efficiency.
•Equipped with XFX Double Dissipation Cooling Technology for optimal cooling and performance
•Multiple Factory GPU Overclocked Settings – 1366MHz True Clock and 1386MHz OC+
•AMD VR Ready Premium -Experience the new generation of compelling Virtual Reality content with the Radeon RX GTS graphics card paired with the leading VR headsets. The Radeon RX GTS graphics card coupled with AMD LiquidVR technology delivers a virtually stutter-free, low latency experience, essential for remarkable Virtual Reality environments.''', price="199.99", category="GPU", image="images/GPU1.jpg")
        item.save()
        item = Item(name='MSI Gaming GeForce GT 710 2GB GDRR3 64-bit HDCP Support DirectX 12 OpenGL 4.5 Single Fan Low Profile Graphics Card (GT 710 2GD3 LP)', description='''
•Chipset: NVIDIA GeForce GT 710;Maximum Displays : 2
•Video Memory: 2GB DDR3/Memory Clock: 1600 MHz/Memory Interface: 64-bit
•300W System Power Supply Requirement. Interface is pci express 2.0 x16 uses x8
•Connectors: VGA, DVI-D Dual Link, HDMI. Form Factor: Low-profile
•Hdmi connectors is maximum resolution 4096 x 2160 at 24 hertz. Dvi connectors is maximum resolution 2560 x 1600 at 60 hertz''', price="51.99", category="GPU", image="images/GPU2.jpg")
        item.save()
        item = Item(name='MSI Computer Video Graphic Cards GeForce GTX 1050 TI Gaming X 4G', description='''
•Chipset: NVIDIA GeForce GTX 1050 It
•Video Memory: 4GB GDDR5
•Memory Interface: 128-bit
•Max. Resolution: 2560 x 1600, Support 3x Display Monitors.
•Card dimension(mm):229 x 131 x 39.Digital Maximum Resolution: 7680 x 4320''', price="239.99", category="GPU", image="images/GPU3.jpg")
        item.save()
        item = Item(name='Gigabyte Geforce GTX 1050 2GB GDDR5 128 Bit PCI-E Graphic Card (GV-N1050OC-2GD)', description='''
•New NVIDIA pascal architecture delivers improved performance and power efficiency
•Classic and modern games at 1080P @ 60 FPS. Recommend operating system is windows 10, windows 8 and windows 7
•Fast, smooth, power-efficient gaming experiences
•Support for the latest DirectX 12 Features. Recommended PSU-300W. Multi-view-3. Digital max resolution-7680x4320
•Delivers all the latest GeForce gaming Features. Card size: H=1.41 L=7.5 W=4.4 inches''', price="149.99", category="GPU", image="images/GPU4.jpg")
        item.save()
        item = Item(name='EVGA GeForce GTX 1060 SC GAMING, ACX 2.0 (Single Fan), 6GB GDDR5, DX12 OSD Support (PXOC), Only 6.8 Inches Graphics Card 06G-P4-6163-KR', description='''
•Real Base Clock: 1607 MHz / Real Boost Clock: 1835 MHz; Memory Detail: 6144MB GDDR5. Revolutionary new 360-degree image capture
•EVGA GeForce GTX 1060 SC - Small Size, Huge Performance. Height: 4.376in - 111.15mm; Length: 6.8in - 172.72mm; Width: Dual Slot
•What you see is what you get! – No additional software required to achieve listed clock speeds
•DX12 OSD Support with EVGA Precision XOC. Requirements: Minimum of a 400 Watt power supply, 6-pin PCIe power connector
•3 Year Warranty & EVGA's 24/7 Technical Support.Operating System Support:Windows 7,8,10(32/64bit).OpenGL 4.6 Support
•Form Factor: Plug-in Card. Max Monitors Supported: 4, 240Hz Max Refresh Rate, Max Digital : 7680 x 4320
•Get Grip Game + EVGA Vehicle Skin w/ purchase, redeemed at EVGA website, while supplies last''', price="299.99", category="GPU", image="images/GPU5.jpg")
        item.save()
        item = Item(name='EVGA GeForce RTX 2070 Black Gaming,8GB GDDR6, Dual HDB Fans Graphics Card 08G-P4-1071-KR', description='''
•Real Boost Clock: 1620 MHz; memory Detail: 8192MB GDDR6
•Dual HDB fans and all-new cooler offer higher performance cooling and much quieter acoustic noise
•Built for EVGA Precision x1 - EVGA all-new tuning utility monitors your graphics card and gives you the power to overclock like a Pro!
•3 year & EVGA 24/7 technical support
•Get grip game + EVGA vehicle skin w/ Purchase, redeemed at EVGA website, while supplies last''', price="489.99", category="GPU", image="images/GPU6.jpg")
        item.save()
        
        #Cases
        item = Item(name='MasterBox Pro 5 RGB ATX Mid-Tower with 3 x 120mm RGB Fans, Tempered Glass Side Panel, DarkMirror Front Panel and Internal Configuration by Cooler Master', description='''
•Flexible mounting: easily mount and rearrange SSDs across the motherboard tray and on the back with the SSD bracket
•RGB Fans* - Three 120mm RGB fans are pre installed behind the front panel to create an amazing lighting effect
•1 to 3 Splitter Cable for RGB LED Fans* – The RGB Connector Splitter and 4 pin male to male adapters are included
•Compact cooling: with the included bracket, the case supports up to three 120mm front fans, one 120mm rear fan, and up to 360mm front radiator for liquid cooling
•4mm thick edge to edge tempered glass side panel: once you finished your build it's time to show off your creation in style through the 4mm thick edge to edge Tempered glass side panel''', price="79.99", category="Cases", image="images/Case1.jpg")
        item.save()
        item = Item(name='NZXT H500 - Compact ATX PC Gaming Case - Tempered Glass - Enhanced Cable Management - Water-Cooling Ready - White/Black', description='''
•PREMIUM QUALITY: All-steel construction with the sleek H Series design; available in four color combinations
•FULL TEMPERED GLASS PANEL: Showcase your build with crisp clarity
•ALL-NEW CABLE MANAGEMENT SYSTEM: Features dual-position cable management bar and cable routing kit located behind motherboard tray. Velcro straps allow you to make changes on the fly
•WATER-COOLING READY: Installation simplified for both AIO and custom loop configurations
•INCLUDED: Two Aer F120mm fans for optimal airflow; Speed: 1200 + 200 RPM
•MOTHERBOARD SUPPORT: Mini-ITX, Micro-ATX, and ATX''', price="75.99", category="Cases", image="images/Case2.jpg")
        item.save()
        item = Item(name='CORSAIR Crystal 570X RGB Mid-Tower Case, 3 RGB Fans, Tempered Glass - Black', description='''
•Four tempered glass panels on the front, top, and sides of the case / Three included SP120 RGB LED fans and integrated RGB controller
•Room for up to six case fans, and compatible with 360mm, 280mm, 240mm, and 120mm radiators / Removable fan trays in the front and top of the chassis
•Cable routing channels with included velcro cable straps for clean cable management / Easy-access high-speed USB 3.0 front panel
•Bright white LED backlit CORSAIR logo on front panel and PSU cover (removable); Case Material :Steel''', price="159.98", category="Cases", image="images/Case3.jpg")
        item.save()
        item = Item(name='Cooler Master MasterCase H500 ATX Mid-Tower, tempered glass panel, two 200mm RGB fans with Controller and Case Handle for Transport', description='''
•Included: 1 mesh and 1 transparent front panel and 2 RGB- 200mm fans
•Radiator support: up to 360mm radiator support in front and 240mm in top also includes Native support for cooler master’s 200mm radiator.
•Included: light grey tinted temper glass and top magnetic filter on the top panel
•Included: front cable covers and power supply cover for clean Look
•Case handle for Easy handling and moving''', price="104.99", category="Cases", image="images/Case4.jpg")
        item.save()
        item = Item(name='Corsair CC-9011101-WWCORSAIR Crystal 460X RGB Compact Mid-Tower Case, 3 RGB Fans, Tempered Glass - Black', description='''
•Beautiful two-panel tempered glass displays every component of your build / included SP120 RGB fans for excellent performance and vivid illumination
•Clean, modern lines with an all steel exterior / compact Mid tower design fits full sized ATX boards and multiple Graphics card configurations
•Direct Air flow access to the hottest components with No Drive cages in the way / capable liquid cooling support for both CPU and GPU loops
•Full dust filtration on bottom, front, and top / tons of cable-routing options and tie downs so cables can be easily tucked out of the way. Maximum GPU Length: 14.5 inches,Maximum PSU Length: 7.87 inches ,Maximum CPU Cooler Height: 6.7 inches
•Radiator Compatibility : 120mm; 240mm; 360mm , Compatible Corsair Liquid Coolers : H55, H60, H75, H80i, H90, H100i, H105, H110''', price="119.99", category="Cases", image="images/Case5.jpg")
        item.save()
        item = Item(name='CORSAIR Graphite 780T Full-Tower Case- Black', description='''
•Rounded corners and a sleek, cohesive design for great-looking systems
•Latched side panels for easy access
•Supports dual 360mm radiators for state-of-the-art cooling installations. Compatibility:Mini-ITX, MicroATX, ATX, E-ATX, XL-ATX
•Front panel three-mode fan controller lets you tailor performance and fan noise
•Dual 140mm LED intake fans and a 140mm exhaust fan for ample airflow
•Six Modular hard drive cages and three space-saving side-mounted SSD bays for smart storage''', price="214.55", category="Cases", image="images/Case6.jpg")
        item.save()
        
        #PSUs
        item = Item(name='EVGA 750 GQ, 80+ Gold 750W, Semi Modular, ECO Mode, 5 Year Warranty, Power Supply 210-GQ-0750-V1', description='''
•EVGA 750 GQ - "Great Quality, Great Value", Active Clamp +DC to DC design for efficient operation
•80 PLUS Gold certified, with 90% (115VAC) / 92% (220VAC~240VAC) efficiency or higher under typical loads
•Fan Size / Bearing: 135mm Fluid Dynamic Bearing, Modular Design to reduce clutter and improve airflow
•Heavy-duty protections, including OVP, UVP, OCP, OPP, SCP, and OTP
•5 Year Warranty''', price="109.99", category="PSU", image="images/PSU1.jpg")
        item.save()
        item = Item(name='EVGA 500 W1, 80+ WHITE 500W, 3 Year Warranty, Power Supply 100-W1-0500-KR, Black', description='''
•3 Year Warranty. For a LIMITED TIME, +2 extra years with registration. (Valid from 6/5/2018 - 12/31/2018)
•EVGA 500W – “Unbeatable Value”. Operating Temperature is 0 degree to 40 degree Celsius
•80 PLUS White certified, with 80% efficiency or higher under typical loads
•Heavy-duty protections, including OVP (Over Voltage Protection); UVP (Under Voltage Protection, OCP (Over Current Protection), OPP (Over Power Protection), and SCP (Short Circuit Protection)''', price="42.95", category="PSU", image="images/PSU2.jpg")
        item.save()
        item = Item(name='Corsair CX Series 750 Watt 80 Plus Bronze Certified Modular Power Supply (CP-9020061-NA)', description='''
•Builder Series cx, 750 Watt, modular power supply, NA version
•Design that delivers high availability, scalability, and for maximum flexibility and price/performance
•Made in China
•Modular cabling system lets you use only the cables you need
•Built and tested to strict standards for trouble-free installation and smooth operation
•80 PLUS Bronze certified efficiency for low noise and lower power bills
•Up to 85% energy efficiency means less heat generation and lower energy bills.''', price="79.99", category="PSU", image="images/PSU3.jpg")
        item.save()
        item = Item(name='Thermaltake Smart 500W 80+ White Certified PSU, Continuous Power with 120mm cooling fan, ATX 12V V2.3/EPS 12V Active PFC Power Supply PS-SPD-0500NPCWUS-W', description='''
•Delivers 500W Continuous output @ +40℃. Compliance with Intel ATX 12V 2.31 & EPS 12V 2.92 standards
•80 PLUS Certified – 80% efficiency under typical load
•Supports (2) PCI-E 6+2pin Connectors. Active (PFC) Power Factor Correction, MTBF: 100,000 hours
•Industry Grade Protections: (OPP) Over Power Protection, (OVP) Over Voltage Protection, (SCP) Short Circuit Protection
•High-Quality Components
•Equipped with a powerful +12V rail, superior performance under all types of system loading
•5 Year Warranty''', price="55.99", category="PSU", image="images/PSU4.jpg")
        item.save()
        item = Item(name='EVGA 750 N1, 750W, 2 Year Warranty, Power Supply 100-N1-0750-L1', description='''
•EVGA 750W N1 Series
•Fan Size/ Bearing: 120mm Sleeve bearing - quiet and intelligent auto fan for near-silent operation
•Heavy-duty protections, including OVP, UVP, OCP, OPP, and SCP
•2 year Warranty & EVGA 24/7 technical support
•Operating Temperature: 0° to 25° C''', price="64.99", category="PSU", image="images/PSU5.jpg")
        item.save()
        item = Item(name='CORSAIR RMx Series, RM1000x, 1000 Watt, 80+ Gold Certified, Fully Modular Power Supply', description='''
•80 PLUS Gold certified: High efficiency operation for less excess heat and lower operating costs
•100% All Japanese 105 capacitors: Premium internal components ensure solid power delivery and long term reliability
•Zero RPM Fan Mode: Virtually silent operation at low and medium loads. 6th generation Intel Core processor Ready (Intel Skylake and Z170 motherboards)ATX12V v2.4 and EPS 2.92 standards and is backward compatible with ATX12V 2.2, 2.31 and ATX12V 2.01 systems
•Fully Modular: Make your builds and upgrades easy, with clean, great-looking results
•Ten year warranty: Your guarantee of reliable operation that will last across several system builds''', price="179.99", category="PSU", image="images/PSU6.jpg")
        item.save()
        item = Item(name='EVGA 750 BQ, 80+ Bronze 750W, Semi Modular, 5 Year Warranty, Includes Free Power On Self Tester, Power Supply 110-BQ-0750-V1', description='''
•EVGA 750 BQ - "Great Quality, Great Value"
•80 PLUS Bronze certified, with 85% efficiency or higher under typical loads
•Fan Size / Bearing: 140mm Teflon Nano-Steel Bearing - Quiet and Intelligent Auto Fan for near-silent operation
•Heavy-duty protections, including OVP, UVP, OCP, OPP, and SCP
•5 Year Warranty''', price="84.99", category="PSU", image="images/PSU7.jpg")
        item.save()
        
        #Storage
        item = Item(name='Samsung 860 EVO 500GB 2.5 Inch SATA III Internal SSD (MZ-76E500B/AM)', description='''
•Powered by Samsung V-NAND Technology. Optimized Performance for Everyday Computing
•Enhanced Performance: Sequential Read/Write speeds up to 550MB/s and 520MB/s respectively
•Ideal for mainstream PCs and laptops for personal, gaming and business use
•Hardware/Software Compatibility: Windows 8/Windows 7/Windows Server 2003 (32-bit and 64-bit), Vista (SP1 and above), XP (SP2 and above), MAC OSX, and Linux
•Included Contents: 2.5" (7mm) SATA III (6Gb/s) SSD & User Manual (All Other Cables, Screws, Brackets Not Included). 5-Year Warranty''', price="109.99", category="Storage", image="images/Storage1.jpg")
        item.save()
        item = Item(name='Crucial MX500 500GB 3D NAND SATA 2.5 Inch Internal SSD - CT500MX500SSD1(Z)', description='''
•Sequential reads/writes up to 560/510 MB/s and random reads/writes up to 95k/90k on all file types
•Accelerated by Micron 3D NAND technology
•Integrated Power Loss Immunity preserves all your saved work if the power unexpectedly gets cut
•Crucial 5-year limited warranty
•Product ships in Amazon Certified Frustration Free Packaging (may differ from retail packaging depicted in product collateral)''', price="69.95", category="Storage", image="images/Storage2.jpg")
        item.save()
        item = Item(name='WD Blue 3D NAND 500GB PC SSD - SATA III 6 Gb/s, 2.5"/7mm - WDS500G2B0A', description='''
•3D NAND SATA SSD for capacities up to 2TB* with enhanced reliability. |*As used for storage capacity, one terabyte (TB) = one trillion bytes. Total accessible capacity varies depending on operating environment
•Sequential read speeds up to 560MB/s and sequential write speeds up to 530MB/s.** |**As used for transfer rate or interface, megabyte per second (MB/s) = one million bytes per second and gigabit per second (Gb/s) = one billion bits per second
•An industry-leading 1.75M hours mean time to failure (MTTF) and up to 500 terabytes written (TBW) for enhanced reliability. | MTTF = Mean Time To Failure based on internal testing using Telcordia stress part testing. TBW (terabytes written) values calculated using JEDEC client workload (JESD219) and vary by product capacity
•WD F.I.T. Lab certification for compatibility with a wide range of computers
•5-year manufacturer's limited warranty
•Free downloadable software to monitor the status of your drive and clone a drive, or backup your data
•An active power draw up to 25% lower than previous generations of WD Blue SSD''', price="72.99", category="Storage", image="images/Storage3.jpg")
        item.save()
        item = Item(name='SanDisk SSD PLUS 480GB Internal SSD - SATA III 6 Gb/s, 2.5"/7mm - SDSSDA-480G-G26', description='''
•Easy upgrade for faster boot-up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive. Based on published specifications and internal benchmarking tests using PCMark Vantage scores.)
•Boosts burst write performance, making it ideal for typical PC workloads
•The perfect balance of performance and reliability
•Read/write speeds of up to 535MB/s/445MB/s (Based on internal testing; performance may vary depending upon drive capacity, host device, OS and application.)
•Shock-resistant for proven durability —even if you drop your computer (Shock resistant (up to 1500G) and vibration resistant (5gRMS, 10-2000 HZ/4.9 gRMS, 7-800 HZ), Temperature (from 0 degrees Celcius to 70 degrees Celcius))
•3-year limited manufacturer warranty''', price="199.99", category="Storage", image="images/Storage4.jpg")
        item.save()
        item = Item(name='WD Blue 1TB PC Hard Drive - 7200 RPM Class, SATA 6 Gb/s, 64 MB Cache, 3.5" - WD10EZEX', description='''
•Reliable everyday computing
•WD quality and reliability
•Free Acronis True Image WD Edition cloning software
•Massive capacities up to 6 TB available
•2-year manufacturer's limited warranty''', price="109.99", category="Storage", image="images/Storage5.jpg")
        item.save()
        item = Item(name='Seagate BarraCuda Internal Hard Drive 2TB SATA 6Gb/s 64MB Cache 3.5-Inch (ST2000DM006)', description='''
•Cost-effective 7200 RPM internal hard drive upgrade for laptop or desktop computers allows you to store all of your games, music, movies, and more
•Seagate BarraCuda’s SATA 6Gb/s interface optimizes burst performance while Seagate Secure models offer hardware-based data security
•Best-fit applications for BarraCuda hard drives include desktop or all-in-one PCs, home servers, entry-level direct-attached storage devices (DAS)
•2 year limited manufacturer warranty''', price="59.99", category="Storage", image="images/Storage6.jpg")
        item.save()
        item = Item(name='WD Black 2TB Performance Desktop Hard Disk Drive - 7200 RPM SATA 6 Gb/s 64MB Cache 3.5 Inch - WD2003FZEX', description='''
•Next-generation desktop performance hard drive designed to intensify your PC experience
•Performance storage available in up to 6TB capacities
•2X DRAM cache up to 256 MB for faster read operations
•Designed for creative professionals, gamers and system builders
•5-year manufacturer's limited warranty''', price="114.96", category="Storage", image="images/Storage7.jpg")
        item.save()
        
        #Memory
        item = Item(name='Corsair Vengeance LPX 16GB (2x8GB) DDR4 DRAM 3000MHz C15 Desktop Memory Kit - Black (CMK16GX4M2B3000C15)', description='''
•Designed for high-performance overclocking
•Designed for great looks; SPD Speed: 2133MHz
•Performance and Compatibility
•Low-profile heat spreader design
•Compatibility: Intel 100 Series,Intel 200 Series,Intel 300 Series,Intel X299''', price="189.99", category="Memory", image="images/Memory1.jpg")
        item.save()
        item = Item(name='CORSAIR Vengeance RGB PRO 16GB (2x8GB) DDR4 3200MHz C16 LED Desktop Memory - Black', description='''
•Dynamic Multi-Zone RGB Lighting
•Next Generation Software
•Custom Performance PCB
•Tightly Screened Memory. Maximum Bandwidth and Tight Response Times
•Compatibility: Intel 100 Series, Intel 200 Series, Intel 300 Series, Intel X299, AMD 300 Series, AMD 400 Series''', price="139.99", category="Memory", image="images/Memory2.jpg")
        item.save()
        item = Item(name='G.SKILL TridentZ RGB Series 16GB (2 x 8GB) 288-Pin DDR4 3000MHz (PC4 24000) Desktop Memory Model F4-3000C16D-16GTZR', description='''
•DDR4 3000 (PC4 24000)
•Timing 16-18-18-38
•Cas Latency 16
•Voltage 1.35V''', price="119.95", category="Memory", image="images/Memory3.jpg")
        item.save()
        item = Item(name='Corsair Vengeance LPX 16GB (2x8GB) DDR4 DRAM 3200MHz C16 Desktop Memory Kit - Black (CMK16GX4M2B3200C16)', description='''
•Vengeance LPX memory is designed for high-performance overclocking. The heatspreader is made of pure aluminum for faster heat dissipation, and the eight-layer PCB helps manage heat and provides superior overclocking headroom
•Compatible with Intel 100 Series,Intel 200 Series,Intel 300 Series,Intel X299,AMD 300 Series, AMD 400 Series
•Compatibility tested across 100 Series motherboards for reliably fast performance
•XMP 2.0 support for trouble-free, automatic overclocking
•SPD Speed:2133MHz''', price="119.59", category="Memory", image="images/Memory4.jpg")
        item.save()
        item = Item(name='Ballistix Sport LT 16GB Kit (8GBx2) DDR4 3000 MT/s (PC4-24000) CL16 SR x8 DIMM 288-Pin Memory - BLS2K8G4D30BESBK (Gray)', description='''
•Speeds up to 3200 MT/s
•Faster speeds and responsiveness than standard DDR4 memory
•Ideal for gamers and performance enthusiasts
•Intel XMP 2.0 profiles for easy configuration
•Unbuffered / 8GB based / Single Rank module''', price="92.99", category="Memory", image="images/Memory5.jpg")
        item.save()
        item = Item(name='XPG Z1 DDR4 2400MHz (PC4 19200) 16GB (2x8GB) Gaming Memory Modules, Silver (AX4U240038G16-DSZ1)', description='''
•PC4-19200 CL16-16-16 1.2V
•Consume less power than DDR3
•Overclock compatible
•2 oz copper for better cooling
•Ideal for PC upgrades''', price="139.99", category="Memory", image="images/Memory6.jpg")
        item.save()
        
        #Accessories
        item = Item(name='Razer Naga Trinity: True 16,000 5G Optical Sensor - 3 Interchangeable Side Plates - Chroma Enable - Gaming Mouse', description='''
•Incredibly Accurate-16, 000 DPI 5G Optical sensor
•More Customization-3 interchangeable side plates with 2, 7 and 12-button configurations
•More Commands-Up to 19 fully programmable buttons
•Designed to Win-Enhanced right-handed form factor
•Powered by Razer Chroma. Up to 450 inches per second (IPS) / 50 G acceleration''', price="99.99", category="Accessories", image="images/Accessories1.jpg")
        item.save()
        item = Item(name='CORSAIR Scimitar Pro RGB - MMO Gaming Mouse - 16,000 DPI Optical Sensor - 12 Programmable Side Buttons - Yellow', description='''
•Exclusive key Slider macro button control system. Compatibility - A PC with a USB port , Windows 10, Windows 8 or Windows 7 , An internet connection is required to download the Corsair Utility Engine software
•12 optimized mechanical side buttons designed to Pro player specifications for consistent tactile feedback and precise actuation. Textured side button keycaps provide enhanced grip and feel
•The patent pending design provides 8mm of key travel with secure lock to ensure every button is within reach. Surface calibration tuning Utility: optimizes sensor precision and responsiveness for your playing surface
•Onboard storage with hardware macro playback: three predefined profiles include actions common for MMO gaming as well as General purpose keyboard shortcuts
•Custom, gaming Grade 16000 DPI Optical sensor: ultra-accurate and high-speed tracking Engine. Cable: 1.8 meter''', price="79.99", category="Accessories", image="images/Accessories2.jpg")
        item.save()
        item = Item(name='Logitech G910 Orion Spark RGB Mechanical Gaming Keyboard – 9 Programmable Buttons, Dedicated Media Controls', description='''
•World's fastest RGB mechanical gaming keyboard: Exclusive Romer-G Mechanical Switches with up to 25 percent faster actuation
•Customizable RGB illumination: Personalize individual key lighting from a palette of 16 million colors ; Cable Length (Power/Charging): 6 ft (1.8 m)
•Arx Control App and smartphone dock: Instantly access in-game data on your smartphone or tablet without interrupting the game
•9 programmable G-keys: Create custom game macros to execute complex commands with lightning speed and accuracy
•Dedicated media controls: One-touch control panel for quick access to play, pause, mute, volume and skip''', price="179.99", category="Accessories", image="images/Accessories3.jpg")
        item.save()
        item = Item(name='Logitech G430 7.1 DTS Headphone: X and Dolby Surround Sound Gaming Headset for PC, Playstation 4 – On-Cable Controls – Sports-Performance Ear Pads – Rotating Ear Cups – Light Weight Design', description='''
•DTS Headphone: X and Dolby 7. 1 surround Sound: experience an immersive 360-degree sound field that lets you hear what you can't see
•Built for comfort: lightweight design and soft sport cloth ear cups with 90-degree swivel for maximum comfort and a personalized fit
•Folding, noise-cancelling boom mic: reduces background noise for clear voice pick up and rotates up and out of the way
•Impedance: 32 ohms. On-cable sound controls: volume dial and mute switch are close at hand for quick Audio adjustments
•Compatibility: Works with PS4 and Windows 10, Windows 8, Windows 7 or windows Vista computers. Sensitivity: 90dB SPL/mw.Cable Length: 10.5 ft
•Headphone- frequency response: 20Hz-20KHz. Microphone pickup pattern: cardioid (unidirectional)-frequency response: 50-20khz. Please note: kindly refer the user guide before use''', price="79.99", category="Accessories", image="images/Accessories4.jpg")
        item.save()
        item = Item(name='ARCTIC MX-4 - Thermal Compound Paste For Coolers | Heat Sink Paste | Composed of Carbon Micro-particles | Easy to Apply | High Durability - 4 Grams', description='''
•It guarantees that heat generated from the CPU or GPU is dissipated efficiently.
•In contrast to metal and silicon thermal compound, the MX-4 does not compromise over time.
•With an ideal consistency, the MX-4 is very easy to use, even for beginners.
•Formula, the MX-4 guarantees exceptional heat dissipation from the components and supports the stability needed to push your system to its limit.
•Composed of carbon micro-particles which lead to an extremely high thermal conductivity.''', price="9.99", category="Accessories", image="images/Accessories5.jpg")
        item.save()
        item = Item(name='Arctic Silver 5 Thermal Compound (Pack of 2)', description='''
•Premium silver polysynthetic thermal compound
•Use between CPU's and heatsinks or water-cooling solutions
•Will not separate, run, migrate, or bleed
•Does not contain any silicone
•3.5 gram tube will cover 20 to 30 small cpu's''', price="8.93", category="Accessories", image="images/Accessories6.jpg")
        item.save()
        
        
