import os
import re

destinations = {
    "china.html": {
        "country": "China",
        "network_title": "Local Networks in China",
        "network_desc": "Your eSIM will connect to local networks to provide data. The best providers partner with top-tier carriers for nationwide 5G coverage, overcoming local restrictions.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>China Mobile</strong> and <strong>China Unicom</strong>. Automatically bypasses the Great Firewall so you can use Google and WhatsApp.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to <strong>China Mobile</strong> with unlimited data. Includes built-in VPN to keep your favorite apps unblocked.",
        "reasons_title": "Why Travelers Choose eSIMs in China",
        "reason_1": "<span><strong>Bypass the Great Firewall:</strong> These travel eSIMs route data externally, meaning Google, Instagram, and WhatsApp work flawlessly.</span>",
        "reason_2": "<span><strong>Instant WeChat/Alipay Access:</strong> Connect to data instantly upon landing at Beijing or Shanghai to use payment apps immediately.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Chinese data.</span>",
        "airport": "Beijing Capital or Shanghai Pudong"
    },
    "japan.html": {
        "country": "Japan",
        "network_title": "Local Networks in Japan",
        "network_desc": "When you travel to Japan, your eSIM will connect to the fastest local networks. Providers partner with top-tier Japanese carriers for 5G coverage.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>SoftBank</strong> and <strong>KDDI</strong>. Excellent for major cities, bullet trains, and rural exploration.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to <strong>NTT Docomo</strong> and <strong>KDDI</strong> with unlimited data, perfect for heavy Google Maps and translation use.",
        "reasons_title": "Why Travelers Choose eSIMs in Japan",
        "reason_1": "<span><strong>No Language Barrier at Kiosks:</strong> Avoid trying to navigate Japanese mobile stores or renting pocket WiFis at the airport.</span>",
        "reason_2": "<span><strong>Instant Translation & Maps:</strong> Connect to data instantly upon landing at Narita, Haneda, or Kansai to navigate the train system.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Japanese data.</span>",
        "airport": "Narita, Haneda, or Kansai"
    },
    "europe.html": {
        "country": "Europe",
        "network_title": "Networks Across Europe",
        "network_desc": "Your regional eSIM automatically switches to the best local network as you cross borders between 35+ European countries.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect to multiple Tier-1 carriers like <strong>Orange, Vodafone, and O2</strong>. Seamless transition as you travel via train or flight.",
        "network_2_name": "Holafly",
        "network_2_desc": "Unlimited data across 30+ countries partnering with major local telecoms like <strong>Telefonica and TIM</strong>.",
        "reasons_title": "Why Travelers Choose eSIMs in Europe",
        "reason_1": "<span><strong>Seamless Border Crossings:</strong> Travel from France to Italy to Germany without ever changing your SIM or losing connection.</span>",
        "reason_2": "<span><strong>Avoid Carrier Roaming Fees:</strong> US and Asian carriers charge $10+/day for slow European roaming. eSIMs are vastly cheaper.</span>",
        "reason_3": "<span><strong>Instant Train Navigation:</strong> Connect instantly upon landing at CDG, LHR, or FCO to figure out your Eurail or local transit route.</span>",
        "airport": "CDG, Heathrow, or Fiumicino"
    },
    "thailand.html": {
        "country": "Thailand",
        "network_title": "Local Networks in Thailand",
        "network_desc": "Your eSIM will connect to local networks to provide data. Providers partner with Thailand's top-tier carriers for nationwide 5G coverage.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>dtac</strong> and <strong>TrueMove H</strong>. Excellent for Bangkok, Chiang Mai, and remote islands.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to top networks with unlimited data, perfect for digital nomads in Chiang Mai or Koh Phangan.",
        "reasons_title": "Why Travelers Choose eSIMs in Thailand",
        "reason_1": "<span><strong>Skip the Airport Scams:</strong> Avoid the overpriced tourist SIM booths at the airport arrivals hall.</span>",
        "reason_2": "<span><strong>Instant Grab Access:</strong> Connect to data instantly upon landing at Suvarnabhumi or Phuket so you can immediately order a Grab taxi.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Thai data.</span>",
        "airport": "Suvarnabhumi or Phuket"
    },
    "turkey.html": {
        "country": "Turkey",
        "network_title": "Local Networks in Turkey",
        "network_desc": "Your eSIM connects to local Turkish networks to provide data. Providers partner with top-tier carriers for 5G coverage across the country.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>Turkcell</strong> and <strong>Türk Telekom</strong>. Excellent for Istanbul, Cappadocia, and the coast.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to top networks with unlimited data, perfect for sharing your hot air balloon photos.",
        "reasons_title": "Why Travelers Choose eSIMs in Turkey",
        "reason_1": "<span><strong>Avoid BTK Blocking:</strong> Using a travel eSIM helps avoid the strict Turkish phone registration rules (BTK) for short trips.</span>",
        "reason_2": "<span><strong>Instant Navigation:</strong> Connect to data instantly upon landing at Istanbul Airport (IST) or Sabiha Gökçen to navigate to your hotel.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Turkish data.</span>",
        "airport": "Istanbul (IST) or Sabiha Gökçen"
    },
    "italy.html": {
        "country": "Italy",
        "network_title": "Local Networks in Italy",
        "network_desc": "Your eSIM connects to local Italian networks to provide data. Providers partner with top-tier carriers for 5G coverage across the peninsula.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>TIM</strong>, <strong>Vodafone</strong>, and <strong>WindTre</strong>. Excellent for Rome, Venice, and the Amalfi Coast.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to top networks with unlimited data, perfect for remote workers and heavy social media users.",
        "reasons_title": "Why Travelers Choose eSIMs in Italy",
        "reason_1": "<span><strong>Skip the Codice Fiscale Hassle:</strong> Buying a physical SIM in Italy requires showing your passport and generating a local tax code. eSIMs bypass this entirely.</span>",
        "reason_2": "<span><strong>Instant Train Bookings:</strong> Connect to data instantly upon landing at Fiumicino or Malpensa to book your Trenitalia or Italo tickets.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Italian data.</span>",
        "airport": "Rome Fiumicino or Milan Malpensa"
    },
    "morocco.html": {
        "country": "Morocco",
        "network_title": "Local Networks in Morocco",
        "network_desc": "Your eSIM connects to local Moroccan networks. Providers partner with top-tier carriers for solid coverage in cities and the desert.",
        "network_1_name": "Saily & Airalo",
        "network_1_desc": "Connect primarily to <strong>Maroc Telecom</strong> and <strong>Orange</strong>. Excellent for Marrakech, Fes, and coastal towns.",
        "network_2_name": "Holafly",
        "network_2_desc": "Connects to top networks with unlimited data, perfect for navigating the winding Medinas without getting lost.",
        "reasons_title": "Why Travelers Choose eSIMs in Morocco",
        "reason_1": "<span><strong>Avoid Airport Hustlers:</strong> Skip the aggressive sales pitches for SIM cards at the airport arrivals area.</span>",
        "reason_2": "<span><strong>Instant Medina Navigation:</strong> Connect to data instantly upon landing at Marrakech Menara to use Google Maps in the confusing Medina.</span>",
        "reason_3": "<span><strong>Keep Your Number:</strong> Keep your home WhatsApp number active while using Moroccan data.</span>",
        "airport": "Marrakech Menara or Casablanca"
    }
}

