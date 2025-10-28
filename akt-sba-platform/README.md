# Dr. Yousra Abdelatti — MRCGP(UK) AKT SBA Platform (Streamlit)

A production-grade, cross-platform **AKT SBA** training app scaffold.  
This is **Step 0**: UI skeleton, navigation, wallpaper banner (with graceful fallback), global branding, and minimal content-protection hooks.  
Next steps add Supabase Auth/DB, RBAC, item authoring, delivery engine, analytics, and hardened protections.

## Quick Start (Local)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Place your wallpaper portrait at:
```
assets/brand/yousra.jpg   # or assets/brand/yousra.png
```
Or use the in-app uploader (temporary for the session; persistent storage arrives in Step 1).

## Deploy to Streamlit Community Cloud

1. Push this repo to GitHub (e.g., `akt-sba-platform`).
2. Go to **Streamlit Community Cloud** → **New app**.
3. Select your repo & branch.  
   - **Main file path**: `streamlit_app.py`
4. In **App settings → Secrets**, paste the contents of `.streamlit/secrets.toml.example`, set values, and **Save**.
5. Deploy.

### Required Secrets (for next steps)
- `PRIMARY_ADMIN_BOOTSTRAP_CODE` (temporary bootstrap)
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- (Optional) `SUPABASE_SERVICE_ROLE_KEY` for admin-only server operations
- `SUPABASE_BUCKET` (e.g., `wallpaper`)

> **Branding/Legal Footer**  
> Appears on every page:  
> `© Dr. Yousra Abdelatti, Family Medicine MD, MRCGP [INT]. All rights reserved. Developed by Dr. Mohammedelnagi Mohammed.`

## Roadmap

- **Step 1** — Supabase Auth & SQL schema; email/password sign-up; admin approval gate  
- **Step 2** — RBAC & Admin Console; audit logging utilities  
- **Step 3** — Item authoring with RCGP AKT SBA linter and reference manager  
- **Step 4** — Exam engine (Tutor/Timed), storage of attempts, explanations & analytics  
- **Step 5** — Learner analytics (blueprint breakdown, distractor patterns, percentiles)  
- **Step 6** — Stronger content-protection (DOM obfuscation, print hooks, watermarks, logging)  
- **Step 7** — Sample AKT-level items (10 exemplars with references)  
- **Step 8** — Accessibility, tests, error-handling, hardening

## Notes on Content Protection

Absolute prevention of copying/screenshotting isn’t possible on the web. We implement best-effort measures (disabling context menu/selection, warning on print/screenshot keys, watermarking). We will log events to an audit trail starting Step 2.

## License

All proprietary content and branding **© Dr. Yousra Abdelatti, Family Medicine MD, MRCGP [INT].**  
Developed by **Dr. Mohammedelnagi Mohammed**. All rights reserved.
