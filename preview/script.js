// ==========================================================================
// Kisah Krayon — 105 Children's Storybooks Platform
// Mobile-first architecture, 10 pages per story, 10 categories, age filtering,
// Gemini Image-to-Image prompt reference drawer on every page.
// ==========================================================================

// Global dataset loaded from window.STORIES_DATA (restricted to active stories 1-36)
const ALL_STORIES = (window.STORIES_DATA || window.__STORIES__ || []).filter(b => (b.storyNumber || 0) <= 36);

// App State
let activeStory = null;
let currentStep = 0; // 0 = Cover, 1..10 = Pages
let currentLang = 'id'; // 'id' or 'en'
let selectedCategory = 'all';
let selectedAge = 'all';
let searchKeyword = '';
let displayLimit = 12; // Mobile-friendly lazy pagination
let lastViewedStoryId = null;
let catalogScrollY = 0;
let speechRate = 0.9;
let autoAdvance = true;
let isAudioPlaying = false;
let isLargeFont = false;
let currentVoice = localStorage.getItem('app_voice') || 'id_female';
let currentAudioObj = null;

// Web Audio API Synthesizer (Page-turn chime)
let audioCtx = null;
function playChime() {
  try {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.12);
    gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.3);
  } catch (e) {}
}

// DOM Elements
const appRoot = document.getElementById('app-root');
const toastNode = document.getElementById('app-toast');

window.addEventListener('DOMContentLoaded', () => {
  initThemeSystem();
  setupRouting();
});

function showToast(msg) {
  toastNode.textContent = msg;
  toastNode.classList.add('show');
  setTimeout(() => toastNode.classList.remove('show'), 2400);
}

function loadSavedPage(book) {
  try {
    const id = (typeof book === 'object' && book) ? book.id : book;
    const legacy = (typeof book === 'object' && book) ? book.legacyId : null;
    const num = (typeof book === 'object' && book) ? book.storyNumber : null;
    return parseInt(
      localStorage.getItem(`read_p_${id}`) ||
      (legacy ? localStorage.getItem(`read_p_${legacy}`) : null) ||
      (num ? localStorage.getItem(`read_p_num_${num}`) : null) ||
      '0',
      10
    );
  } catch (e) {
    return 0;
  }
}

function savePage(book, num) {
  try {
    const id = (typeof book === 'object' && book) ? book.id : book;
    const legacy = (typeof book === 'object' && book) ? book.legacyId : null;
    const storyNum = (typeof book === 'object' && book) ? book.storyNumber : null;
    if (id) localStorage.setItem(`read_p_${id}`, num);
    if (legacy) localStorage.setItem(`read_p_${legacy}`, num);
    if (storyNum) localStorage.setItem(`read_p_num_${storyNum}`, num);
  } catch (e) {}
}

// Theme Dropdown Management
function initThemeSystem() {
  const saved = localStorage.getItem('app_theme') || 'oatmeal';
  applyTheme(saved);

  const themeBtn = document.getElementById('theme-menu-btn');
  const themeDropdown = document.getElementById('theme-dropdown');

  themeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    themeDropdown.classList.toggle('hidden');
  });

  document.addEventListener('click', () => {
    themeDropdown.classList.add('hidden');
  });

  document.querySelectorAll('.theme-opt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      applyTheme(btn.dataset.theme);
      themeDropdown.classList.add('hidden');
    });
  });
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('app_theme', theme);

  const icons = {
    oatmeal: { icon: '☀️', label: 'Kertas' },
    terracotta: { icon: '🍂', label: 'Tanah Liat' },
    celestial: { icon: '🌙', label: 'Malam' },
    pastel: { icon: '🌿', label: 'Sage' }
  };

  const current = icons[theme] || icons.oatmeal;
  document.getElementById('theme-current-icon').textContent = current.icon;
  document.getElementById('theme-current-label').textContent = current.label;

  document.querySelectorAll('.theme-opt-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.theme === theme);
  });
}

// Routing
function setupRouting() {
  window.addEventListener('hashchange', handleHash);
  handleHash();
}

function handleHash() {
  const hash = window.location.hash || '#rak';
  if (hash.startsWith('#baca/')) {
    const id = decodeURIComponent(hash.replace('#baca/', ''));
    mountReader(id);
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
  } else {
    mountCatalog(false);
  }
}

// ==========================================================================
// View: Mobile-First Catalog (105 Stories)
// ==========================================================================

function getFilteredStories() {
  return ALL_STORIES.filter(b => {
    const matchCat = (selectedCategory === 'all') || (b.category === selectedCategory);
    const matchAge = (selectedAge === 'all') || (b.ageGroup && b.ageGroup.includes(selectedAge));
    const q = searchKeyword.toLowerCase();
    const matchSearch = !searchKeyword ||
      b.title.toLowerCase().includes(q) ||
      b.englishTitle.toLowerCase().includes(q) ||
      b.synopsis.toLowerCase().includes(q) ||
      b.protagonist.toLowerCase().includes(q) ||
      (b.moralTheme && b.moralTheme.toLowerCase().includes(q));
    return matchCat && matchAge && matchSearch;
  });
}

function openStory(storyId) {
  catalogScrollY = window.scrollY || window.pageYOffset || 0;
  lastViewedStoryId = storyId;
  try {
    sessionStorage.setItem('last_viewed_story', storyId);
    sessionStorage.setItem('catalog_scroll_y', String(catalogScrollY));
  } catch (e) {}
  location.hash = `#baca/${storyId}`;
}

