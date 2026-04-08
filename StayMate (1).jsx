import { useState, useEffect, useRef } from "react";

const STORAGE_KEY_USERS = "staymate-users";
const STORAGE_KEY_PROPS = "staymate-properties";
const STORAGE_KEY_INQUIRIES = "staymate-inquiries";

const SAMPLE_PROPS = [
  { id: "p1", ownerId: "owner1", ownerName: "Rajesh Kumar", ownerPhone: "+91 98765 43210", ownerEmail: "rajesh@email.com",
    title: "Spacious 2BHK in Koramangala", type: "Apartment", bedrooms: 2, bathrooms: 2, area: 1100,
    rent: 28000, deposit: 56000, city: "Bangalore", locality: "Koramangala", address: "12th Cross, Koramangala 4th Block",
    furnishing: "Semi-Furnished", available: "Immediately", gender: "Any", parking: true, pets: false, water: true,
    amenities: ["Gym","Swimming Pool","Security","Power Backup","Lift"],
    description: "Well-maintained 2BHK apartment in prime Koramangala location. East-facing, good ventilation, modular kitchen. Close to offices, restaurants and metro.",
    images: ["https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800","https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800"],
    postedOn: "2025-03-15", available_date: "Immediately", verified: true },
  { id: "p2", ownerId: "owner2", ownerName: "Priya Sharma", ownerPhone: "+91 99887 76655", ownerEmail: "priya@email.com",
    title: "Modern 1BHK near Bandra Station", type: "Apartment", bedrooms: 1, bathrooms: 1, area: 650,
    rent: 32000, deposit: 96000, city: "Mumbai", locality: "Bandra West", address: "Hill Road, Bandra West",
    furnishing: "Furnished", available: "1st April", gender: "Any", parking: false, pets: true, water: true,
    amenities: ["Security","Power Backup","Lift","Intercom"],
    description: "Fully furnished 1BHK in the heart of Bandra West. Walking distance to station, cafes, and shopping. Perfect for working professionals.",
    images: ["https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800","https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800"],
    postedOn: "2025-03-20", available_date: "1st April", verified: true },
  { id: "p3", ownerId: "owner3", ownerName: "Anil Mehta", ownerPhone: "+91 97654 32198", ownerEmail: "anil@email.com",
    title: "3BHK Independent House with Garden", type: "House", bedrooms: 3, bathrooms: 3, area: 2000,
    rent: 45000, deposit: 90000, city: "Pune", locality: "Kalyani Nagar", address: "Lane 7, Kalyani Nagar",
    furnishing: "Unfurnished", available: "Immediately", gender: "Family", parking: true, pets: true, water: true,
    amenities:["Garden","Garage","Security","Water 24x7"],
    description: "Spacious 3BHK independent house with private garden and garage. Ideal for families. Peaceful neighborhood, great connectivity.",
    images: ["https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800","https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800"],
    postedOn: "2025-03-10", available_date: "Immediately", verified: false },
];

const SAMPLE_USERS = [
  { id: "owner1", name: "Rajesh Kumar", email: "rajesh@email.com", password: "1234", role: "owner", phone: "+91 98765 43210", avatar: "RK" },
  { id: "owner2", name: "Priya Sharma", email: "priya@email.com", password: "1234", role: "owner", phone: "+91 99887 76655", avatar: "PS" },
  { id: "tenant1", name: "Arjun Singh", email: "arjun@email.com", password: "1234", role: "tenant", phone: "+91 90000 11111", avatar: "AS" },
];

function initStorage() {
  if (!localStorage.getItem(STORAGE_KEY_USERS)) localStorage.setItem(STORAGE_KEY_USERS, JSON.stringify(SAMPLE_USERS));
  if (!localStorage.getItem(STORAGE_KEY_PROPS)) localStorage.setItem(STORAGE_KEY_PROPS, JSON.stringify(SAMPLE_PROPS));
  if (!localStorage.getItem(STORAGE_KEY_INQUIRIES)) localStorage.setItem(STORAGE_KEY_INQUIRIES, JSON.stringify([]));
}
function getUsers() { return JSON.parse(localStorage.getItem(STORAGE_KEY_USERS) || "[]"); }
function getProperties() { return JSON.parse(localStorage.getItem(STORAGE_KEY_PROPS) || "[]"); }
function getInquiries() { return JSON.parse(localStorage.getItem(STORAGE_KEY_INQUIRIES) || "[]"); }
function saveUsers(u) { localStorage.setItem(STORAGE_KEY_USERS, JSON.stringify(u)); }
function saveProperties(p) { localStorage.setItem(STORAGE_KEY_PROPS, JSON.stringify(p)); }
function saveInquiries(i) { localStorage.setItem(STORAGE_KEY_INQUIRIES, JSON.stringify(i)); }

const CITIES = ["Bangalore","Mumbai","Pune","Delhi","Hyderabad","Chennai","Kolkata","Ahmedabad","Noida","Gurgaon"];
const AMENITIES_LIST = ["Gym","Swimming Pool","Security","Power Backup","Lift","Parking","Garden","Intercom","CCTV","Club House","Children Play Area","Water 24x7","Gas Pipeline","Housekeeping"];

