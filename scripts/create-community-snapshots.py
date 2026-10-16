from __future__ import annotations

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "community-web-snapshots"
OUT.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("MSYH", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def para(value: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(esc(value).replace("\n", "<br/>") , style)


def make_pdf(
    filename: str,
    title: str,
    url: str,
    status: str,
    capture: str,
    source_date: str,
    notes: list[str],
    sections: list[tuple[str, str]],
    links: list[tuple[str, str, str]],
) -> None:
    path = OUT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CJKTitle", parent=styles["Title"], fontName="MSYH",
        fontSize=18, leading=23, alignment=TA_CENTER, textColor=colors.HexColor("#17324D"),
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="CJKHeading", parent=styles["Heading2"], fontName="MSYH",
        fontSize=12, leading=16, textColor=colors.HexColor("#17324D"), spaceBefore=9, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="CJKBody", parent=styles["BodyText"], fontName="MSYH",
        fontSize=9.2, leading=13.2, textColor=colors.HexColor("#20252B"), spaceAfter=5,
    ))
    styles.add(ParagraphStyle(
        name="CJKSmall", parent=styles["BodyText"], fontName="MSYH",
        fontSize=8, leading=11, textColor=colors.HexColor("#4B5563"), spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="LinkCell", parent=styles["BodyText"], fontName="MSYH",
        fontSize=7, leading=9, textColor=colors.HexColor("#20252B"), wordWrap="CJK",
    ))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D5DCE3"))
        canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
        canvas.setFont("MSYH", 7)
        canvas.setFillColor(colors.HexColor("#6B7280"))
        canvas.drawString(18 * mm, 9 * mm, "Monety community web snapshot")
        canvas.drawRightString(192 * mm, 9 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(
        str(path), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=17 * mm, bottomMargin=20 * mm, title=title, author="Monety",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=footer)])

    story = [Paragraph(esc(title), styles["CJKTitle"])]
    meta = [
        [para("状态", styles["LinkCell"]), para(status, styles["LinkCell"])],
        [para("来源 URL", styles["LinkCell"]), para(url, styles["LinkCell"])],
        [para("抓取时间", styles["LinkCell"]), para(capture, styles["LinkCell"])],
        [para("原文日期", styles["LinkCell"]), para(source_date, styles["LinkCell"])],
    ]
    table = Table(meta, colWidths=[25 * mm, 149 * mm], repeatRows=0)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EEF3F7")),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#B9C6D2")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D5DCE3")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story += [table, Spacer(1, 8)]

    if notes:
        story.append(Paragraph("抓取说明", styles["CJKHeading"]))
        for note in notes:
            story.append(Paragraph("• " + esc(note), styles["CJKBody"]))

    for heading, body in sections:
        story.append(Paragraph(esc(heading), styles["CJKHeading"]))
        for paragraph in body.split("\n\n"):
            story.append(Paragraph(esc(paragraph).replace("\n", "<br/>"), styles["CJKBody"]))

    if links:
        story.append(Paragraph("正文/评论中识别的附属链接", styles["CJKHeading"]))
        rows = [[para("链接文本", styles["LinkCell"]), para("URL", styles["LinkCell"]), para("快照", styles["LinkCell"])]]
        for label, link_url, link_status in links:
            rows.append([para(label, styles["LinkCell"]), para(link_url, styles["LinkCell"]), para(link_status, styles["LinkCell"])])
        link_table = Table(rows, colWidths=[35 * mm, 104 * mm, 35 * mm], repeatRows=1)
        link_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#B9C6D2")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D5DCE3")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(link_table)

    doc.build(story)