function renderBookCard(b) {
  const saved = loadSavedPage(b);
  let progText = "Belum Dibaca";
  if (saved >= b.pages.length) {
    progText = "Selesai ✨";
  } else if (saved > 0) {
    progText = `Hal ${saved}/${b.pages.length}`;
  }

  return `
    <article id="card-story-${b.id}" data-story-number="${b.storyNumber}" class="flex flex-col bg-[var(--bg-card)] rounded-3xl border border-[var(--border-color)] overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
      <div onclick="openStory('${b.id}')" class="relative w-full aspect-[4/3] bg-stone-200 overflow-hidden cursor-pointer group">
        <img src="${b.cover}" alt="Sampul ${b.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" onerror="this.src='images/story1.jpg'">
        <div class="absolute top-3 left-3 flex flex-wrap gap-1.5 max-w-[80%]">
          <span class="px-2.5 py-1 rounded-full text-[10px] font-extrabold bg-white/95 text-stone-900 shadow-sm backdrop-blur-sm">#${b.storyNumber}</span>
          <span class="px-2.5 py-1 rounded-full text-[10px] font-extrabold bg-white/95 text-stone-900 shadow-sm backdrop-blur-sm">${b.ageGroup}</span>
          <span class="px-2.5 py-1 rounded-full text-[10px] font-extrabold bg-white/95 text-stone-900 shadow-sm backdrop-blur-sm">${b.categoryLabel}</span>
        </div>
        <span class="absolute bottom-3 right-3 px-2.5 py-1 rounded-full text-[10px] font-extrabold bg-black/75 text-white">10 Halaman</span>
      </div>
      <div class="p-4 sm:p-5 flex flex-col flex-1 gap-2">
        <h3 onclick="openStory('${b.id}')" class="font-serif font-black text-lg text-[var(--text-main)] leading-snug cursor-pointer hover:text-clay transition-colors">${b.title}</h3>
        <p class="text-xs text-[var(--text-muted)] line-clamp-2 leading-relaxed flex-1">${b.synopsis}</p>
        <div class="text-[11px] font-bold text-amber-700 bg-amber-500/10 px-2.5 py-1 rounded-full w-fit">🐾 ${b.protagonist}</div>
        <div class="pt-3 mt-1 border-t border-dashed border-[var(--border-color)] flex items-center justify-between">
          <span class="text-xs font-bold text-[var(--text-muted)]">🔖 ${progText}</span>
          <button onclick="openStory('${b.id}')" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full text-xs font-extrabold bg-clay hover:bg-ember text-white shadow-sm transition-transform active:scale-95">
            <span>Buka Cerita</span> ➔
          </button>
        </div>
      </div>
    </article>
  `;
}

function loadMoreStories() {
  const filtered = getFilteredStories();
  const prevLimit = displayLimit;
  displayLimit += 12;
  const nextBatch = filtered.slice(prevLimit, displayLimit);
  
  const grid = document.getElementById('book-grid');
  if (grid && nextBatch.length) {
    const fragment = nextBatch.map(renderBookCard).join('');
    grid.insertAdjacentHTML('beforeend', fragment);
  }

  // Update counter
  const counter = document.getElementById('catalog-counter-text');
  if (counter) {
    counter.textContent = `Menampilkan ${Math.min(displayLimit, filtered.length)} dari ${filtered.length} cerita`;
  }

  // Update load more container
  const container = document.getElementById('load-more-container');
  if (container) {
    const remaining = filtered.length - displayLimit;
    if (remaining > 0) {
      container.innerHTML = `
        <button id="btn-load-more" class="px-8 py-3 rounded-full text-xs font-extrabold bg-[var(--bg-card)] border border-[var(--border-color)] text-[var(--text-main)] shadow-sm hover:border-clay hover:text-clay transition-all active:scale-95">
          Muat Lebih Banyak Cerita (Sisa ${remaining}) ▾
        </button>
      `;
      bindLoadMore();
    } else {
      container.innerHTML = `
        <p class="text-xs font-bold text-[var(--text-muted)] py-4">✨ Semua cerita (${filtered.length}) telah ditampilkan ✨</p>
      `;
    }
  }
}

function bindLoadMore() {
  const loadMoreBtn = document.getElementById('btn-load-more');
  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', (e) => {
      e.preventDefault();
      loadMoreStories();
    });
  }
}