const css = `
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
:root { --brand: #E53935; --brand-dark: #B71C1C; --brand-light: #FFEBEE; --text: #1a1a2e; --muted: #6b7280; --border: #e5e7eb; --bg: #f8f9fa; --white: #fff; --success: #10b981; --warning: #f59e0b; --radius: 12px; --shadow: 0 2px 12px rgba(0,0,0,0.08); }
.app { min-height: 100vh; background: var(--bg); }
.navbar { background: var(--white); border-bottom: 1px solid var(--border); padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; box-shadow: 0 1px 8px rgba(0,0,0,0.06); }
.logo { display: flex; align-items: center; gap: 8px; cursor: pointer; }
.logo-icon { width: 36px; height: 36px; background: var(--brand); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 16px; }
.logo-text { font-size: 20px; font-weight: 700; color: var(--text); }
.logo-text span { color: var(--brand); }
.nav-actions { display: flex; align-items: center; gap: 12px; }
.btn { padding: 8px 18px; border-radius: 8px; border: none; font-size: 14px; font-weight: 500; cursor: pointer; transition: all 0.15s; }
.btn-primary { background: var(--brand); color: white; }
.btn-primary:hover { background: var(--brand-dark); }
.btn-outline { background: transparent; border: 1.5px solid var(--brand); color: var(--brand); }
.btn-outline:hover { background: var(--brand-light); }
.btn-ghost { background: transparent; border: 1px solid var(--border); color: var(--muted); }
.btn-ghost:hover { background: var(--bg); }
.btn-sm { padding: 6px 14px; font-size: 13px; }
.btn-lg { padding: 12px 28px; font-size: 15px; }
.btn-danger { background: #fee2e2; color: #b91c1c; border: none; }
.btn-success { background: #d1fae5; color: #065f46; border: none; }
.hero { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 64px 24px; text-align: center; }
.hero h1 { font-size: 42px; font-weight: 800; margin-bottom: 12px; }
.hero h1 span { color: #ff6b6b; }
.hero p { font-size: 18px; opacity: 0.8; margin-bottom: 36px; }
.search-bar { background: white; border-radius: 16px; padding: 8px; display: flex; gap: 8px; max-width: 700px; margin: 0 auto; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
.search-bar input, .search-bar select { border: none; outline: none; padding: 10px 14px; font-size: 15px; flex: 1; border-radius: 10px; background: #f8f9fa; color: #1a1a2e; }
.search-bar .search-btn { background: var(--brand); color: white; border: none; padding: 10px 24px; border-radius: 10px; font-size: 15px; font-weight: 600; cursor: pointer; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section { padding: 40px 0; }
.section-title { font-size: 24px; font-weight: 700; color: var(--text); margin-bottom: 24px; }
.stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; max-width: 700px; margin: 32px auto 0; }
.stat-box { text-align: center; background: rgba(255,255,255,0.1); border-radius: 12px; padding: 16px; }
.stat-box .num { font-size: 28px; font-weight: 800; }
.stat-box .lbl { font-size: 13px; opacity: 0.8; margin-top: 4px; }
.filter-bar { background: white; border-radius: var(--radius); padding: 20px; margin-bottom: 24px; border: 1px solid var(--border); display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-end; }
.filter-group { display: flex; flex-direction: column; gap: 4px; }
.filter-group label { font-size: 12px; color: var(--muted); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
.filter-group select, .filter-group input { padding: 8px 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 14px; background: var(--bg); color: var(--text); min-width: 140px; }
.prop-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 24px; }
.prop-card { background: white; border-radius: var(--radius); border: 1px solid var(--border); overflow: hidden; cursor: pointer; transition: all 0.2s; box-shadow: var(--shadow); }
.prop-card:hover { transform: translateY(-4px); box-shadow: 0 8px 32px rgba(0,0,0,0.12); }
.prop-img { width: 100%; height: 200px; object-fit: cover; position: relative; }
.prop-img-wrap { position: relative; }
.prop-badge { position: absolute; top: 12px; left: 12px; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }
.badge-verified { background: #d1fae5; color: #065f46; }
.badge-new { background: #dbeafe; color: #1e40af; }
.badge-type { background: rgba(0,0,0,0.6); color: white; position: absolute; bottom: 12px; right: 12px; }
.prop-body { padding: 16px; }
.prop-title { font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
.prop-loc { font-size: 13px; color: var(--muted); margin-bottom: 12px; display: flex; align-items: center; gap: 4px; }
.prop-meta { display: flex; gap: 12px; margin-bottom: 12px; }
.prop-meta-item { display: flex; align-items: center; gap: 4px; font-size: 13px; color: var(--muted); }
.prop-footer { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 12px; }
.prop-rent { font-size: 20px; font-weight: 700; color: var(--brand); }
.prop-rent span { font-size: 12px; color: var(--muted); font-weight: 400; }
.prop-furnish { font-size: 12px; padding: 3px 8px; border-radius: 5px; font-weight: 500; }
.furnish-full { background: #fef3c7; color: #92400e; }
.furnish-semi { background: #ede9fe; color: #5b21b6; }
.furnish-un { background: #f3f4f6; color: #374151; }
.detail-page { max-width: 1100px; margin: 0 auto; padding: 32px 24px; }
.detail-grid { display: grid; grid-template-columns: 1fr 360px; gap: 32px; }
.img-gallery { border-radius: var(--radius); overflow: hidden; margin-bottom: 24px; }
.img-gallery img { width: 100%; height: 320px; object-fit: cover; }
.img-thumbs { display: flex; gap: 8px; margin-top: 8px; }
.img-thumb { width: 80px; height: 60px; object-fit: cover; border-radius: 6px; cursor: pointer; opacity: 0.7; transition: opacity 0.15s; }
.img-thumb.active, .img-thumb:hover { opacity: 1; outline: 2px solid var(--brand); }
.detail-title { font-size: 26px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
.detail-loc { font-size: 15px; color: var(--muted); margin-bottom: 20px; }
.info-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 24px 0; }
.info-box { background: var(--bg); border-radius: 10px; padding: 14px; text-align: center; }
.info-box .val { font-size: 18px; font-weight: 700; color: var(--text); }
.info-box .key { font-size: 12px; color: var(--muted); margin-top: 2px; }
.amenity-list { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0; }
.amenity-tag { background: var(--bg); border: 1px solid var(--border); border-radius: 20px; padding: 5px 14px; font-size: 13px; color: var(--text); }
.contact-card { background: white; border-radius: var(--radius); border: 1px solid var(--border); padding: 24px; position: sticky; top: 80px; box-shadow: var(--shadow); }
.owner-row { display: flex; align-items: center; gap: 14px; margin-bottom: 20px; }
.avatar { width: 48px; height: 48px; border-radius: 50%; background: var(--brand); color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 16px; flex-shrink: 0; }
.owner-name { font-size: 16px; font-weight: 600; }
.owner-tag { font-size: 12px; color: var(--success); font-weight: 500; }
.contact-btns { display: flex; flex-direction: column; gap: 10px; }
.contact-btn { width: 100%; padding: 12px; border-radius: 10px; border: none; font-size: 15px; font-weight: 600; cursor: pointer; }
.contact-btn-call { background: var(--success); color: white; }
.contact-btn-msg { background: var(--brand); color: white; }
.contact-btn-whatsapp { background: #25D366; color: white; }
.inquiry-form { margin-top: 20px; border-top: 1px solid var(--border); padding-top: 20px; }
.inquiry-form textarea { width: 100%; border: 1px solid var(--border); border-radius: 8px; padding: 10px; font-size: 14px; min-height: 90px; resize: none; color: var(--text); }
.form-container { max-width: 780px; margin: 0 auto; background: white; border-radius: var(--radius); border: 1px solid var(--border); padding: 32px; box-shadow: var(--shadow); }
.form-title { font-size: 22px; font-weight: 700; color: var(--text); margin-bottom: 28px; }
.form-group { margin-bottom: 20px; }
.form-group label { display: block; font-size: 14px; font-weight: 500; color: var(--text); margin-bottom: 6px; }
.form-group input, .form-group select, .form-group textarea { width: 100%; padding: 10px 14px; border: 1.5px solid var(--border); border-radius: 8px; font-size: 14px; color: var(--text); background: white; outline: none; transition: border 0.15s; }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { border-color: var(--brand); }
.form-group textarea { min-height: 100px; resize: vertical; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.form-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
.amenity-checks { display: flex; flex-wrap: wrap; gap: 8px; }
.amenity-check { display: flex; align-items: center; gap: 6px; padding: 6px 12px; border: 1px solid var(--border); border-radius: 20px; cursor: pointer; font-size: 13px; color: var(--text); transition: all 0.15s; }
.amenity-check.checked { background: var(--brand-light); border-color: var(--brand); color: var(--brand); font-weight: 500; }
.toggle-row { display: flex; gap: 24px; }
.toggle-item { display: flex; align-items: center; gap: 8px; cursor: pointer; font-size: 14px; color: var(--text); }
.auth-wrap { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 24px; background: var(--bg); }
.auth-card { background: white; border-radius: 20px; padding: 40px; width: 100%; max-width: 440px; border: 1px solid var(--border); box-shadow: var(--shadow); }
.auth-logo { text-align: center; margin-bottom: 28px; }
.auth-title { font-size: 22px; font-weight: 700; color: var(--text); text-align: center; margin-bottom: 6px; }
.auth-sub { font-size: 14px; color: var(--muted); text-align: center; margin-bottom: 28px; }
.role-tabs { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 24px; }
.role-tab { padding: 12px; border-radius: 10px; border: 2px solid var(--border); cursor: pointer; text-align: center; transition: all 0.15s; }
.role-tab .icon { font-size: 24px; margin-bottom: 4px; }
.role-tab .label { font-size: 14px; font-weight: 500; color: var(--muted); }
.role-tab.active { border-color: var(--brand); background: var(--brand-light); }
.role-tab.active .label { color: var(--brand); }
.tabs { display: flex; border-bottom: 2px solid var(--border); margin-bottom: 24px; }
.tab { padding: 10px 20px; font-size: 14px; font-weight: 500; cursor: pointer; color: var(--muted); border-bottom: 2px solid transparent; margin-bottom: -2px; }
.tab.active { color: var(--brand); border-bottom-color: var(--brand); }
.toast { position: fixed; bottom: 24px; right: 24px; background: #1f2937; color: white; padding: 14px 20px; border-radius: 10px; font-size: 14px; z-index: 9999; animation: slideUp 0.3s ease; }
.toast.success { background: #065f46; }
.toast.error { background: #b91c1c; }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.empty-state { text-align: center; padding: 60px 24px; }
.empty-icon { font-size: 48px; margin-bottom: 12px; }
.empty-title { font-size: 18px; font-weight: 600; color: var(--text); }
.empty-sub { font-size: 14px; color: var(--muted); margin-top: 6px; }
.owner-dash { max-width: 1100px; margin: 0 auto; padding: 32px 24px; }
.dash-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
.dash-stat { background: white; border-radius: var(--radius); border: 1px solid var(--border); padding: 20px; }
.dash-stat .ds-val { font-size: 28px; font-weight: 700; color: var(--text); }
.dash-stat .ds-lbl { font-size: 13px; color: var(--muted); margin-top: 4px; }
.dash-stat .ds-icon { font-size: 20px; margin-bottom: 8px; }
.listing-card { background: white; border-radius: var(--radius); border: 1px solid var(--border); padding: 20px; margin-bottom: 16px; display: flex; gap: 20px; }
.listing-thumb { width: 120px; height: 90px; border-radius: 8px; object-fit: cover; flex-shrink: 0; }
.listing-body { flex: 1; }
.listing-title { font-size: 16px; font-weight: 600; color: var(--text); }
.listing-meta { font-size: 13px; color: var(--muted); margin: 4px 0 10px; }
.listing-actions { display: flex; gap: 8px; }
.inquiry-item { background: white; border-radius: 10px; border: 1px solid var(--border); padding: 16px; margin-bottom: 12px; }
.inq-header { display: flex; justify-content: space-between; margin-bottom: 8px; }
.inq-name { font-size: 14px; font-weight: 600; color: var(--text); }
.inq-time { font-size: 12px; color: var(--muted); }
.inq-prop { font-size: 13px; color: var(--brand); margin-bottom: 6px; }
.inq-msg { font-size: 13px; color: var(--muted); }
.no-broker-badge { background: #fff; border: 2px solid var(--success); border-radius: 24px; padding: 4px 14px; font-size: 12px; font-weight: 700; color: var(--success); display: inline-flex; align-items: center; gap: 5px; }
.profile-menu { position: relative; }
.profile-dropdown { position: absolute; right: 0; top: 44px; background: white; border: 1px solid var(--border); border-radius: 12px; padding: 8px; min-width: 200px; box-shadow: 0 8px 32px rgba(0,0,0,0.12); z-index: 200; }
.profile-dropdown .pd-item { padding: 10px 14px; font-size: 14px; color: var(--text); cursor: pointer; border-radius: 8px; }
.profile-dropdown .pd-item:hover { background: var(--bg); }
.chip { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 500; }
.chip-blue { background: #dbeafe; color: #1e40af; }
.chip-green { background: #d1fae5; color: #065f46; }
.chip-amber { background: #fef3c7; color: #92400e; }
.back-btn { display: flex; align-items: center; gap: 6px; font-size: 14px; color: var(--muted); cursor: pointer; margin-bottom: 20px; background: none; border: none; }
.back-btn:hover { color: var(--text); }
.price-chip { background: var(--brand-light); color: var(--brand); font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 5px; }
.section-divider { border: none; border-top: 1px solid var(--border); margin: 24px 0; }
.feature-section { padding: 48px 0; background: white; border-top: 1px solid var(--border); }
.feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.feature-box { text-align: center; padding: 24px; }
.feature-icon { font-size: 36px; margin-bottom: 12px; }
.feature-title { font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 6px; }
.feature-sub { font-size: 14px; color: var(--muted); line-height: 1.6; }
.msg-box { padding: 10px 16px; border-radius: 10px; font-size: 14px; margin-bottom: 8px; }
.msg-box.success { background: #d1fae5; color: #065f46; }
.msg-box.error { background: #fee2e2; color: #b91c1c; }
`;