template = """

  <!-- Device Compatibility Warning -->
  <div class="bg-red-50 border-l-4 border-red-500 p-6 rounded-2xl mb-12 flex gap-4 items-start">
    <i class="fa-solid fa-triangle-exclamation text-red-500 text-2xl mt-1"></i>
    <div>
      <h3 class="text-xl font-bold text-red-900 mb-1">Device Compatibility Warning</h3>
      <p class="text-red-800">Before you buy an eSIM for {country}, ensure your phone is <strong>unlocked</strong> and <strong>eSIM compatible</strong>. Most iPhones from XS/XR onwards and Samsung Galaxy S20 onwards support eSIMs. Locked phones from carriers will not work.</p>
    </div>
  </div>

  <div class="grid md:grid-cols-2 gap-12 mb-16">
    <!-- Local Network Coverage -->
    <div>
      <h3 class="text-3xl font-semibold mb-6">{network_title}</h3>
      <p class="text-gray-700 mb-4">{network_desc}</p>
      <ul class="space-y-4">
        <li class="flex gap-4 p-4 bg-white rounded-2xl shadow-sm border border-gray-100">
          <i class="fa-solid fa-tower-cell text-blue-600 text-xl mt-1"></i>
          <div>
            <strong class="block text-gray-900">{network_1_name}</strong>
            <span class="text-gray-600">{network_1_desc}</span>
          </div>
        </li>
        <li class="flex gap-4 p-4 bg-white rounded-2xl shadow-sm border border-gray-100">
          <i class="fa-solid fa-signal text-blue-600 text-xl mt-1"></i>
          <div>
            <strong class="block text-gray-900">{network_2_name}</strong>
            <span class="text-gray-600">{network_2_desc}</span>
          </div>
        </li>
      </ul>
    </div>

    <!-- Why Travelers Love These -->
    <div>
      <h3 class="text-3xl font-semibold mb-6">{reasons_title}</h3>
      <ul class="space-y-4">
        <li class="flex gap-3 text-gray-700"><i class="fa-solid fa-check text-green-500 mt-1"></i> {reason_1}</li>
        <li class="flex gap-3 text-gray-700"><i class="fa-solid fa-check text-green-500 mt-1"></i> {reason_2}</li>
        <li class="flex gap-3 text-gray-700"><i class="fa-solid fa-check text-green-500 mt-1"></i> {reason_3}</li>
      </ul>
    </div>
  </div>

  <!-- eSIM vs Local SIM vs Pocket WiFi -->
  <div class="bg-white rounded-3xl shadow-xl p-8 mb-16 border border-gray-100">
    <h3 class="text-3xl font-semibold mb-8 text-center">eSIM vs Local SIM vs Pocket WiFi</h3>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="text-center">
        <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-qrcode text-2xl text-blue-600"></i></div>
        <h4 class="text-xl font-bold mb-2">Travel eSIM</h4>
        <p class="text-gray-600">The best overall. Buy from home, scan a QR code, and get instant data upon arrival. No physical swapping needed.</p>
      </div>
      <div class="text-center">
        <div class="bg-gray-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-sim-card text-2xl text-gray-600"></i></div>
        <h4 class="text-xl font-bold mb-2">Physical SIM</h4>
        <p class="text-gray-600">Inconvenient. Requires finding a local store, waiting in line, and swapping your tiny home SIM card.</p>
      </div>
      <div class="text-center">
        <div class="bg-gray-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-wifi text-2xl text-gray-600"></i></div>
        <h4 class="text-xl font-bold mb-2">Pocket WiFi</h4>
        <p class="text-gray-600">Expensive and clunky. You have to carry an extra device, keep it charged, and return it before flying home.</p>
      </div>
    </div>
  </div>

  <!-- Step by Step Guide -->
  <h3 class="text-3xl font-semibold mb-8 text-center">How to Install Your {country} eSIM</h3>
  <div class="grid md:grid-cols-4 gap-6 mb-16">
    <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 text-center relative">
      <div class="absolute -top-4 -left-4 w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl border-4 border-gray-50">1</div>
      <i class="fa-solid fa-cart-shopping text-3xl text-blue-500 mb-4"></i>
      <h4 class="font-bold mb-2">Buy Before You Fly</h4>
      <p class="text-sm text-gray-600">Purchase your plan online while still at home using your Wi-Fi.</p>
    </div>
    <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 text-center relative">
      <div class="absolute -top-4 -left-4 w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl border-4 border-gray-50">2</div>
      <i class="fa-solid fa-qrcode text-3xl text-blue-500 mb-4"></i>
      <h4 class="font-bold mb-2">Scan the QR Code</h4>
      <p class="text-sm text-gray-600">Go to Settings > Cellular > Add eSIM and scan the code from your email.</p>
    </div>
    <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 text-center relative">
      <div class="absolute -top-4 -left-4 w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl border-4 border-gray-50">3</div>
      <i class="fa-solid fa-plane-arrival text-3xl text-blue-500 mb-4"></i>
      <h4 class="font-bold mb-2">Land at {airport}</h4>
      <p class="text-sm text-gray-600">Turn off your home SIM's data roaming to avoid unexpected fees.</p>
    </div>
    <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 text-center relative">
      <div class="absolute -top-4 -left-4 w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl border-4 border-gray-50">4</div>
      <i class="fa-solid fa-signal text-3xl text-blue-500 mb-4"></i>
      <h4 class="font-bold mb-2">Activate Data</h4>
      <p class="text-sm text-gray-600">Turn on your new eSIM and enable data roaming for it. You're connected!</p>
    </div>
  </div>

  <!-- FAQ Section -->
  <div class="bg-white rounded-3xl shadow-xl p-8 mb-12">
    <h3 class="text-3xl font-semibold mb-8">Frequently Asked Questions</h3>
    <div class="space-y-4">
      <details class="group border border-gray-200 rounded-2xl p-4 cursor-pointer bg-gray-50 hover:bg-gray-100 transition">
        <summary class="font-semibold text-lg flex justify-between items-center list-none">
          Can I keep my WhatsApp number?
          <span class="transition group-open:rotate-180">
            <i class="fa-solid fa-chevron-down"></i>
          </span>
        </summary>
        <p class="text-gray-600 mt-4 leading-relaxed">Yes! When you activate your eSIM, WhatsApp will ask if you want to update your number or keep the existing one. Choose to keep your existing number, and you can message and call just like you do at home.</p>
      </details>
      <details class="group border border-gray-200 rounded-2xl p-4 cursor-pointer bg-gray-50 hover:bg-gray-100 transition">
        <summary class="font-semibold text-lg flex justify-between items-center list-none">
          Can I make local {country} phone calls?
          <span class="transition group-open:rotate-180">
            <i class="fa-solid fa-chevron-down"></i>
          </span>
        </summary>
        <p class="text-gray-600 mt-4 leading-relaxed">Most travel eSIMs (like Saily, Holafly, Airalo) are <strong>data-only</strong>. This means they do not come with a local phone number. However, you can easily make calls using internet-based apps like WhatsApp, FaceTime, Skype, or Messenger.</p>
      </details>
      <details class="group border border-gray-200 rounded-2xl p-4 cursor-pointer bg-gray-50 hover:bg-gray-100 transition">
        <summary class="font-semibold text-lg flex justify-between items-center list-none">
          When exactly should I install the eSIM?
          <span class="transition group-open:rotate-180">
            <i class="fa-solid fa-chevron-down"></i>
          </span>
        </summary>
        <p class="text-gray-600 mt-4 leading-relaxed">We highly recommend installing the eSIM while you are still at home on a stable Wi-Fi connection, usually a day before your flight. Once installed, simply leave it turned off. When your plane lands in {country}, turn it on.</p>
      </details>
      <details class="group border border-gray-200 rounded-2xl p-4 cursor-pointer bg-gray-50 hover:bg-gray-100 transition">
        <summary class="font-semibold text-lg flex justify-between items-center list-none">
          Do I need to show my passport to buy an eSIM?
          <span class="transition group-open:rotate-180">
            <i class="fa-solid fa-chevron-down"></i>
          </span>
        </summary>
        <p class="text-gray-600 mt-4 leading-relaxed">No. Unlike buying a physical SIM card at a local store where you might need to show ID, buying a travel eSIM online requires no KYC (Know Your Customer) documents or passport verification.</p>
      </details>
    </div>
  </div>

</div>
"""