function mountCatalog(resetScroll = true) {
  stopSpeech();
  activeStory = null;

  const filtered = getFilteredStories();

  // If returning to catalog from a story, auto-expand displayLimit to ensure the story is rendered
  const targetStoryId = lastViewedStoryId || (function() {
    try { return sessionStorage.getItem('last_viewed_story'); } catch(e) { return null; }
  })();

  if (targetStoryId) {
    const targetIdx = filtered.findIndex(item =>
      item.id === targetStoryId ||
      item.legacyId === targetStoryId ||
      String(item.storyNumber) === String(targetStoryId)
    );
    if (targetIdx >= 0 && targetIdx >= displayLimit) {
      displayLimit = Math.min(filtered.length, Math.ceil((targetIdx + 1) / 12) * 12);
    }
  }

  const displayedStories = filtered.slice(0, displayLimit);
  const hasMore = filtered.length > displayLimit;

  const cardsHtml = displayedStories.map(renderBookCard).join('');

  appRoot.innerHTML = `
    <!-- Hero Banner -->
    <section class="rounded-3xl bg-[var(--bg-card)] border border-[var(--border-color)] p-5 sm:p-8 mb-6 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="space-y-2 text-center sm:text-left flex-1">
        <div class="flex items-center justify-center sm:justify-start gap-2">
          <span class="px-3 py-1 rounded-full text-[10px] font-black tracking-widest text-clay bg-clay/10 uppercase">PERPUSTAKAAN DIGITAL ANAK</span>
          <span class="px-3 py-1 rounded-full text-[10px] font-black text-emerald-800 bg-emerald-500/10">${ALL_STORIES.length} BUKU LENGKAP</span>
        </div>
        <h1 class="font-serif font-black text-2xl sm:text-3xl lg:text-4xl text-[var(--text-main)] leading-tight">
          Koleksi ${ALL_STORIES.length} Dongeng Bergambar <span class="text-clay italic">Edukasi & Moral</span>
        </h1>
        <p class="text-xs sm:text-sm text-[var(--text-muted)] max-w-xl leading-relaxed">
          Koleksi terpilih kaya moral dan logika: Empati & Emosi, Pengantar Tidur, Logika & Sains, Petualangan, Dapur & Berbagi, dan Persahabatan.
        </p>
      </div>
      <div class="w-full sm:w-auto">
        <a href="#baca/barnaby-bear" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full text-sm font-extrabold bg-clay text-white shadow-md hover:bg-ember transition-all active:scale-95">
          <span>Baca Dongeng #1</span> ➔
        </a>
      </div>
    </section>

    <!-- Toolbar: Category Chips, Age Filters & Search on the Right -->
    <div class="space-y-3 mb-6">
      
      <!-- Top Row: Age Filters + Search on Right -->
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
        <!-- Age Filter Chips -->
        <div class="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-1 sm:pb-0">
          <span class="text-xs font-bold text-[var(--text-muted)] whitespace-nowrap mr-1">Usia:</span>
          <button class="age-filter-btn whitespace-nowrap px-3 py-1 rounded-full text-xs font-bold border ${selectedAge === 'all' ? 'bg-stone-800 text-white border-stone-800' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-age="all">Semua Usia</button>
          <button class="age-filter-btn whitespace-nowrap px-3 py-1 rounded-full text-xs font-bold border ${selectedAge === '2–4' ? 'bg-stone-800 text-white border-stone-800' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-age="2–4">Balita (2–4 Th)</button>
          <button class="age-filter-btn whitespace-nowrap px-3 py-1 rounded-full text-xs font-bold border ${selectedAge === '3–5' ? 'bg-stone-800 text-white border-stone-800' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-age="3–5">PAUD (3–5 Th)</button>
          <button class="age-filter-btn whitespace-nowrap px-3 py-1 rounded-full text-xs font-bold border ${selectedAge === '4–7' ? 'bg-stone-800 text-white border-stone-800' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-age="4–7">TK / SD (4–7 Th)</button>
        </div>

        <!-- Search Box (Positioned on the Right) -->
        <div class="relative w-full sm:w-72 flex-shrink-0">
          <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-xs text-[var(--text-muted)]">🔍</span>
          <input type="text" id="catalog-search-box" placeholder="Cari dari ${ALL_STORIES.length} cerita, tokoh, moral..." value="${searchKeyword}" class="w-full h-10 pl-9 pr-3 rounded-full text-xs font-medium border border-[var(--border-color)] bg-[var(--bg-card)] text-[var(--text-main)] outline-none focus:border-clay focus:ring-2 focus:ring-clay/20 transition-all">
        </div>
      </div>

      <!-- Category Filter Pills (Horizontal Scroll on Mobile) -->
      <div class="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-1">
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'all' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="all">Semua Kategori (${ALL_STORIES.length})</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'emosi' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="emosi">💛 Empati & Emosi</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'tidur' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="tidur">🦉 Pengantar Tidur</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'logika' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="logika">🧩 Logika & Sains</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'petualangan' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="petualangan">⛵ Petualangan</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'berbagi' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="berbagi">🥧 Dapur & Berbagi</button>
        <button class="cat-pill-btn whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs font-bold border ${selectedCategory === 'persahabatan' ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)]'}" data-cat="persahabatan">🤝 Persahabatan</button>
      </div>

    </div>

    <!-- Active Filter Counter -->
    <div class="flex items-center justify-between text-xs text-[var(--text-muted)] mb-4 font-semibold">
      <span id="catalog-counter-text">Menampilkan ${displayedStories.length} dari ${filtered.length} cerita</span>
    </div>

    <!-- Book Grid -->
    <div id="book-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
      ${cardsHtml.length ? cardsHtml : '<p class="col-span-full text-center py-16 text-sm text-[var(--text-muted)]">Tidak ada cerita yang cocok dengan kata kunci atau filter Anda.</p>'}
    </div>

    <!-- Load More Container -->
    <div id="load-more-container" class="text-center pt-8 pb-4">
      ${hasMore ? `
        <button id="btn-load-more" class="px-8 py-3 rounded-full text-xs font-extrabold bg-[var(--bg-card)] border border-[var(--border-color)] text-[var(--text-main)] shadow-sm hover:border-clay hover:text-clay transition-all active:scale-95">
          Muat Lebih Banyak Cerita (Sisa ${filtered.length - displayLimit}) ▾
        </button>
      ` : ''}
    </div>
  `;

  // Bind Search
  document.getElementById('catalog-search-box').addEventListener('input', (e) => {
    searchKeyword = e.target.value;
    displayLimit = 12;
    lastViewedStoryId = null;
    try { sessionStorage.removeItem('last_viewed_story'); } catch(e) {}
    mountCatalog(false);
  });

  // Bind Category Pills
  document.querySelectorAll('.cat-pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      selectedCategory = btn.dataset.cat;
      displayLimit = 12;
      lastViewedStoryId = null;
      try { sessionStorage.removeItem('last_viewed_story'); } catch(e) {}
      mountCatalog(true);
    });
  });

  // Bind Age Filters
  document.querySelectorAll('.age-filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      selectedAge = btn.dataset.age;
      displayLimit = 12;
      lastViewedStoryId = null;
      try { sessionStorage.removeItem('last_viewed_story'); } catch(e) {}
      mountCatalog(true);
    });
  });

  // Bind Load More
  bindLoadMore();

  // Handle scroll position restoration
  if (targetStoryId && !resetScroll) {
    requestAnimationFrame(() => {
      setTimeout(() => {
        const card = document.getElementById(`card-story-${targetStoryId}`);
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          card.classList.add('ring-4', 'ring-clay/50', 'ring-offset-2');
          setTimeout(() => {
            card.classList.remove('ring-4', 'ring-clay/50', 'ring-offset-2');
          }, 2200);
        } else if (catalogScrollY > 0) {
          window.scrollTo({ top: catalogScrollY, behavior: 'smooth' });
        }
      }, 60);
    });
  } else if (resetScroll) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