export default function App() {
  const [page, setPage] = useState("home");
  const [user, setUser] = useState(null);
  const [toast, setToast] = useState(null);
  const [viewProp, setViewProp] = useState(null);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [authMode, setAuthMode] = useState("login");
  const [authRole, setAuthRole] = useState("tenant");

  useEffect(() => { initStorage(); }, []);

  const showToast = (msg, type = "success") => {
    setToast({ msg, type });
    setTimeout(() => setToast(null), 3000);
  };

  const handleLogout = () => {
    setUser(null);
    setPage("home");
    setDropdownOpen(false);
    showToast("Logged out successfully");
  };

  const goHome = () => { setPage("home"); setViewProp(null); };

  const openProperty = (prop) => { setViewProp(prop); setPage("detail"); };

  return (
    <>
      <style>{css}</style>
      <div className="app">
        <Navbar user={user} onLogout={handleLogout} onLogin={() => { setAuthMode("login"); setPage("auth"); }}
          onPost={() => user?.role === "owner" ? setPage("post") : (setAuthRole("owner"), setPage("auth"))}
          onHome={goHome}
          onDash={() => setPage(user?.role === "owner" ? "owner-dash" : "tenant-dash")}
          dropdownOpen={dropdownOpen} setDropdownOpen={setDropdownOpen} />

        {page === "home" && <HomePage onSearch={(q) => setPage("browse")} onOpenProp={openProperty} onGetStarted={() => { setAuthMode("signup"); setPage("auth"); }} />}
        {page === "auth" && <AuthPage mode={authMode} setMode={setAuthMode} defaultRole={authRole} onSuccess={(u) => { setUser(u); setPage(u.role === "owner" ? "owner-dash" : "home"); showToast(`Welcome, ${u.name}!`); }} />}
        {page === "browse" && <BrowsePage onOpen={openProperty} user={user} showToast={showToast} />}
        {page === "detail" && viewProp && <DetailPage prop={viewProp} onBack={() => setPage("browse")} user={user} showToast={showToast} />}
        {page === "post" && user?.role === "owner" && <PostPropertyPage user={user} onBack={() => setPage("owner-dash")} showToast={showToast} onDone={() => { showToast("Property listed successfully!"); setPage("owner-dash"); }} />}
        {page === "owner-dash" && user?.role === "owner" && <OwnerDashboard user={user} onPost={() => setPage("post")} onViewProp={openProperty} showToast={showToast} />}
        {page === "tenant-dash" && user?.role === "tenant" && <TenantDashboard user={user} onBrowse={() => setPage("browse")} showToast={showToast} />}

        {toast && <div className={`toast ${toast.type}`}>{toast.msg}</div>}
      </div>
    </>
  );
}