def main() -> None:
    capture = "2026-10-15 Asia/Shanghai"
    network_links = [
        ("tips to improve revenue", "https://www.reddit.com/r/admob/comments/1ojk0vn/my_tips_to_improve_your_revenue_from_ads/", "text-fallback PDF"),
        ("AdMob ad sources", "https://developers.google.com/admob/android/choose-networks", "rendered PDF"),
        ("Families ads SDK", "https://support.google.com/googleplay/android-developer/answer/12955712?hl=en", "rendered PDF"),
        ("App Manager", "https://play.google.com/store/apps/details?id=com.lb.app_manager", "rendered PDF"),
        ("Full-screen native", "https://developers.google.com/admob/android/native/full-screen", "rendered PDF"),
        ("VocaLearn", "https://play.google.com/store/apps/details?id=com.lb.vocalearn&referrer=utm_source%3Dreddit%26utm_medium%3Dsocial%26utm_campaign%3Dvocalearn_post", "rendered PDF"),
        ("MREC/fixed banner", "https://developers.google.com/admob/android/banner/fixed-size", "rendered PDF"),
        ("Meta testing page", "https://business.facebook.com/pub/testing", "blocked/login status PDF"),
        ("Meta app-ads.txt", "https://developers.facebook.com/docs/audience-network/optimization/best-practices/authorized-sellers-app-ads/#adding-facebook-with-a-business-id", "rendered PDF"),
    ]
    tips_links = [
        ("App Manager", "https://play.google.com/store/apps/details?id=com.lb.app_manager", "rendered PDF"),
        ("AdMob ad sources", "https://developers.google.com/admob/android/choose-networks", "rendered PDF"),
        ("Families ads SDK", "https://support.google.com/googleplay/android-developer/answer/12955712?hl=en", "rendered PDF"),
        ("various ad-networks", "https://www.reddit.com/r/admob/comments/1oy8gjd/my_experience_with_the_various_adnetworks_for/", "text-fallback PDF"),
        ("UMP SDK", "https://developers.google.com/admob/android/privacy", "rendered PDF"),
        ("custom ad partners dashboard", "URL not exposed by public index (Reddit link id 10)", "unresolved/status PDF"),
        ("app-ads.txt dashboard", "https://admob.google.com/v2/apps/appadstxt", "login redirect status PDF"),
        ("GitHub Pages app-ads.txt", "https://stackoverflow.com/a/79386462/878126", "rendered PDF"),
        ("Distill Web Monitor", "https://chromewebstore.google.com/detail/distill-web-monitor/inlikjemeeknofckkjolnjbpehgadgge", "rendered PDF"),
        ("LiftOff download script", "https://greasyfork.org/en/scripts/539329-vungle-prevent-auto-downloads", "rendered PDF"),
        ("MobileAds.initialize", "https://developers.google.com/admob/android/reference/com/google/android/gms/ads/MobileAds", "rendered PDF"),
        ("Banner automatic refresh", "https://support.google.com/admob/answer/3245199?hl=en-GB", "rendered PDF"),
        ("AdMob fixed banner", "https://developers.google.com/admob/android/banner/fixed-size", "rendered PDF"),
        ("AppLovin size discussion", "https://groups.google.com/g/google-admob-ads-sdk/c/y9j--NoFaKo/m/ZhCORrU3AAAJ", "rendered PDF"),
        ("Pangle placements", "https://www.pangleglobal.com/knowledge/set-up-ad-placements", "rendered PDF"),
        ("privacy/consent discussion", "https://stackoverflow.com/q/79371638/878126", "rendered PDF"),
        ("GameZop", "https://www.gamezop.com/en", "rendered PDF"),
        ("NativeAdOptions", "https://developers.google.com/admob/android/reference/com/google/android/gms/ads/nativead/NativeAdOptions.Builder", "rendered PDF"),
        ("rewarded SSV", "https://developers.google.com/admob/android/ssv", "rendered PDF"),
        ("setHttpTimeoutMillis reference", "https://developers.google.com/admob/android/reference/com/google/android/gms/ads/AbstractAdRequestBuilder", "rendered PDF"),
        ("moveTaskToBack", "https://developer.android.com/reference/android/app/Activity", "rendered PDF"),
        ("Ad content rating", "https://support.google.com/admob/answer/7562142?hl=en", "rendered PDF"),
        ("Target audience", "https://support.google.com/googleplay/android-developer/answer/9867159?hl=en", "rendered PDF"),
        ("AdMob app list", "URL not exposed by public index (Reddit link id 23)", "unresolved/status PDF"),
        ("AdMob account settings", "URL not exposed by public index (Reddit link id 29)", "unresolved/status PDF"),
        ("Share full IP address", "https://support.google.com/admob/answer/16731059", "rendered PDF"),
        ("AdMob Next-Gen migration", "https://developers.google.com/admob/android/next-gen/migration", "rendered PDF"),
        ("Next-Gen discussion", "https://www.reddit.com/r/admob/comments/1qhje7b/has_anyone_tried_the_new_admob_android_google/", "rendered/text PDF"),
        ("AdMob test ads", "https://developers.google.com/admob/android/test-ads", "rendered PDF"),
        ("Next-Gen video", "URL not exposed by public index (Reddit link id 33)", "unresolved/status PDF"),
        ("redesigned AdMob", "https://blog.google/products/admob/introducing-new-redesigned-admob-4jgg/", "rendered PDF"),
        ("earnings app", "https://play.google.com/store/apps/details?id=net.hubalek.android.apps.myandroidearnings", "rendered PDF"),
        ("Medium Compose Multiplatform comment", "https://meet-miyani.medium.com/why-i-built-admob-cmp-compose-multiplatform-146fed8cc4ec", "rendered PDF"),
    ]

    network_body = (
        "After posting my tips I've accumulated over the years with AdMob, the author asks about other networks and shares a multi-app experience. Most revenue comes from native ads; banner ads are fallbacks. Rewarded ads have the highest eCPM in this account, while interstitials are a low priority.\n\n"
        "The author's self-reported eCPM order is: native - AdMob, Meta/Facebook, Liftoff/Vungle, InMobi Exchange, Mintegral, Pangle, InMobi, Equativ; banners - Chartboost, Meta/Facebook, AdMob, Equativ, Liftoff/Vungle, InMobi, Unity, Mintegral, InMobi Exchange, Pangle; rewarded - InMobi, Unity, AdMob, Liftoff/Vungle, Mintegral, Pangle, Chartboost; rewarded interstitial - Liftoff/Vungle, AdMob; interstitial - Unity, AdMob. The author explicitly says eCPM is not everything and that fill rate matters.\n\n"
        "Reported operational notes include: AdMob is about 90% of the author's ad revenue; Liftoff has strong support and bidding coverage; Meta has payment, support, device-login and banner-size friction; Mintegral and Unity have app-ads.txt validation; InMobi was tested by country; Pangle has strict setup and orientation requirements; Yandex had native-ad and crash problems; Chartboost was removed after poor revenue and a crash; several networks produced no revenue or rejected the account. These are single-account observations, not benchmarks."
    )
    make_pdf(
        "reddit/admob-network-experience.pdf",
        "Reddit text snapshot: My experience with the various ad-networks for AdMob mediation",
        "https://www.reddit.com/r/admob/comments/1oy8gjd/my_experience_with_the_various_adnetworks_for/",
        "text-fallback (Reddit returned HTTP 403 to direct and JSON requests)",
        capture,
        "2026-09-24",
        [
            "This PDF preserves the indexed post text and the link inventory available through the search service; it is not a browser-rendered Reddit HTML archive.",
            "The numbers and rankings are the author's personal account across multiple apps and should be treated as a B-level hypothesis only.",
        ],
        [("正文摘录", network_body)],
        network_links,
    )

    tips_body = (
        "The author reports applying these tips across their apps. The core recommendations are to use mediation, prefer bidding over waterfall when possible, handle GDPR/CCPA, payments and app-ads.txt for every network, and avoid waiting indefinitely for all SDKs before the first request. The author chose a four-second initialization budget.\n\n"
        "The post compares native and banner formats, recommends testing MREC and multiple full-screen fallbacks (rewarded, rewarded interstitial, interstitial), suggests country-specific mediation groups, and describes using remote config. It also recommends a fallback when no ad loads, a paywall option to remove fixed ads, ad-content-rating experiments, server-side rewarded validation, and monitoring account/app status.\n\n"
        "The author states that their own results are not universal and that most advice should be measured with local A/B tests. Comments discuss Meta no-fill, Facebook login and the Meta testing page, and point to app-ads.txt requirements."
    )
    make_pdf(
        "reddit/admob-revenue-tips.pdf",
        "Reddit text snapshot: My tips to improve your revenue from ads",
        "https://www.reddit.com/r/admob/comments/1ojk0vn/my_tips_to_improve_your_revenue_from_ads/",
        "text-fallback (Reddit returned HTTP 403 to direct and JSON requests)",
        capture,
        "2026-10-29 (indexed page date; Reddit search display)",
        [
            "This is a text snapshot of the indexed post and not a direct HTML capture.",
            "The PDF includes the direct-link inventory from the post body. Login-only and unresolved dashboard links are separately marked in the manifest.",
        ],
        [("正文摘录", tips_body)],
        tips_links,
    )

    make_pdf(
        "official/meta-testing-status.pdf",
        "Linked-page status: Meta Audience Network testing page",
        "https://business.facebook.com/pub/testing",
        "blocked/login-required (the page did not expose public content)",
        capture,
        "not available",
        [
            "The URL is explicitly linked from a Reddit comment as the Meta device-testing page.",
            "A public browser session could not retrieve a stable page body without Meta login/session state; this file records the limitation instead of fabricating a page snapshot.",
        ],
        [("访问结果", "Meta Business testing page requires an authenticated session or did not expose public content.")],
        [],
    )

    make_pdf(
        "official/admob-dashboard-links-status.pdf",
        "Linked-page status: AdMob dashboard links",
        "https://admob.google.com/v2/apps/appadstxt",
        "login-required / unresolved dashboard route",
        capture,
        "not applicable",
        [
            "The Reddit post links to AdMob dashboard pages for custom mediation partners, app-ads.txt validation, app list and account settings.",
            "These are account-scoped pages. The search service redirected the app-ads.txt link to Google sign-in and did not expose stable public content for the other dashboard links.",
        ],
        [("app-ads.txt dashboard", "https://admob.google.com/v2/apps/appadstxt"), ("other dashboard links", "URL hidden behind Reddit link IDs and account session")],
        [],
    )


if __name__ == "__main__":
    main()