// ==========================================================================
// View: Mobile-First Reader (10 Pages per Story)
// ==========================================================================

function mountReader(bookId) {
  const cleanId = String(bookId || '').trim();
  const b = ALL_STORIES.find(item => 
    item.id === cleanId ||
    item.legacyId === cleanId ||
    String(item.storyNumber) === cleanId ||
    `story-${item.storyNumber}` === cleanId ||
    `story-${String(item.storyNumber).padStart(3, '0')}` === cleanId
  );
  if (!b) {
    location.hash = '#rak';
    return;
  }

  activeStory = b;
  lastViewedStoryId = b.id;
  try {
    sessionStorage.setItem('last_viewed_story', b.id);
  } catch (e) {}
  const saved = loadSavedPage(b);
  currentStep = (saved > 0 && saved <= b.pages.length) ? saved : 0;

  renderReaderScreen();
  window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
  requestAnimationFrame(() => {
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
  });
}

function renderReaderScreen() {
  if (!activeStory) return;
  const isCover = (currentStep === 0);
  const total = activeStory.pages.length;
  const page = isCover ? null : activeStory.pages[currentStep - 1];
  const progressPct = isCover ? 0 : (currentStep / total) * 100;

  if (!isCover) {
    savePage(activeStory, currentStep);
  }

  const imgSrc = isCover ? activeStory.cover : (page.image || activeStory.cover);
  const storyTitle = (currentLang === 'en' && activeStory.englishTitle) ? activeStory.englishTitle : activeStory.title;
  const titleText = isCover
    ? storyTitle
    : ((currentLang === 'en' && page.titleEn) ? page.titleEn : (currentLang === 'en' ? `Page ${currentStep}` : page.title));
  const narrative = isCover
    ? ((currentLang === 'en' && activeStory.synopsisEn) ? activeStory.synopsisEn : activeStory.synopsis)
    : (currentLang === 'en' ? page.textEn : page.textId);

  const quoteText = isCover
    ? (currentLang === 'en' ? `🐾 Characters: ${activeStory.protagonist} & ${activeStory.companion}` : `🐾 Tokoh: ${activeStory.protagonist} & ${activeStory.companion}`)
    : page.quote;

  const coReadingPrompt = isCover
    ? (currentLang === 'en' ? `💡 <strong>Reading Tips:</strong> Read gently and with warmth, encourage your child to point at the artwork and enjoy bedtime together.` : `💡 <strong>Tips Membaca:</strong> Baca dengan santai, ajak si kecil menunjuk detail gambar dan menirukan suara bersama.`)
    : page.coReading;

  // Current Page Gemini Image-to-Image Prompt
  const currentImagePrompt = isCover
    ? `Anchor Image Master Prompt (Story ${activeStory.storyNumber}):\n${activeStory.pages[0].imagePrompt}`
    : `Page ${currentStep} Prompt (Gemini Image-to-Image):\n${page.imagePrompt}`;

  // Jump beads for 10 pages
  const beadsHtml = Array.from({ length: total + 1 }, (_, i) => {
    const active = (i === currentStep);
    const label = (i === 0) ? "Sampul" : `${i}`;
    return `<button class="px-2.5 py-1 rounded-full text-[11px] font-extrabold border transition-colors ${active ? 'bg-clay text-white border-clay shadow-sm' : 'bg-[var(--bg-card)] text-[var(--text-muted)] border-[var(--border-color)] hover:border-clay'}" onclick="jumpStepTo(${i})">${label}</button>`;
  }).join('');

  appRoot.innerHTML = `
    <div class="reader-container max-w-3xl mx-auto space-y-4 ${isLargeFont ? 'large-type' : ''}">
      
      <!-- Reader Header Bar -->
      <div class="flex items-center justify-between gap-2 bg-[var(--bg-card)] border border-[var(--border-color)] px-3 py-2 rounded-2xl shadow-sm">
        <a href="#rak" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold text-[var(--text-muted)] hover:text-[var(--text-main)] hover:bg-[var(--bg-page)] transition-colors">
          <span>←</span> <span>Rak</span>
        </a>

        <div class="text-center px-2 truncate">
          <span class="block text-[10px] font-black uppercase text-amberGold tracking-wider truncate">Kisah #${activeStory.storyNumber} • ${activeStory.categoryLabel}</span>
          <h2 class="font-serif font-black text-sm sm:text-base text-[var(--text-main)] truncate">${storyTitle}</h2>
        </div>

        <div class="flex items-center gap-1.5">
          <button id="reader-lang-btn" class="w-8 h-8 rounded-full border border-[var(--border-color)] bg-[var(--bg-page)] text-xs font-black text-[var(--text-main)] flex items-center justify-center hover:border-clay transition-colors" title="Ganti Bahasa">
            ${currentLang === 'en' ? 'EN' : 'ID'}
          </button>
          <button id="reader-font-btn" class="w-8 h-8 rounded-full border border-[var(--border-color)] ${isLargeFont ? 'bg-clay text-white border-clay' : 'bg-[var(--bg-page)] text-[var(--text-main)]'} text-xs font-black flex items-center justify-center transition-colors" title="Ukuran Font">
            Aa
          </button>
        </div>
      </div>

      <!-- Top Reading Progress Bar -->
      <div class="h-1.5 w-full bg-[var(--border-color)] rounded-full overflow-hidden">
        <div class="h-full bg-gradient-to-r from-amberGold to-clay transition-all duration-300" style="width: ${progressPct}%;"></div>
      </div>

      <!-- Story Spread Slate -->
      <article class="bg-[var(--bg-card)] border border-[var(--border-color)] rounded-3xl overflow-hidden shadow-md">
        
        <!-- Artwork Canvas with Tap/Paddle Navigation -->
        <div class="gallery-art-frame frame-wide">
          <img src="${imgSrc}" alt="${titleText}" class="w-full h-full object-cover" onerror="this.src='images/story1.jpg'">
          
          <button id="reader-prev-btn" ${isCover ? 'disabled' : ''} class="absolute left-2.5 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/90 text-stone-900 border border-black/10 shadow-md flex items-center justify-center text-lg disabled:opacity-20 disabled:cursor-not-allowed hover:scale-105 active:scale-95 transition-all z-10" title="Sebelumnya">
            ◀
          </button>
          <button id="reader-next-btn" ${(currentStep === total) ? 'disabled' : ''} class="absolute right-2.5 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/90 text-stone-900 border border-black/10 shadow-md flex items-center justify-center text-lg disabled:opacity-20 disabled:cursor-not-allowed hover:scale-105 active:scale-95 transition-all z-10" title="Selanjutnya">
            ▶
          </button>

          <span class="absolute top-3 left-3 px-3 py-1 rounded-full text-[11px] font-black bg-white/95 text-stone-900 shadow-sm">
            ${isCover ? (currentLang === 'en' ? 'Book Cover' : 'Sampul Buku') : (currentLang === 'en' ? `Page ${currentStep} / ${total}` : `Hal ${currentStep} / ${total}`)}
          </span>
        </div>

        <!-- Narrative Text Block -->
        <div class="p-5 sm:p-7 text-center space-y-3">
          <h3 class="font-serif font-black text-xl sm:text-2xl text-clay">${titleText}</h3>
          <p id="story-text-body" class="text-base sm:text-lg font-medium text-[var(--text-main)] leading-relaxed max-w-xl mx-auto">${narrative}</p>
          <div class="font-hand font-bold text-base sm:text-lg text-emerald-800 bg-emerald-500/10 px-4 py-1.5 rounded-full w-fit mx-auto mt-2">
            ${quoteText}
          </div>
        </div>

      </article>

      <!-- Co-Reading Prompt Note -->
      <div class="bg-amber-500/10 border-l-4 border-amberGold rounded-r-2xl p-3.5 text-xs sm:text-sm font-semibold text-amber-900 leading-relaxed shadow-sm">
        ${coReadingPrompt}
      </div>

      <!-- Reader Controls & Audio Toolbar -->
      <div class="bg-[var(--bg-card)] border border-[var(--border-color)] rounded-2xl p-3 sm:p-4 flex flex-wrap items-center justify-between gap-3 shadow-sm">
        
        <div class="flex items-center gap-2">
          <button id="bottom-prev-btn" ${isCover ? 'disabled' : ''} class="w-8 h-8 rounded-full border border-[var(--border-color)] bg-[var(--bg-page)] text-xs font-bold flex items-center justify-center disabled:opacity-30">←</button>
          <span class="text-xs font-bold text-[var(--text-muted)]">${isCover ? (currentLang === 'en' ? 'Cover' : 'Sampul') : (currentLang === 'en' ? `Page <b>${currentStep}</b> / ${total}` : `Hal <b>${currentStep}</b> / ${total}`)}</span>
          <button id="bottom-next-btn" ${(currentStep === total) ? 'disabled' : ''} class="w-8 h-8 rounded-full border border-[var(--border-color)] bg-[var(--bg-page)] text-xs font-bold flex items-center justify-center disabled:opacity-30">→</button>
        </div>

        <!-- Audio Player Group: Play, Pause, Stop, Voice Selector -->
        <div class="flex items-center gap-1.5 flex-wrap">
          <button id="reader-play-btn" class="inline-flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-black bg-amberGold text-stone-900 shadow-sm hover:opacity-90 transition-all active:scale-95" title="Putar Suara Narasi">
            <span>▶ Putar</span>
          </button>

          <button id="reader-pause-btn" class="inline-flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-black bg-stone-200 text-stone-800 shadow-sm hover:bg-stone-300 transition-all active:scale-95" title="Jeda Suara Narasi">
            <span>⏸ Jeda</span>
          </button>

          <button id="reader-stop-btn" class="w-7 h-7 rounded-full border border-[var(--border-color)] bg-[var(--bg-page)] text-[var(--text-muted)] hover:text-red-600 text-xs font-bold flex items-center justify-center transition-all" title="Hentikan Narasi">
            <span>⏹</span>
          </button>

          <select id="reader-voice-select" class="px-2.5 py-1.5 rounded-full text-[11px] font-bold border border-[var(--border-color)] bg-[var(--bg-page)] text-[var(--text-main)] outline-none cursor-pointer" title="Pilihan Suara Gemini AI">
            <option value="id_female" ${currentVoice === 'id_female' ? 'selected' : ''}>🇮🇩 Wanita (Despina)</option>
            <option value="id_male" ${currentVoice === 'id_male' ? 'selected' : ''}>🇮🇩 Pria (Enceladus)</option>
            <option value="en_female" ${currentVoice === 'en_female' ? 'selected' : ''}>🇬🇧 Female (Despina)</option>
            <option value="en_male" ${currentVoice === 'en_male' ? 'selected' : ''}>🇬🇧 Male (Enceladus)</option>
          </select>
        </div>

        <div class="flex items-center gap-2">
          <label class="inline-flex items-center gap-1 text-[11px] font-bold text-[var(--text-muted)] cursor-pointer">
            <input type="checkbox" id="auto-flip-checkbox" ${autoAdvance ? 'checked' : ''} class="rounded text-clay">
            <span>${currentLang === 'en' ? 'Auto-flip' : 'Balik otomatis'}</span>
          </label>

          <select id="reader-speed-select" class="px-2 py-1 rounded-full text-[11px] font-bold border border-[var(--border-color)] bg-[var(--bg-page)] text-[var(--text-main)] outline-none">
            <option value="0.75" ${speechRate === 0.75 ? 'selected' : ''}>0.75x</option>
            <option value="0.9" ${speechRate === 0.9 ? 'selected' : ''}>0.9x</option>
            <option value="1.0" ${speechRate === 1.0 ? 'selected' : ''}>1.0x</option>
          </select>
        </div>

      </div>

      ${currentLang === 'en' ? `
      <div class="text-[11px] text-amber-900 bg-amber-50 border border-amber-200 rounded-xl px-3.5 py-2 text-center leading-relaxed">
        ℹ️ <em>Audio bahasa Inggris belum tersedia dan akan segera ditambahkan. Kamu dapat membaca teks dalam bahasa Inggris atau beralih ke bahasa Indonesia untuk mendengarkan narasi suara.</em>
      </div>
      ` : ''}

      <!-- Quick Page Jump Beads (10 Pages) -->
      <div class="flex items-center justify-center gap-1 flex-wrap pt-1">
        ${beadsHtml}
      </div>

      <!-- Collapsible Gemini Image-to-Image Prompt Drawer for Later Image Generation -->
      <details class="bg-[var(--bg-card)] border border-[var(--border-color)] rounded-2xl p-4 text-xs shadow-sm">
        <summary class="font-bold text-clay cursor-pointer flex items-center justify-between">
          <span>🎨 Prompt Gemini Image-to-Image (Halaman Ini)</span>
          <span class="text-[10px] text-[var(--text-muted)]">Klik untuk melihat / salin</span>
        </summary>
        <div class="mt-3 space-y-2">
          <div class="flex justify-between items-center">
            <span class="text-[10px] font-bold text-[var(--text-muted)] uppercase">Siap digunakan untuk generate gambar nanti</span>
            <button id="copy-page-prompt-btn" class="px-3 py-1 rounded-full text-[10px] font-extrabold bg-clay text-white hover:bg-ember">📋 Salin Prompt</button>
          </div>
          <pre id="page-prompt-text" class="p-3 bg-[var(--bg-page)] border border-[var(--border-color)] rounded-xl text-[11px] font-mono whitespace-pre-wrap leading-relaxed text-[var(--text-main)]">${currentImagePrompt}</pre>
        </div>
      </details>

    </div>
  `;

  // Attach Reader Listeners
  document.getElementById('reader-prev-btn').addEventListener('click', prevStep);
  document.getElementById('reader-next-btn').addEventListener('click', nextStep);
  document.getElementById('bottom-prev-btn').addEventListener('click', prevStep);
  document.getElementById('bottom-next-btn').addEventListener('click', nextStep);

  document.getElementById('reader-lang-btn').addEventListener('click', () => {
    currentLang = (currentLang === 'id') ? 'en' : 'id';
    renderReaderScreen();
    if (currentLang === 'en') {
      showToast('Bahasa Inggris aktif. Audio EN belum tersedia & segera hadir.');
    } else {
      showToast('Bahasa Indonesia aktif');
    }
  });

  document.getElementById('reader-font-btn').addEventListener('click', () => {
    isLargeFont = !isLargeFont;
    document.querySelector('.reader-container').classList.toggle('large-type', isLargeFont);
  });

  document.getElementById('reader-play-btn').addEventListener('click', playAudio);
  document.getElementById('reader-pause-btn').addEventListener('click', pauseAudio);
  document.getElementById('reader-stop-btn').addEventListener('click', () => stopAudio(true));

  document.getElementById('reader-voice-select').addEventListener('change', (e) => {
    currentVoice = e.target.value;
    localStorage.setItem('app_voice', currentVoice);
    // Sync language automatically
    const isEnVoice = currentVoice.startsWith('en_');
    if ((isEnVoice && currentLang !== 'en') || (!isEnVoice && currentLang !== 'id')) {
      currentLang = isEnVoice ? 'en' : 'id';
      renderReaderScreen();
    }
    if (isAudioPlaying) {
      stopAudio(false);
      playAudio();
    }
  });

  document.getElementById('auto-flip-checkbox').addEventListener('change', (e) => {
    autoAdvance = e.target.checked;
  });

  document.getElementById('reader-speed-select').addEventListener('change', (e) => {
    speechRate = parseFloat(e.target.value);
    if (currentAudioObj) {
      currentAudioObj.playbackRate = speechRate;
    } else if (isAudioPlaying) {
      startAudio();
    }
  });

  document.getElementById('copy-page-prompt-btn').addEventListener('click', () => {
    const text = document.getElementById('page-prompt-text').textContent;
    navigator.clipboard.writeText(text);
    showToast("Prompt halaman ini berhasil disalin!");
  });
}