function Navbar({ user, onLogout, onLogin, onPost, onHome, onDash, dropdownOpen, setDropdownOpen }) {
  return (
    <nav className="navbar">
      <div className="logo" onClick={onHome}>
        <div className="logo-icon">S</div>
        <span className="logo-text">Stay<span>Mate</span></span>
        <span className="no-broker-badge" style={{ marginLeft: 10 }}>
          <span style={{ fontSize: 14 }}>✓</span> No Broker
        </span>
      </div>
      <div className="nav-actions">
        {user ? (
          <>
            {user.role === "owner" && (
              <button className="btn btn-primary btn-sm" onClick={onPost}>+ List Property</button>
            )}
            <button className="btn btn-ghost btn-sm" onClick={onDash}>Dashboard</button>
            <div className="profile-menu">
              <div style={{ display: "flex", alignItems: "center", gap: 8, cursor: "pointer" }} onClick={() => setDropdownOpen(!dropdownOpen)}>
                <div className="avatar" style={{ width: 36, height: 36, fontSize: 13 }}>{user.name.split(" ").map(n => n[0]).join("").slice(0, 2).toUpperCase()}</div>
                <span style={{ fontSize: 14, fontWeight: 500, color: "var(--text)" }}>{user.name.split(" ")[0]}</span>
                <span style={{ fontSize: 12, color: "var(--muted)" }}>▾</span>
              </div>
              {dropdownOpen && (
                <div className="profile-dropdown">
                  <div style={{ padding: "8px 14px 12px", borderBottom: "1px solid var(--border)", marginBottom: 4 }}>
                    <div style={{ fontWeight: 600, fontSize: 14, color: "var(--text)" }}>{user.name}</div>
                    <div style={{ fontSize: 12, color: "var(--muted)" }}>{user.email}</div>
                    <div style={{ marginTop: 4 }}><span className={`chip chip-${user.role === "owner" ? "blue" : "green"}`}>{user.role === "owner" ? "🏠 Owner" : "🔍 Tenant"}</span></div>
                  </div>
                  <div className="pd-item" onClick={onDash}>📊 Dashboard</div>
                  {user.role === "owner" && <div className="pd-item" onClick={onPost}>➕ Post Property</div>}
                  <div className="pd-item" style={{ color: "#b91c1c" }} onClick={onLogout}>🚪 Logout</div>
                </div>
              )}
            </div>
          </>
        ) : (
          <>
            <button className="btn btn-ghost btn-sm" onClick={onLogin}>Login</button>
            <button className="btn btn-primary btn-sm" onClick={onPost}>List Your Property</button>
          </>
        )}
      </div>
    </nav>
  );
}

function HomePage({ onSearch, onOpenProp, onGetStarted }) {
  const [search, setSearch] = useState("");
  const [city, setCity] = useState("");
  const properties = getProperties().slice(0, 6);

  return (
    <>
      <div className="hero">
        <h1>Find Your Perfect Home<br /><span>Zero Broker Fee.</span> Zero Hassle.</h1>
        <p>Connect directly with property owners. No middlemen, no commissions.</p>
        <div className="search-bar">
          <select value={city} onChange={e => setCity(e.target.value)}>
            <option value="">Select City</option>
            {CITIES.map(c => <option key={c}>{c}</option>)}
          </select>
          <input value={search} onChange={e => setSearch(e.target.value)} placeholder="Locality, landmark..." onKeyDown={e => e.key === "Enter" && onSearch({ search, city })} />
          <button className="search-btn" onClick={() => onSearch({ search, city })}>Search</button>
        </div>
        <div className="stats-row">
          <div className="stat-box"><div className="num">12,400+</div><div className="lbl">Properties Listed</div></div>
          <div className="stat-box"><div className="num">₹0</div><div className="lbl">Brokerage Fee</div></div>
          <div className="stat-box"><div className="num">85,000+</div><div className="lbl">Happy Tenants</div></div>
        </div>
      </div>
      <div className="container section">
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 24 }}>
          <div className="section-title" style={{ marginBottom: 0 }}>Featured Properties</div>
          <button className="btn btn-outline btn-sm" onClick={onSearch}>View All</button>
        </div>
        <div className="prop-grid">
          {properties.map(p => <PropertyCard key={p.id} prop={p} onClick={() => onOpenProp(p)} />)}
        </div>
      </div>
      <div className="feature-section">
        <div className="container">
          <div style={{ textAlign: "center", marginBottom: 32 }}>
            <div className="section-title" style={{ marginBottom: 8 }}>Why StayMate?</div>
            <p style={{ fontSize: 16, color: "var(--muted)" }}>The smarter way to rent — directly from owner to tenant</p>
          </div>
          <div className="feature-grid">
            {[
              { icon: "🏡", title: "Direct Owner Contact", sub: "Connect directly with property owners. No brokers standing between you and your dream home." },
              { icon: "💰", title: "Zero Brokerage", sub: "Save months of rent. We charge nothing — no broker fees, no hidden charges, ever." },
              { icon: "✅", title: "Verified Listings", sub: "Every property is verified by our team. What you see is exactly what you get." },
            ].map(f => (
              <div className="feature-box" key={f.title}>
                <div className="feature-icon">{f.icon}</div>
                <div className="feature-title">{f.title}</div>
                <div className="feature-sub">{f.sub}</div>
              </div>
            ))}
          </div>
          <div style={{ textAlign: "center", marginTop: 36 }}>
            <button className="btn btn-primary btn-lg" onClick={onGetStarted}>Get Started for Free</button>
          </div>
        </div>
      </div>
    </>
  );
}

