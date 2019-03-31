from django.core.management.base import BaseCommand, CommandError
from products.models import Item

class Command(BaseCommand):
    help = "Adds test items to database"

    def handle(self, *args, **options):
        #motherboards
        item = Item(name='GIGABYTE Z390 AORUS XTREME LGA 1151 (300 Series) Intel Z390 HDMI THUNDERBOLT 3 USB 3.1 Extended ATX Intel Motherboard', description='''Supports Intel 8th & 9th Gen Core i9/i7/i5/i3, Celeron, and Pentium Processors
Dual Channel Non-ECC Unbuffered DDR4, 4 DIMMs
Intel Optane Memory Ready
16 Phases IR Digital VRM Solution with PowIRstage
Thermal Design with Fins-Array Heatsink, Direct Touch Heatpipe, NanoCarbon Baseplate
Onboard Intel CNVI 802.11 ac 2x2 Wave 2 Wi-Fi with All new AORUS Antenna
AMP-UP Audio with High-End ESS SABRE 9018K2M DAC
AQUANTIA 10GbE BASE-T LAN and Intel Gigabit LAN with cFosSpeed
Intel Thunderbolt 3 onboard
Exclusive RGB FAN COMMANDER and OC Touch
USB TurboCharger for mobile device fast charge support
RGB FUSION with Multi-Zone Addressable LED Light Show design
Smart Fan 5 features Multiple Temperature Sensors
Front USB 3.1 Gen 2 Type-C Header
Triple Ultra-Fast M.2 with Triple Thermal Guards''', price="549.99", category="Motherboard", image="images/Motherboard1.jpg")
        item.save()
        item = Item(name='ASUS ROG Dominus Extreme Intel LGA 3647 for Xeon W-3175X (C621) 12 DIMM DDR4 DIMM.2 U.2 EEB Performance Motherboard with Aquantia 10G LAN, USB 3.1', description='''LGA 3647 socket, engineered to overclock Intel Xeon W-3175X processors
Designed for extreme performance, dual 24-pin, quad 8-pin and dual 6-pin 12V power connectors that deliver industry-leading power efficiency
Quad strength graphic power featuring 4-Way PCIe 3.0 link supporting NVIDIA GeForce SLI, NVIDIA NVLink and AMD CrossFireX
Built for high performance networking: Onboard Aquantia AQC-107 10G LAN, Intel I219-LM Gigabit LAN, Intel Wireless AC-9260 Wi-Fi (802.11 ac) and ROG GameFirst technology
5-Way Optimization featuring Auto-Tuning and FanXpert 4 provides automatic overclocking profiles for maximum OC performance, plus 14 PWM fan headers to support dynamic system cooling''', price="1799.99", category='Motherboard', image="images/Motherboard2.jpg")
        item.save()
        item = Item(name='MSI MEG Z390 ACE LGA 1151 (300 Series) Intel Z390 SATA 6Gb/s USB 3.1 ATX Intel Motherboard', description='''Intel Z390
Supports 9th/8th Gen Intel Core / Pentium Gold / Celeron processors for LGA 1151 socket
* Not backward compatible with older generation of LGA 1151 CPUs
DDR4 4500(OC)/ 4400(OC)/ 4300(OC)/ 4266(OC)/ 4200(OC)/ 4133(OC)/ 4000(OC)/ 3866(OC)/ 3733(OC)/ 3600(OC)/ 3466(OC)/ 3400(OC)/ 3333(OC)/ 3300(OC)/ 3200(OC)/ 3000(OC)/ 2800(OC)/ 2666/ 2400/ 2133''', price="289.99", category='Motherboard', image="images/Motherboard3.jpg")
        item.save()
        item = Item(name='ASRock Z390 Phantom Gaming 9 LGA 1151 (300 Series) Intel Z390 HDMI SATA 6Gb/s USB 3.1 ATX Intel Motherboard', description='''Intel Z390
Supports 9th and 8th Gen Intel Core processors (Socket 1151)
* Not backward compatible with older generation of LGA 1151 CPUs
On board LAN support 10/100/1000/2500Mbps + Dual 10/100/1000Mbps
DDR4 4200+(OC)*/ 4133(OC)/ 4000(OC)/ 3866(OC)/ 3800(OC)/ 3733(OC)/ 3600(OC)/ 3200(OC)/ 2933(OC)/ 2800(OC)/ 2666/ 2400/ 2133
* Please refer to Memory Support List on ASRock's website for more information. (http://www.asrock.com/)''', price="268.99", category='Motherboard', image="images/Motherboard4.jpg")
        item.save()
        item = Item(name='EVGA 123-CS-E397-KR LGA 1151 (300 Series) Intel Z390 SATA 6Gb/s ATX Intel Motherboard', description='''Intel Z390
Supports 8th/9th Generation Intel Processsor Family for LGA1151 socket
* Not backward compatible with older generation of LGA 1151 CPUs
DDR4 4133 +''', price="229.99", category='Motherboard', image="images/Motherboard5.jpg")
        item.save()
        item = Item(name='EVGA X299 FTW K, 142-SX-E297-KR, LGA 2066, Intel X299, SATA 6Gb/s, USB 3.1, USB 3.0, EATX, Intel Motherboard', description='''Intel X299 Chipset - supports Intel Core X-Series 7th Generation Processor Family for 2066 socket.
EATX Form Factor. Supports up to 3-Way SLI.
8 DIMM Quad-Channel DDR4 up to 128GB 4000MHz+ Skylake-X, and 64GB 4133MHz+ Kaby Lake-X. 2 x USB 3.1 (Type-A/Type-C), 8 x USB 3.0, and 4 x USB 2.0.
8 SATA III 6Gb/s ports, 2 x M.2 Key-M - 1 x 110mm, 1 x 80mm (up to 32Gbps), 1 x M.2 Key-E 32mm, Intel Optane Memory Ready. 2 x U.2 Ports.
Killer E2500 + Intel i219v Gigabit NIC. Highly-Efficient 14 Phase Digital VRM. RGB LED I/O cover, PCH Heatsink, and fan header support.''', price="349.00", category='Motherboard', image="images/Motherboard6.jpg")
        item.save()