base_dir = "/Users/user/Documents/GitHub/esim-hub"

for filename, data in destinations.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find where the table card ends.
    # The table is in `<div class="bg-white rounded-3xl shadow-xl p-8...`
    # and ends with `</table>`.
    # Let's find `</table>`
    table_end_idx = content.find("</table>")
    if table_end_idx == -1:
        continue
    
    # We want to replace everything from the end of the table card to the footer.
    # The table card ends with a `</div>`.
    # Let's find the first `</div>` after `</table>`.
    
    # In some pages, we have <p> after table.
    # So it's better to just find `<footer id="site-footer"`
    footer_idx = content.find('<footer id="site-footer"')
    if footer_idx == -1:
        continue

    # Let's find the `</div>` that closes the table card.
    # Searching backwards from the first <div class="grid... or similar is tricky.
    # Let's use a simpler heuristic. We know the table card has `</table>\n  </div>` or `</table>\n <p>...</p>\n </div>`.
    # Let's find the `</div>` that corresponds to the `bg-white rounded-3xl...`
    # Actually, we can just cut from `</table>` to `<footer`.
    # Wait, the `max-w-6xl` wrapper starts before the table and ends before the footer.
    # Let's find `<footer` and then look backwards for `</div>` to find where to inject.
    
    # To be safe, we will just use a regex to replace everything between 
    # `</table>` and ` <footer id="site-footer"`.
    # Wait, if we do that, we need to ensure the closing `</div>` for the table card is included.
    
    # Let's extract the part before `</table>`
    part1 = content[:table_end_idx + 8] # includes </table>
    
    # Is there a <p> after table (like Pro tip)?
    # Let's check.
    part_after_table = content[table_end_idx + 8:footer_idx]
    if "Pro tip" in part_after_table:
        # Keep the pro tip and its closing div
        match = re.search(r'</p>\s*</div>', part_after_table)
        if match:
            part1 += part_after_table[:match.end()]
        else:
            # fallback
            part1 += "\n  </div>"
    else:
        # Just close the table card
        part1 += "\n  </div>"
        
    formatted_template = template.format(**data)
    
    # Construct final content
    footer_part = content[footer_idx:]
    final_content = part1 + formatted_template + "  " + footer_part
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"Updated {filename}")