function prevStep() {
  stopSpeech();
  if (currentStep > 0) {
    playChime();
    currentStep--;
    renderReaderScreen();
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
  }
}

function nextStep() {
  stopSpeech();
  if (currentStep < activeStory.pages.length) {
    playChime();
    currentStep++;
    renderReaderScreen();
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
  } else {
    showFinishedModal();
  }
}

function jumpStepTo(stepIndex) {
  stopSpeech();
  playChime();
  currentStep = stepIndex;
  renderReaderScreen();
  window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
}

// Finished Celebration Modal
function showFinishedModal() {
  const currentIndex = ALL_STORIES.findIndex(b => b.id === activeStory.id);
  const nextBook = ALL_STORIES[currentIndex + 1];

  const modal = document.createElement('div');
  modal.className = 'fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4';
  modal.innerHTML = `
    <div class="bg-[var(--bg-card)] border border-[var(--border-color)] rounded-3xl p-6 sm:p-8 max-w-sm w-full text-center space-y-4 shadow-2xl">
      <span class="text-5xl block animate-bounce">🎉</span>
      <h3 class="font-serif font-black text-2xl text-[var(--text-main)]">Cerita Selesai!</h3>
      <p class="text-xs sm:text-sm text-[var(--text-muted)] leading-relaxed">
        Hebat sekali! Kamu dan si kecil sudah menyelesaikan <b>${activeStory.title}</b> sampai halaman ke-${activeStory.pages.length}!
      </p>
      <div class="flex flex-col gap-2 pt-2">
        <button id="finish-replay-btn" class="w-full py-2.5 rounded-full text-xs font-black bg-clay text-white shadow-sm hover:bg-ember transition-colors">🔄 Baca Lagi</button>
        ${nextBook ? `<button id="finish-next-btn" class="w-full py-2.5 rounded-full text-xs font-black bg-amberGold text-stone-900 shadow-sm hover:opacity-90 transition-colors">📖 Lanjut: ${nextBook.title} ➔</button>` : ''}
        <button id="finish-exit-btn" class="w-full py-2.5 rounded-full text-xs font-bold border border-[var(--border-color)] bg-[var(--bg-page)] text-[var(--text-main)] hover:bg-stone-200 transition-colors">🏠 Kembali ke Rak</button>
      </div>
    </div>
  `;

  document.body.appendChild(modal);

  document.getElementById('finish-replay-btn').addEventListener('click', () => {
    modal.remove();
    currentStep = 0;
    renderReaderScreen();
  });

  if (nextBook) {
    document.getElementById('finish-next-btn').addEventListener('click', () => {
      modal.remove();
      location.hash = `#baca/${nextBook.id}`;
    });
  }

  document.getElementById('finish-exit-btn').addEventListener('click', () => {
    modal.remove();
    location.hash = '#rak';
  });
}