function PropertyCard({ prop, onClick }) {
  const furnishClass = prop.furnishing === "Furnished" ? "furnish-full" : prop.furnishing === "Semi-Furnished" ? "furnish-semi" : "furnish-un";
  return (
    <div className="prop-card" onClick={onClick}>
      <div className="prop-img-wrap">
        <img className="prop-img" src={prop.images[0]} alt={prop.title} onError={e => e.target.src = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"} />
        {prop.verified && <span className="prop-badge badge-verified">✓ Verified</span>}
        <span className="prop-badge badge-type">{prop.type}</span>
      </div>
      <div className="prop-body">
        <div className="prop-title">{prop.title}</div>
        <div className="prop-loc">📍 {prop.locality}, {prop.city}</div>
        <div className="prop-meta">
          <div className="prop-meta-item">🛏 {prop.bedrooms} BHK</div>
          <div className="prop-meta-item">🚿 {prop.bathrooms} Bath</div>
          <div className="prop-meta-item">📐 {prop.area} sqft</div>
        </div>
        <div className="prop-footer">
          <div className="prop-rent">₹{prop.rent.toLocaleString()} <span>/month</span></div>
          <span className={`prop-furnish ${furnishClass}`}>{prop.furnishing}</span>
        </div>
      </div>
    </div>
  );
}

function BrowsePage({ onOpen, user, showToast }) {
  const [filters, setFilters] = useState({ city: "", type: "", bedrooms: "", furnishing: "", minRent: "", maxRent: "", sort: "newest" });
  const allProps = getProperties();

  const filtered = allProps.filter(p => {
    if (filters.city && p.city !== filters.city) return false;
    if (filters.type && p.type !== filters.type) return false;
    if (filters.bedrooms && p.bedrooms !== parseInt(filters.bedrooms)) return false;
    if (filters.furnishing && p.furnishing !== filters.furnishing) return false;
    if (filters.minRent && p.rent < parseInt(filters.minRent)) return false;
    if (filters.maxRent && p.rent > parseInt(filters.maxRent)) return false;
    return true;
  }).sort((a, b) => {
    if (filters.sort === "rent-asc") return a.rent - b.rent;
    if (filters.sort === "rent-desc") return b.rent - a.rent;
    return new Date(b.postedOn) - new Date(a.postedOn);
  });

  const set = (k, v) => setFilters(f => ({ ...f, [k]: v }));

  return (
    <div className="container section">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
        <div className="section-title" style={{ marginBottom: 0 }}>Browse Properties <span style={{ fontSize: 16, color: "var(--muted)", fontWeight: 400 }}>({filtered.length} results)</span></div>
      </div>
      <div className="filter-bar">
        {[
          { label: "City", key: "city", opts: CITIES },
          { label: "Type", key: "type", opts: ["Apartment", "House", "Condo", "Studio", "Townhouse"] },
          { label: "Bedrooms", key: "bedrooms", opts: ["1", "2", "3", "4", "5+"] },
          { label: "Furnishing", key: "furnishing", opts: ["Furnished", "Semi-Furnished", "Unfurnished"] },
        ].map(f => (
          <div className="filter-group" key={f.key}>
            <label>{f.label}</label>
            <select value={filters[f.key]} onChange={e => set(f.key, e.target.value)}>
              <option value="">All</option>
              {f.opts.map(o => <option key={o}>{o}</option>)}
            </select>
          </div>
        ))}
        <div className="filter-group">
          <label>Min Rent</label>
          <input type="number" placeholder="₹ Min" value={filters.minRent} onChange={e => set("minRent", e.target.value)} />
        </div>
        <div className="filter-group">
          <label>Max Rent</label>
          <input type="number" placeholder="₹ Max" value={filters.maxRent} onChange={e => set("maxRent", e.target.value)} />
        </div>
        <div className="filter-group">
          <label>Sort By</label>
          <select value={filters.sort} onChange={e => set("sort", e.target.value)}>
            <option value="newest">Newest First</option>
            <option value="rent-asc">Rent: Low to High</option>
            <option value="rent-desc">Rent: High to Low</option>
          </select>
        </div>
        <button className="btn btn-ghost btn-sm" onClick={() => setFilters({ city: "", type: "", bedrooms: "", furnishing: "", minRent: "", maxRent: "", sort: "newest" })}>Clear</button>
      </div>
      {filtered.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">🏘</div>
          <div className="empty-title">No properties found</div>
          <div className="empty-sub">Try adjusting your filters</div>
        </div>
      ) : (
        <div className="prop-grid">
          {filtered.map(p => <PropertyCard key={p.id} prop={p} onClick={() => onOpen(p)} />)}
        </div>
      )}
    </div>
  );
}

