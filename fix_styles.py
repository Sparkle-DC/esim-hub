#!/usr/bin/env python3
import os
import re

NAV = '''<nav class="bg-white border-b sticky top-0 z-50">
 <div class="max-w-6xl mx-auto px-6 py-5 flex justify-between items-center">
 <a href="./index.html" class="flex items-center gap-2 text-3xl font-bold text-blue-600">eSIM Hub</a>
 <div class="hidden md:flex items-center gap-8 font-medium">
 <a href="./compare.html" class="hover:text-blue-600">Compare</a>
 <a href="./index.html#destinations" class="hover:text-blue-600">Travel Guides</a>
 <a href="./index.html#site-footer" class="hover:text-blue-600">About</a>
 </div>
 <div class="flex items-center gap-4">
 <a href="./index.html#search" onclick="document.getElementById('search')?.focus()"
 class="hidden md:inline-block bg-blue-600 text-white px-6 py-3 rounded-2xl font-medium hover:bg-blue-700">Find my eSIM</a>
 <button id="menu-btn" class="md:hidden text-3xl text-gray-700 focus:outline-none">
 <i class="fa-solid fa-bars"></i>
 </button>
 </div>
 </div>
 <div id="mobile-menu" class="hidden md:hidden bg-white border-t px-6 py-6 space-y-4">
 <a href="./compare.html" class="block text-lg font-medium text-gray-700 hover:text-blue-600">Compare</a>
 <a href="./index.html#destinations" class="block text-lg font-medium text-gray-700 hover:text-blue-600">Travel Guides</a>
 <a href="./index.html#site-footer" class="block text-lg font-medium text-gray-700 hover:text-blue-600">About</a>
 <a href="./index.html#search" onclick="document.getElementById('search')?.focus()"
 class="block text-center bg-blue-600 text-white px-6 py-3 rounded-2xl font-medium mt-4">Find my eSIM</a>
 </div>
 </nav>
 <script>
 document.getElementById("menu-btn")?.addEventListener("click", function() {
 document.getElementById("mobile-menu")?.classList.toggle("hidden");
 });
 </script>'''

FOOTER = '''<footer id="site-footer" class="bg-gray-900 text-gray-400 py-12 text-center text-sm mt-auto">
 <div class="max-w-6xl mx-auto px-6">
 <p>© 2026 eSIM Hub • All eSIM links are affiliate links. We may earn a commission at no extra cost to you.</p>
 <p class="mt-2">Fast, honest comparisons since 2026</p>
 </div>
 </footer>'''

TABLE_TBODY = '''<tbody class="text-lg">
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Saily</td>
 <td>20 GB</td>
 <td>30 days</td>
 <td class="font-bold">$24.99</td>
 <td>5G</td>
 <td class="text-center">⭐⭐⭐⭐⭐ 4.9</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Holafly</td>
 <td>Unlimited</td>
 <td>15 days</td>
 <td class="font-bold">$47.90</td>
 <td>5G</td>
 <td class="text-center">⭐⭐⭐⭐ 4.8</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Airalo</td>
 <td>20 GB</td>
 <td>30 days</td>
 <td class="font-bold">$26.00</td>
 <td>5G</td>
 <td class="text-center">⭐⭐⭐⭐ 4.7</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 <tr class="hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Nomad</td>
 <td>20 GB</td>
 <td>30 days</td>
 <td class="font-bold">$29.00</td>
 <td>5G</td>
 <td class="text-center">⭐⭐⭐⭐ 4.6</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 </tbody>'''

EUROPE_TABLE_TBODY = '''<tbody class="text-lg">
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Saily</td>
 <td>10 GB</td>
 <td>30 days</td>
 <td class="font-bold">$35.99</td>
 <td>35 Countries</td>
 <td class="text-center">⭐⭐⭐⭐⭐ 4.9</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Holafly</td>
 <td>Unlimited</td>
 <td>30 days</td>
 <td class="font-bold">$77.00</td>
 <td>30+ Countries</td>
 <td class="text-center">⭐⭐⭐⭐ 4.8</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 <tr class="border-b hover:bg-blue-50 transition">
 <td class="py-7 font-semibold">Airalo Eurolink</td>
 <td>20 GB</td>
 <td>30 days</td>
 <td class="font-bold">$45.00</td>
 <td>39 Countries</td>
 <td class="text-center">⭐⭐⭐⭐ 4.7</td>
 <td><a href="#" class="block bg-blue-600 text-white text-center py-4 px-10 rounded-2xl font-medium">Buy Now</a></td>
 </tr>
 </tbody>'''

TAILWIND_SCRIPT = '<script src="https://cdn.tailwindcss.com"></script>\n<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'

# Fix country pages tables
countries = ['japan.html', 'europe.html', 'thailand.html', 'usa.html', 'italy.html', 'turkey.html', 'morocco.html']
for c in countries:
    with open(c) as f:
        content = f.read()
    
    # fix table
    tbody_match = re.search(r'<tbody.*?</tbody>', content, re.DOTALL)
    if tbody_match:
        if c == 'europe.html':
            content = content[:tbody_match.start()] + EUROPE_TABLE_TBODY + content[tbody_match.end():]
        else:
            content = content[:tbody_match.start()] + TABLE_TBODY + content[tbody_match.end():]
            
    # duplicate scripts removal (some had double menu scripts)
    content = re.sub(r'(<script>\s*document\.getElementById\("menu-btn"\).*?</script>\s*){2,}', r'\1', content, flags=re.DOTALL)
    
    with open(c, 'w') as f:
        f.write(content)


def add_tailwind_and_nav_footer(file_path):
    with open(file_path) as f:
        content = f.read()
        
    # add tailwind
    if 'cdn.tailwindcss.com' not in content:
        content = content.replace('</head>', f'{TAILWIND_SCRIPT}\n</head>')
        
    # replace nav
    if '<nav class="nav">' in content:
        nav_match = re.search(r'<nav class="nav">.*?</nav>', content, re.DOTALL)
        if nav_match:
            content = content[:nav_match.start()] + NAV + content[nav_match.end():]
            
    # replace footer
    if '<footer class="footer">' in content:
        footer_match = re.search(r'<footer class="footer">.*?</footer>', content, re.DOTALL)
        if footer_match:
            content = content[:footer_match.start()] + FOOTER + content[footer_match.end():]
            
    # remove old footer if it exists to avoid duplicates
    old_footer_match = re.search(r'<footer id="site-footer".*?</footer>', content, re.DOTALL)
    if old_footer_match and '<footer class="footer">' not in locals().get('content',''):
       content = content[:old_footer_match.start()] + FOOTER + content[old_footer_match.end():]

    with open(file_path, 'w') as f:
        f.write(content)

# Update index and others
others = [
    'index.html',
    'comparisons/saily-vs-airalo.html',
    'comparisons/holafly-vs-airalo.html',
    'comparisons/saily-vs-holafly.html',
    'guides/how-to-install-esim.html',
    'guides/esim-not-working.html',
    'guides/esim-vs-roaming.html'
]
for o in others:
    if os.path.exists(o):
        add_tailwind_and_nav_footer(o)

print("Tables fixed and header/footer unified.")