// Audio Narration: High-Fidelity Gemini TTS (.wav / .m4a) with Web Speech API Fallback
function playAudio() {
  if (currentAudioObj && currentAudioObj.paused) {
    // Resume existing paused audio
    currentAudioObj.play().then(() => {
      isAudioPlaying = true;
      updateAudioBtnState(true);
      showToast(currentLang === 'en' ? 'Resuming narration' : 'Melanjutkan narasi suara');
    }).catch(err => console.warn(err));
    return;
  }

  // Start fresh playback
  stopAudio(false);

  const isCover = (currentStep === 0);
  const page = isCover ? null : activeStory.pages[currentStep - 1];
  const isMale = currentVoice.endsWith('_male');
  const isEn = currentVoice.startsWith('en_');

  let audioSrc = null;
  let audioLabel = "";

  if (isEn) {
    audioSrc = `audio/story${activeStory.storyNumber}_${currentVoice}.m4a`;
    audioLabel = `English (${isMale ? 'Enceladus' : 'Despina'})`;
  } else {
    const pageNum = isCover ? 0 : (page ? page.number : 1);
    const filename = isCover ? 'page_0_cover.wav' : `page_${pageNum}.wav`;
    const labelPrefix = isCover ? 'Sampul Cerita' : `Halaman ${pageNum}`;

    if (isMale) {
      audioSrc = `audio/story${activeStory.storyNumber}/male/${filename}`;
      audioLabel = `${labelPrefix} • Pria (Enceladus)`;
    } else {
      audioSrc = `audio/story${activeStory.storyNumber}/${filename}`;
      audioLabel = `${labelPrefix} • Wanita (Despina/Aoede)`;
    }
  }

  const audio = new Audio(audioSrc);
  audio.playbackRate = speechRate;

  audio.addEventListener('canplaythrough', () => {
    currentAudioObj = audio;
    audio.play().then(() => {
      isAudioPlaying = true;
      updateAudioBtnState(true);
      showToast(`🎙️ Memutar: ${audioLabel} (Gemini TTS)`);
    }).catch(err => {
      console.warn('Audio play prevented or failed, fallback to Web Speech:', err);
      startWebSpeech();
    });
  }, { once: true });

  audio.addEventListener('error', () => {
    // Fallback to monolithic .m4a if per-page file is not yet available
    const fallbackM4a = `audio/story${activeStory.storyNumber}_${currentVoice}.m4a`;
    if (audioSrc !== fallbackM4a) {
      console.info(`Per-page audio ${audioSrc} not found. Trying fallback ${fallbackM4a}`);
      const fallbackAudio = new Audio(fallbackM4a);
      fallbackAudio.playbackRate = speechRate;
      fallbackAudio.addEventListener('canplaythrough', () => {
        currentAudioObj = fallbackAudio;
        fallbackAudio.play().then(() => {
          isAudioPlaying = true;
          updateAudioBtnState(true);
          showToast(`🎙️ Memutar: ${currentVoice.replace('_', ' ').toUpperCase()} (Gemini TTS Full)`);
        }).catch(startWebSpeech);
      }, { once: true });
      fallbackAudio.addEventListener('error', startWebSpeech, { once: true });
      return;
    }
    console.info(`Audio file ${audioSrc} not found. Falling back to browser speech synthesis.`);
    startWebSpeech();
  }, { once: true });

  audio.addEventListener('ended', () => {
    isAudioPlaying = false;
    currentAudioObj = null;
    updateAudioBtnState(false);
    if (autoAdvance && activeStory && currentStep < activeStory.pages.length) {
      nextStep();
      setTimeout(playAudio, 800);
    } else if (currentStep === activeStory.pages.length) {
      showFinishedModal();
    }
  });
}