function DetailPage({ prop, onBack, user, showToast }) {
  const [activeImg, setActiveImg] = useState(0);
  const [inquiryMsg, setInquiryMsg] = useState("Hi, I am interested in your property. Please contact me.");
  const [sent, setSent] = useState(false);
  const [showPhone, setShowPhone] = useState(false);

  const sendInquiry = () => {
    if (!user) { showToast("Please login to contact owner", "error"); return; }
    const inquiries = getInquiries();
    inquiries.push({ id: Date.now().toString(), tenantId: user.id, tenantName: user.name, tenantPhone: user.phone, tenantEmail: user.email, propertyId: prop.id, propertyTitle: prop.title, ownerId: prop.ownerId, message: inquiryMsg, createdAt: new Date().toISOString() });
    saveInquiries(inquiries);
    setSent(true);
    showToast("Inquiry sent to owner!");
  };

  return (
    <div className="detail-page">
      <button className="back-btn" onClick={onBack}>← Back to results</button>
      <div className="detail-grid">
        <div>
          <div className="img-gallery">
            <img src={prop.images[activeImg]} alt="" style={{ width: "100%", height: 340, objectFit: "cover", borderRadius: 12 }} onError={e => e.target.src = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"} />
            {prop.images.length > 1 && (
              <div className="img-thumbs">
                {prop.images.map((img, i) => (
                  <img key={i} src={img} className={`img-thumb ${activeImg === i ? "active" : ""}`} onClick={() => setActiveImg(i)} onError={e => e.target.src = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"} alt="" />
                ))}
              </div>
            )}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
            {prop.verified && <span className="chip chip-green">✓ Verified</span>}
            <span className="chip chip-blue">{prop.type}</span>
            <span className="no-broker-badge">✓ No Broker</span>
          </div>
          <div className="detail-title">{prop.title}</div>
          <div className="detail-loc">📍 {prop.address}, {prop.locality}, {prop.city}</div>
          <div style={{ display: "flex", alignItems: "baseline", gap: 10, marginBottom: 20 }}>
            <span style={{ fontSize: 28, fontWeight: 800, color: "var(--brand)" }}>₹{prop.rent.toLocaleString()}</span>
            <span style={{ fontSize: 14, color: "var(--muted)" }}>/month</span>
            <span style={{ fontSize: 14, color: "var(--muted)" }}>• Deposit: ₹{prop.deposit.toLocaleString()}</span>
          </div>
          <div className="info-grid">
            {[
              { key: "Bedrooms", val: prop.bedrooms + " BHK" },
              { key: "Bathrooms", val: prop.bathrooms },
              { key: "Area", val: prop.area + " sqft" },
              { key: "Furnishing", val: prop.furnishing },
              { key: "Available", val: prop.available_date },
              { key: "Preferred", val: prop.gender },
            ].map(i => (
              <div className="info-box" key={i.key}><div className="val">{i.val}</div><div className="key">{i.key}</div></div>
            ))}
          </div>
          <hr className="section-divider" />
          <div style={{ fontWeight: 600, fontSize: 16, marginBottom: 10 }}>About this property</div>
          <p style={{ fontSize: 14, color: "var(--muted)", lineHeight: 1.7 }}>{prop.description}</p>
          <hr className="section-divider" />
          <div style={{ fontWeight: 600, fontSize: 16, marginBottom: 12 }}>Amenities</div>
          <div className="amenity-list">
            {prop.amenities.map(a => <span key={a} className="amenity-tag">✓ {a}</span>)}
            {prop.parking && <span className="amenity-tag">🚗 Parking</span>}
            {prop.pets && <span className="amenity-tag">🐾 Pets Allowed</span>}
            {prop.water && <span className="amenity-tag">💧 24x7 Water</span>}
          </div>
        </div>
        <div>
          <div className="contact-card">
            <div style={{ fontSize: 12, color: "var(--muted)", marginBottom: 16, textAlign: "center" }}>Posted by Owner · No Broker Fee</div>
            <div className="owner-row">
              <div className="avatar">{prop.ownerName.split(" ").map(n => n[0]).join("").slice(0, 2).toUpperCase()}</div>
              <div>
                <div className="owner-name">{prop.ownerName}</div>
                <div className="owner-tag">✓ Verified Owner</div>
              </div>
            </div>
            <div className="contact-btns">
              <button className="contact-btn contact-btn-call" onClick={() => { setShowPhone(true); showToast("Owner phone revealed!"); }}>
                {showPhone ? `📞 ${prop.ownerPhone}` : "📞 View Phone Number"}
              </button>
              <button className="contact-btn contact-btn-whatsapp" onClick={() => showToast("Opening WhatsApp...")}>
                💬 WhatsApp Owner
              </button>
              <button className="contact-btn contact-btn-msg" onClick={() => showToast("Email sent to owner!")}>
                ✉️ Send Email
              </button>
            </div>
            <div className="inquiry-form">
              <div style={{ fontSize: 14, fontWeight: 600, marginBottom: 10 }}>Send Inquiry</div>
              {sent ? (
                <div className="msg-box success">✓ Your inquiry has been sent to the owner!</div>
              ) : (
                <>
                  <textarea value={inquiryMsg} onChange={e => setInquiryMsg(e.target.value)} />
                  <button className="btn btn-primary" style={{ width: "100%", marginTop: 10 }} onClick={sendInquiry}>Send Inquiry</button>
                  {!user && <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 8, textAlign: "center" }}>Login required to send inquiry</div>}
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function AuthPage({ mode, setMode, defaultRole, onSuccess }) {
  const [role, setRole] = useState(defaultRole || "tenant");
  const [form, setForm] = useState({ name: "", email: "", password: "", phone: "" });
  const [error, setError] = useState("");

  const set = (k, v) => setForm(f => ({ ...f, [k]: v }));

  const submit = () => {
    setError("");
    const users = getUsers();
    if (mode === "login") {
      const u = users.find(u => u.email === form.email && u.password === form.password);
      if (!u) { setError("Invalid email or password."); return; }
      onSuccess(u);
    } else {
      if (!form.name || !form.email || !form.password) { setError("All fields required."); return; }
      if (users.find(u => u.email === form.email)) { setError("Email already registered."); return; }
      const newUser = { id: "u_" + Date.now(), name: form.name, email: form.email, password: form.password, phone: form.phone, role, avatar: form.name.slice(0, 2).toUpperCase() };
      saveUsers([...users, newUser]);
      onSuccess(newUser);
    }
  };

  return (
    <div className="auth-wrap">
      <div className="auth-card">
        <div className="auth-logo">
          <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: 8 }}>
            <div className="logo-icon">S</div>
            <span className="logo-text">Stay<span>Mate</span></span>
          </div>
        </div>
        <div className="auth-title">{mode === "login" ? "Welcome back" : "Create your account"}</div>
        <div className="auth-sub">{mode === "login" ? "Login to access your dashboard" : "Join thousands of owners and tenants"}</div>
        <div className="role-tabs">
          {[{ id: "tenant", icon: "🔍", label: "I'm a Tenant" }, { id: "owner", icon: "🏠", label: "I'm an Owner" }].map(r => (
            <div key={r.id} className={`role-tab ${role === r.id ? "active" : ""}`} onClick={() => setRole(r.id)}>
              <div className="icon">{r.icon}</div>
              <div className="label">{r.label}</div>
            </div>
          ))}
        </div>
        {error && <div className="msg-box error" style={{ marginBottom: 16 }}>{error}</div>}
        {mode === "signup" && (
          <div className="form-group">
            <label>Full Name</label>
            <input value={form.name} onChange={e => set("name", e.target.value)} placeholder="Enter your name" />
          </div>
        )}
        <div className="form-group">
          <label>Email Address</label>
          <input type="email" value={form.email} onChange={e => set("email", e.target.value)} placeholder="you@email.com" />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" value={form.password} onChange={e => set("password", e.target.value)} placeholder="Enter password" />
        </div>
        {mode === "signup" && (
          <div className="form-group">
            <label>Phone Number</label>
            <input value={form.phone} onChange={e => set("phone", e.target.value)} placeholder="+91 99999 99999" />
          </div>
        )}
        <button className="btn btn-primary" style={{ width: "100%", padding: "12px", fontSize: 15, marginTop: 8 }} onClick={submit}>
          {mode === "login" ? "Login" : "Create Account"}
        </button>
        <div style={{ textAlign: "center", marginTop: 16, fontSize: 14, color: "var(--muted)" }}>
          {mode === "login" ? "Don't have an account? " : "Already have an account? "}
          <span style={{ color: "var(--brand)", cursor: "pointer", fontWeight: 500 }} onClick={() => setMode(mode === "login" ? "signup" : "login")}>
            {mode === "login" ? "Sign Up" : "Login"}
          </span>
        </div>
        {mode === "login" && (
          <div style={{ marginTop: 16, background: "var(--bg)", borderRadius: 8, padding: 10, fontSize: 13, color: "var(--muted)" }}>
            <strong>Demo credentials:</strong><br />
            Owner: rajesh@email.com / 1234<br />
            Tenant: arjun@email.com / 1234
          </div>
        )}
      </div>
    </div>
  );
}

function PostPropertyPage({ user, onBack, onDone, showToast }) {
  const [step, setStep] = useState(1);
  const [form, setForm] = useState({
    title: "", type: "Apartment", bedrooms: 1, bathrooms: 1, area: "",
    rent: "", deposit: "", city: "", locality: "", address: "",
    furnishing: "Semi-Furnished", available_date: "Immediately", gender: "Any",
    parking: false, pets: false, water: true,
    amenities: [],
    description: "",
    images: [""],
  });
  const [errors, setErrors] = useState({});

  const set = (k, v) => setForm(f => ({ ...f, [k]: v }));
  const toggleAmenity = (a) => set("amenities", form.amenities.includes(a) ? form.amenities.filter(x => x !== a) : [...form.amenities, a]);

  const validate = () => {
    const e = {};
    if (!form.title) e.title = "Title required";
    if (!form.rent) e.rent = "Rent required";
    if (!form.city) e.city = "City required";
    if (!form.locality) e.locality = "Locality required";
    if (!form.description) e.description = "Description required";
    setErrors(e);
    return Object.keys(e).length === 0;
  };

  const submit = () => {
    if (!validate()) return;
    const props = getProperties();
    const newProp = {
      ...form, id: "p_" + Date.now(), ownerId: user.id, ownerName: user.name, ownerPhone: user.phone || "+91 00000 00000", ownerEmail: user.email,
      images: form.images.filter(i => i.trim()),
      rent: parseInt(form.rent), deposit: parseInt(form.deposit) || parseInt(form.rent) * 2,
      bedrooms: parseInt(form.bedrooms), bathrooms: parseInt(form.bathrooms), area: parseInt(form.area) || 0,
      postedOn: new Date().toISOString().split("T")[0], verified: false,
    };
    if (!newProp.images.length) newProp.images = ["https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"];
    saveProperties([...props, newProp]);
    onDone();
  };

  const steps = ["Basic Info", "Location", "Amenities", "Description & Photos"];

  return (
    <div className="container section">
      <button className="back-btn" onClick={onBack}>← Back to Dashboard</button>
      <div className="form-container">
        <div className="form-title">List Your Property</div>
        <div style={{ display: "flex", gap: 0, marginBottom: 32, borderBottom: "2px solid var(--border)" }}>
          {steps.map((s, i) => (
            <div key={s} onClick={() => i < step && setStep(i + 1)} style={{ flex: 1, textAlign: "center", paddingBottom: 12, fontSize: 13, fontWeight: 500, cursor: "pointer",
              color: step === i + 1 ? "var(--brand)" : i + 1 < step ? "var(--success)" : "var(--muted)",
              borderBottom: `2px solid ${step === i + 1 ? "var(--brand)" : i + 1 < step ? "var(--success)" : "transparent"}`, marginBottom: -2 }}>
              <span>{i + 1 < step ? "✓ " : ""}{s}</span>
            </div>
          ))}
        </div>

        {step === 1 && (
          <>
            <div className="form-group">
              <label>Property Title *</label>
              <input value={form.title} onChange={e => set("title", e.target.value)} placeholder="e.g. Spacious 2BHK in Koramangala" />
              {errors.title && <span style={{ color: "red", fontSize: 12 }}>{errors.title}</span>}
            </div>
            <div className="form-row">
              <div className="form-group">
                <label>Property Type *</label>
                <select value={form.type} onChange={e => set("type", e.target.value)}>
                  {["Apartment", "House", "Condo", "Studio", "Townhouse", "Duplex", "PG"].map(t => <option key={t}>{t}</option>)}
                </select>
              </div>
              <div className="form-group">
                <label>Furnishing *</label>
                <select value={form.furnishing} onChange={e => set("furnishing", e.target.value)}>
                  {["Furnished", "Semi-Furnished", "Unfurnished"].map(t => <option key={t}>{t}</option>)}
                </select>
              </div>
            </div>
            <div className="form-row-3">
              <div className="form-group">
                <label>Bedrooms</label>
                <select value={form.bedrooms} onChange={e => set("bedrooms", e.target.value)}>
                  {[1,2,3,4,5].map(n => <option key={n}>{n}</option>)}
                </select>
              </div>
              <div className="form-group">
                <label>Bathrooms</label>
                <select value={form.bathrooms} onChange={e => set("bathrooms", e.target.value)}>
                  {[1,2,3,4].map(n => <option key={n}>{n}</option>)}
                </select>
              </div>
              <div className="form-group">
                <label>Area (sqft)</label>
                <input type="number" value={form.area} onChange={e => set("area", e.target.value)} placeholder="1000" />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group">
                <label>Monthly Rent (₹) *</label>
                <input type="number" value={form.rent} onChange={e => set("rent", e.target.value)} placeholder="25000" />
                {errors.rent && <span style={{ color: "red", fontSize: 12 }}>{errors.rent}</span>}
              </div>
              <div className="form-group">
                <label>Security Deposit (₹)</label>
                <input type="number" value={form.deposit} onChange={e => set("deposit", e.target.value)} placeholder="50000" />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group">
                <label>Available From</label>
                <select value={form.available_date} onChange={e => set("available_date", e.target.value)}>
                  {["Immediately", "15 Days", "1 Month", "2 Months"].map(t => <option key={t}>{t}</option>)}
                </select>
              </div>
              <div className="form-group">
                <label>Preferred Tenant</label>
                <select value={form.gender} onChange={e => set("gender", e.target.value)}>
                  {["Any", "Family", "Bachelor Male", "Bachelor Female", "Working Professional"].map(t => <option key={t}>{t}</option>)}
                </select>
              </div>
            </div>
          </>
        )}

        {step === 2 && (
          <>
            <div className="form-row">
              <div className="form-group">
                <label>City *</label>
                <select value={form.city} onChange={e => set("city", e.target.value)}>
                  <option value="">Select City</option>
                  {CITIES.map(c => <option key={c}>{c}</option>)}
                </select>
                {errors.city && <span style={{ color: "red", fontSize: 12 }}>{errors.city}</span>}
              </div>
              <div className="form-group">
                <label>Locality *</label>
                <input value={form.locality} onChange={e => set("locality", e.target.value)} placeholder="e.g. Koramangala, Indiranagar" />
                {errors.locality && <span style={{ color: "red", fontSize: 12 }}>{errors.locality}</span>}
              </div>
            </div>
            <div className="form-group">
              <label>Full Address</label>
              <input value={form.address} onChange={e => set("address", e.target.value)} placeholder="Street, area, landmark" />
            </div>
          </>
        )}

        {step === 3 && (
          <>
            <div className="form-group">
              <label>Amenities</label>
              <div className="amenity-checks">
                {AMENITIES_LIST.map(a => (
                  <div key={a} className={`amenity-check ${form.amenities.includes(a) ? "checked" : ""}`} onClick={() => toggleAmenity(a)}>{a}</div>
                ))}
              </div>
            </div>
            <div className="form-group" style={{ marginTop: 16 }}>
              <label>Additional Features</label>
              <div className="toggle-row">
                {[{ k: "parking", label: "🚗 Parking" }, { k: "pets", label: "🐾 Pets Allowed" }, { k: "water", label: "💧 24x7 Water" }].map(t => (
                  <label key={t.k} className="toggle-item">
                    <input type="checkbox" checked={form[t.k]} onChange={e => set(t.k, e.target.checked)} />
                    {t.label}
                  </label>
                ))}
              </div>
            </div>
          </>
        )}

        {step === 4 && (
          <>
            <div className="form-group">
              <label>Property Description *</label>
              <textarea value={form.description} onChange={e => set("description", e.target.value)} placeholder="Describe your property — highlights, nearby landmarks, connectivity..." style={{ minHeight: 120 }} />
              {errors.description && <span style={{ color: "red", fontSize: 12 }}>{errors.description}</span>}
            </div>
            <div className="form-group">
              <label>Photo URLs (paste image links)</label>
              {form.images.map((img, i) => (
                <div key={i} style={{ display: "flex", gap: 8, marginBottom: 8 }}>
                  <input value={img} onChange={e => { const imgs = [...form.images]; imgs[i] = e.target.value; set("images", imgs); }} placeholder="https://..." />
                  {i === form.images.length - 1 && (
                    <button className="btn btn-ghost btn-sm" onClick={() => set("images", [...form.images, ""])}>+</button>
                  )}
                </div>
              ))}
              <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 4 }}>Paste Unsplash or any direct image URLs</div>
            </div>
          </>
        )}

        <div style={{ display: "flex", justifyContent: "space-between", marginTop: 32 }}>
          <button className="btn btn-ghost" onClick={step > 1 ? () => setStep(s => s - 1) : onBack}>{step > 1 ? "← Previous" : "Cancel"}</button>
          {step < 4 ? (
            <button className="btn btn-primary" onClick={() => { if (step === 1 && (!form.title || !form.rent)) { validate(); return; } if (step === 2 && (!form.city || !form.locality)) { validate(); return; } setStep(s => s + 1); }}>Next →</button>
          ) : (
            <button className="btn btn-primary btn-lg" onClick={submit}>🏠 Publish Property</button>
          )}
        </div>
      </div>
    </div>
  );
}

