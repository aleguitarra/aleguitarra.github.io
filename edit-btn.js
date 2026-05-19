(function(){
  // Only inject on /cancion/ pages
  if (!location.pathname.match(/^\/cancion\//)) return;
  var slug = location.pathname.replace(/^\/cancion\//, '').replace(/\/$/, '');
  if (!slug) return;
  var btn = document.createElement('a');
  btn.href = '/editor/?slug=' + encodeURIComponent(slug);
  btn.title = 'Editar canción (admin)';
  btn.style.cssText = [
    'position:fixed','bottom:24px','right:24px','z-index:9999',
    'width:52px','height:52px','border-radius:50%',
    'background:#CC0000','color:#fff','display:flex',
    'align-items:center','justify-content:center',
    'box-shadow:0 4px 16px rgba(204,0,0,0.45)',
    'text-decoration:none','transition:transform .2s',
    'font-size:22px'
  ].join(';');
  btn.innerHTML = '✏️';
  btn.onmouseenter = function(){ btn.style.transform='scale(1.12)'; };
  btn.onmouseleave = function(){ btn.style.transform='scale(1)'; };
  document.body.appendChild(btn);
})();