function pauseAudio() {
  if (currentAudioObj && !currentAudioObj.paused) {
    currentAudioObj.pause();
    isAudioPlaying = false;
    updateAudioBtnState(false);
    showToast(currentLang === 'en' ? 'Audio paused' : 'Narasi suara dijeda');
  } else if ('speechSynthesis' in window && window.speechSynthesis.speaking) {
    window.speechSynthesis.pause();
    isAudioPlaying = false;
    updateAudioBtnState(false);
    showToast(currentLang === 'en' ? 'Audio paused' : 'Narasi suara dijeda');
  }
}

function stopAudio(notify = true) {
  if (currentAudioObj) {
    currentAudioObj.pause();
    currentAudioObj.currentTime = 0;
    currentAudioObj = null;
  }
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isAudioPlaying = false;
  updateAudioBtnState(false);
  if (notify) {
    showToast(currentLang === 'en' ? 'Audio stopped' : 'Narasi suara dihentikan');
  }
}

function stopSpeech() {
  stopAudio(false);
}

function startWebSpeech() {
  if (!('speechSynthesis' in window)) {
    showToast("Fitur audio tidak didukung di peramban ini.");
    return;
  }

  window.speechSynthesis.cancel();

  const isCover = (currentStep === 0);
  const page = isCover ? null : activeStory.pages[currentStep - 1];
  const speechText = isCover
    ? `${(currentLang === 'en' && activeStory.englishTitle) ? activeStory.englishTitle : activeStory.title}. ${(currentLang === 'en' && activeStory.synopsisEn) ? activeStory.synopsisEn : activeStory.synopsis}`
    : (currentLang === 'en' ? page.textEn : page.textId);

  const utterance = new SpeechSynthesisUtterance(speechText);
  utterance.rate = speechRate;
  utterance.lang = (currentLang === 'en') ? 'en-US' : 'id-ID';

  const voices = window.speechSynthesis.getVoices();
  const matched = voices.find(v => (currentLang === 'en') ? v.lang.startsWith('en') : v.lang.startsWith('id'));
  if (matched) utterance.voice = matched;

  utterance.onstart = () => {
    isAudioPlaying = true;
    updateAudioBtnState(true);
  };

  utterance.onend = () => {
    isAudioPlaying = false;
    updateAudioBtnState(false);
    if (autoAdvance && activeStory && currentStep < activeStory.pages.length) {
      nextStep();
      setTimeout(playAudio, 800);
    } else if (currentStep === activeStory.pages.length) {
      showFinishedModal();
    }
  };

  utterance.onerror = () => {
    isAudioPlaying = false;
    updateAudioBtnState(false);
  };

  window.speechSynthesis.speak(utterance);
}

function updateAudioBtnState(playing) {
  const playBtn = document.getElementById('reader-play-btn');
  if (playBtn) {
    if (playing) {
      playBtn.classList.add('ring-2', 'ring-amberGold/50', 'bg-amber-400');
      playBtn.querySelector('span').textContent = '▶ Sedang Putar';
    } else {
      playBtn.classList.remove('ring-2', 'ring-amberGold/50', 'bg-amber-400');
      playBtn.querySelector('span').textContent = (currentAudioObj && currentAudioObj.currentTime > 0) ? '▶ Lanjut' : '▶ Putar';
    }
  }
}

// Keyboard nav
document.addEventListener('keydown', (e) => {
  if (!activeStory) return;
  if (e.key === 'ArrowRight') nextStep();
  if (e.key === 'ArrowLeft') prevStep();
});