function OwnerDashboard({ user, onPost, onViewProp, showToast }) {
  const [tab, setTab] = useState("listings");
  const [props, setProps] = useState([]);
  const [inquiries, setInquiries] = useState([]);

  useEffect(() => {
    setProps(getProperties().filter(p => p.ownerId === user.id));
    setInquiries(getInquiries().filter(i => i.ownerId === user.id));
  }, []);

  const deleteProp = (id) => {
    const updated = getProperties().filter(p => p.id !== id);
    saveProperties(updated);
    setProps(props.filter(p => p.id !== id));
    showToast("Property deleted");
  };

  return (
    <div className="owner-dash">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 28 }}>
        <div>
          <div style={{ fontSize: 24, fontWeight: 700, color: "var(--text)" }}>Owner Dashboard</div>
          <div style={{ fontSize: 14, color: "var(--muted)", marginTop: 4 }}>Welcome back, {user.name}</div>
        </div>
        <button className="btn btn-primary" onClick={onPost}>+ List New Property</button>
      </div>
      <div className="dash-stats">
        {[
          { icon: "🏠", val: props.length, lbl: "Total Listings" },
          { icon: "📩", val: inquiries.length, lbl: "Total Inquiries" },
          { icon: "✅", val: props.filter(p => p.verified).length, lbl: "Verified" },
          { icon: "👁", val: props.length * 34, lbl: "Total Views" },
        ].map(s => (
          <div className="dash-stat" key={s.lbl}>
            <div className="ds-icon">{s.icon}</div>
            <div className="ds-val">{s.val}</div>
            <div className="ds-lbl">{s.lbl}</div>
          </div>
        ))}
      </div>
      <div className="tabs">
        {[["listings", "My Listings"], ["inquiries", "Inquiries"]].map(([k, l]) => (
          <div key={k} className={`tab ${tab === k ? "active" : ""}`} onClick={() => setTab(k)}>{l} {k === "inquiries" && inquiries.length > 0 && <span style={{ background: "var(--brand)", color: "white", borderRadius: 10, padding: "1px 7px", fontSize: 11, marginLeft: 5 }}>{inquiries.length}</span>}</div>
        ))}
      </div>
      {tab === "listings" && (
        <>
          {props.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">🏘</div>
              <div className="empty-title">No listings yet</div>
              <div className="empty-sub">Post your first property to start receiving tenant inquiries</div>
              <button className="btn btn-primary" style={{ marginTop: 16 }} onClick={onPost}>+ Post Property</button>
            </div>
          ) : (
            props.map(p => (
              <div className="listing-card" key={p.id}>
                <img className="listing-thumb" src={p.images[0]} alt="" onError={e => e.target.src = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800"} />
                <div className="listing-body">
                  <div className="listing-title">{p.title}</div>
                  <div className="listing-meta">📍 {p.locality}, {p.city} • ₹{p.rent.toLocaleString()}/mo • {p.bedrooms}BHK • {p.furnishing}</div>
                  <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
                    {p.verified ? <span className="chip chip-green">✓ Verified</span> : <span className="chip chip-amber">⏳ Pending</span>}
                    <span style={{ fontSize: 12, color: "var(--muted)" }}>Posted: {p.postedOn}</span>
                  </div>
                  <div className="listing-actions" style={{ marginTop: 10 }}>
                    <button className="btn btn-ghost btn-sm" onClick={() => onViewProp(p)}>👁 View</button>
                    <button className="btn btn-danger btn-sm" onClick={() => deleteProp(p.id)}>🗑 Delete</button>
                  </div>
                </div>
              </div>
            ))
          )}
        </>
      )}
      {tab === "inquiries" && (
        <>
          {inquiries.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">📩</div>
              <div className="empty-title">No inquiries yet</div>
              <div className="empty-sub">Inquiries from tenants will appear here</div>
            </div>
          ) : (
            inquiries.map(inq => (
              <div className="inquiry-item" key={inq.id}>
                <div className="inq-header">
                  <span className="inq-name">👤 {inq.tenantName}</span>
                  <span className="inq-time">{new Date(inq.createdAt).toLocaleDateString()}</span>
                </div>
                <div className="inq-prop">🏠 {inq.propertyTitle}</div>
                <div className="inq-msg">"{inq.message}"</div>
                <div style={{ marginTop: 10, display: "flex", gap: 8 }}>
                  <button className="btn btn-success btn-sm">📞 {inq.tenantPhone || "View Phone"}</button>
                  <button className="btn btn-ghost btn-sm">✉️ {inq.tenantEmail}</button>
                </div>
              </div>
            ))
          )}
        </>
      )}
    </div>
  );
}

