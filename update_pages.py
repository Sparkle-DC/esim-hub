#!/usr/bin/env python3
import re

NAV = ''' <nav class="bg-white border-b sticky top-0 z-50">
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

FOOTER_SCRIPT = '''<script>
 fetch('/footer.html')
 .then(r => r.text())
 .then(html => { document.getElementById('site-footer').innerHTML = html; });
 </script>'''

FOOTER = ''' <footer id="site-footer" class="bg-gray-900 text-gray-400 py-12 text-center text-sm">
 <p>© 2026 utilwipe.com • All eSIM links are affiliate links. We may earn a commission at no extra cost to you.</p>
 <p class="mt-2">Fast, honest comparisons since 2026</p>
 </footer>'''

pages = ['index.html', 'japan.html', 'europe.html', 'turkey.html', 'usa.html',
         'thailand.html', 'china.html', 'italy.html', 'morocco.html', 'compare.html']

for page in pages:
    with open(page) as f:
        content = f.read()
    
    # 1. Replace nav: find old <nav...>...</nav> and replace with new NAV
    nav_match = re.search(r'<nav\s+class="bg-white.*?</nav>', content, re.DOTALL)
    if nav_match:
        # Also remove any old <script> right after </nav> for hamburger if present
        content = content[:nav_match.start()] + NAV + content[nav_match.end():]
        print(f"{page}: nav replaced")
    else:
        print(f"{page}: WARNING - no nav found")
    
    # 2. Replace footer: find <footer...>...</footer>
    footer_match = re.search(r'<footer[^>]*>.*?</footer>', content, re.DOTALL)
    if footer_match:
        content = content[:footer_match.start()] + FOOTER + content[footer_match.end():]
        print(f"{page}: footer replaced")
    else:
        print(f"{page}: WARNING - no footer found")
    
    with open(page, 'w') as f:
        f.write(content)
    
    # Verify
    with open(page) as f:
        c = f.read()
    checks = []
    if 'document.getElementById("menu-btn")' in c: checks.append("nav✓")
    if 'id="site-footer"' in c: checks.append("footer✓")
    if 'esim.utilwipe' in c: checks.append("logo✓")
    print(f"  -> {' '.join(checks)}")
