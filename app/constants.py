from typing import Final
APP_TITLE: Final = "Dr. Yousra Abdelatti — MRCGP(UK) AKT SBA Bank"
BRAND_LINE: Final = ("© Dr. Yousra Abdelatti, Family Medicine MD, MRCGP [INT]. All rights reserved. Developed by Dr. Mohammedelnagi Mohammed.")
ASSETS_WALLPAPER_CANDIDATES: Final = ["assets/brand/yousra.jpg","assets/brand/yousra.jpeg","assets/brand/yousra.png"]
PLACEHOLDER_WALLPAPER_CSS: Final = """
.banner-placeholder {background: linear-gradient(120deg, #0f172a 0%, #1e293b 35%, #0f766e 100%);border-radius: 16px;min-height: 180px;display: flex;align-items: center;justify-content: center;color: #e2e8f0;font-weight: 600;letter-spacing: .2px;}
.banner-img {width: 100%; height: 220px; object-fit: cover; border-radius: 16px; filter: blur(1px) brightness(0.85);}
.watermark {position: fixed; bottom: 64px; right: 24px; opacity: 0.06; font-size: 12px; user-select: none;}
.footer-legal {font-size: 12px; color: var(--text-color, #6b7280); text-align: center; margin-top: 36px;}
.no-select {-webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none;}
"""
DEFAULT_PAGE_DESC: Final = ("An AKT-style SBA bank with RBAC, moderation, audit trails, and analytics.")