function TenantDashboard({ user, onBrowse, showToast }) {
  const inquiries = getInquiries().filter(i => i.tenantId === user.id);

  return (
    <div className="owner-dash">
      <div style={{ marginBottom: 28 }}>
        <div style={{ fontSize: 24, fontWeight: 700, color: "var(--text)" }}>Tenant Dashboard</div>
        <div style={{ fontSize: 14, color: "var(--muted)", marginTop: 4 }}>Welcome back, {user.name}</div>
      </div>
      <div className="dash-stats" style={{ gridTemplateColumns: "repeat(3,1fr)" }}>
        {[
          { icon: "📩", val: inquiries.length, lbl: "Inquiries Sent" },
          { icon: "🔍", val: "0", lbl: "Saved Properties" },
          { icon: "🏠", val: "0", lbl: "Rented" },
        ].map(s => (
          <div className="dash-stat" key={s.lbl}>
            <div className="ds-icon">{s.icon}</div>
            <div className="ds-val">{s.val}</div>
            <div className="ds-lbl">{s.lbl}</div>
          </div>
        ))}
      </div>
      <div style={{ marginTop: 28 }}>
        <div style={{ fontSize: 18, fontWeight: 600, marginBottom: 16 }}>Your Inquiries</div>
        {inquiries.length === 0 ? (
          <div className="empty-state">
            <div className="empty-icon">🔍</div>
            <div className="empty-title">No inquiries yet</div>
            <div className="empty-sub">Browse properties and reach out to owners directly</div>
            <button className="btn btn-primary" style={{ marginTop: 16 }} onClick={onBrowse}>Browse Properties</button>
          </div>
        ) : (
          inquiries.map(inq => (
            <div className="inquiry-item" key={inq.id}>
              <div className="inq-header">
                <span className="inq-prop" style={{ margin: 0 }}>🏠 {inq.propertyTitle}</span>
                <span className="inq-time">{new Date(inq.createdAt).toLocaleDateString()}</span>
              </div>
              <div className="inq-msg" style={{ marginTop: 6 }}>"{inq.message}"</div>
              <div style={{ marginTop: 8 }}><span className="chip chip-blue">✓ Sent</span></div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
