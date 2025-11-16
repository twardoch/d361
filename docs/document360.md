# Combined Documentation

## Table of Contents

- [What is Document360?](#document360-getting-started)
- [Sign up to Document360](#sign-up-to-document-360)
- [System and browser requirements](#system-and-browser-requirements)
- [Project dashboard](#document360-my-projects)
- [Top-right menu overview](#top-right-menu-overview)
- [Creating a project in Document360](#creating-a-project)
- [Dashboard](#dashboard)
- [Multilingual Knowledge bases](#getting-started-with-multi-lingual-knowledge-base)
- [Creating a sandbox project](#creating-a-sandbox-project)
- [Document360 security and infrastructure](#quick-summary-of-the-security-and-infrastructure-aspects)
- [X-Frame options](#x-frame-options)
- [Content security policy](#content-security-policy)
- [CSP and Whitelisting guidelines for Document360 widget](#csp-guidelines-for-document360-widget)
- [Bot management](#bot-management)
- [Fair usage policy for bot management](#fair-usage-policy-for-bot-management)
- [Editor choices in Document360](#using-the-text-editor)
- [Elements of the editor](#elements-of-the-editor)
- [Markdown editor](#markdown-editor-overview)
- [Basic Markdown syntax](#markdown-basics)
- [WYSIWYG editor](#wysiwyg-editor)
- [Advanced WYSIWYG editor](#advanced-wysiwyg-editor)
- [Advanced WYSIWYG editor basics](#advanced-wysiwyg-editor-basics)
- [Movable blocks in Advanced WYSIWYG editor](#movable-blocks-in-advanced-wysiwyg-editor)
- [Conditional content blocks in Advanced WYSIWYG editor](#conditional-content-blocks)
- [Tables in Advanced WYSIWYG editor](#tables-in-advanced-wysiwyg-editor)
- [Image formatting in the Advanced WYSIWYG editor](#image-formatting-in-the-advanced-wysiwyg-editor)
- [Tabs in the Advanced WYSIWYG editor](#tabs-in-the-advanced-wysiwyg-editor)
- [Categories and subcategories](#categories-and-subcategories)
- [Managing categories](#managing-categories)
- [Category types](#category-types)
- [Mapping a category with a folder in Drive](#assigning-drive-folder-for-a-category)
- [Downloading category and article in KB site](#downloading-category-and-article-in-kb-site)
- [Managing articles](#managing-articles)
- [Word .docx files](#article-import-from-word-files)
- [Publishing an article](#publishing-an-article)
- [Reviewing an article using Inline comments](#reviewing-an-article-inline-comments)
- [Adding images to articles](#adding-images-to-articles)
- [Adding videos in articles](#adding-videos-in-articles)
- [Adding files to article](#adding-files-to-articles)
- [Adding hyperlinks](#linking-to-other-articles)
- [Code blocks](#code-blocks)
- [Adding private notes](#private-notes)
- [Embedding Stream videos in articles](#embedding-microsoft-streams-video-in-articles)
- [Embedding Google forms in articles](#embedding-google-forms-in-article)
- [Embedding a Draw.io diagram](#embedding-a-drawio-diagram)
- [All articles - Overview page](#all-articles-overview-page)
- [Using filters in All articles page](#filter-bulk-operations)
- [Export All articles list](#export-bulk-operations)
- [Article review reminder](#review-reminders)
- [Article SEO](#article-seo)
- [Excluding articles from search engines](#excluding-articles-from-searches)
- [Change the URL of an article](#changing-the-url-of-an-article)
- [Article tags](#article-tags)
- [Add article labels](#adding-article-labels)
- [Related articles](#related-articles)
- [Featured image](#featured-image)
- [Attachments](#attachments)
- [Status indicator](#status-indicator)
- [Article status](#article-status)
- [Preferences](#preferences)
- [Show/hide table of contents for an article](#showhide-table-of-contents-for-an-article)
- [Mark as deprecated](#marking-articles-as-deprecated)
- [Update article contributors](#updating-article-contributors)
- [Schedule publishing](#schedule-publishing)
- [Discussion feed](#article-discussion-feed)
- [Revision history](#revision-history)
- [Article analytics](#article-analytics)
- [Security - Article access control](#article-access-control-knowledge-base-site)
- [Health check metrics](#health-check-metrics)
- [Readability score](#readability-score)
- [Sitemap](#sitemap-generator)
- [Public article comments](#public-comments)
- [Robots.txt](#robotstxt)
- [Read receipt](#read-receipt)
- [Share articles via private link](#share-articles-via-private-link)
- [Eddy AI customization](#ai-customization)
- [AI machine translation](#ai-machine-translation)
- [Eddy AI trust page](#eddy-ai-trust-page)
- [AI writer suite](#ai-writer-suite)
- [AI writer](#ai-writer)
- [AI FAQ generator](#ai-faq-generator)
- [AI title recommender](#ai-title-recommender)
- [AI SEO description generator](#seo-description-generator)
- [AI tag recommender](#ai-tag-recommender)
- [AI related articles recommender](#ai-related-articles-recommender)
- [AI Chart generator](#ai-chart-generator)
- [AI alt text generator](#ai-alt-text-generator)
- [AI search suite](#ai-search-suite)
- [AI assistive search (Ask Eddy AI)](#ai-assistive-search-ask-eddy)
- [AI dynamic related articles recommendation](#ai-dynamic-related-articles-recommendation)
- [AI Chatbot](#ai-chatbot)
- [Securing Chatbot authentication using JWT](#securing-chatbot-authentication-using-jwt)
- [Styling the Chatbot](#styling-the-chatbot)
- [Adding external sources for AI Assistive search](#eddy-ai-federated-search)
- [AI article summarizer](#ai-article-summarizer)
- [Ask Eddy AI API](#ask-eddy-ai-api)
- [Enhancing accessibility with our read out loud feature](#text-to-voice-functionality)
- [AI premium suite](#ai-premium-suite)
- [AI glossary generator](#ai-glossary-generator)
- [How to write GenAI friendly content](#how-to-write-genai-friendly-content)
- [Prompt engineering tips](#prompt-engineering-tips)
- [File management](#drive)
- [Adding folders and files](#adding-folders-and-files)
- [Folder actions in Drive](#folder-actions-in-drive)
- [File actions in Drive](#file-actions-in-drive)
- [All files overview](#all-content-overview)
- [Recent, Starred, and Recycle bin files](#recycle-bin-recent-and-starred-files)
- [Workflow designer](#workflow-designer)
- [Managing workflow status](#managing-workflow-status)
- [Workflow assignment](#workflow-assignment)
- [Templates](#article-templates)
- [Variables](#variables)
- [Snippet](#snippets)
- [Glossary](#glossary)
- [Adding glossary terms](#adding-glossary-term)
- [Inserting glossary term in an article](#adding-glossary-term-in-articles)
- [Managing glossary terms](#editing-and-deleting-glossary-term)
- [Managing the glossary landing page](#glossary-overview-page)
- [Feedback manager](#feedback-manager-overview)
- [Custom pages](#custom-pages)
- [Tags](#tags)
- [Manage tags page overview](#tag-manager-overview-page)
- [Adding a new tag](#adding-a-new-tag)
- [Tag groups page overview](#tag-groups-overview)
- [Manage tag dependencies](#tag-dependency-viewer)
- [Find and replace](#find-and-replace)
- [SEO descriptions](#seo-descriptions)
- [Exporting your Document360 project as a ZIP file](#export-documentation-as-zip)
- [Importing a Document360 project ZIP file](#import-a-documentation-project)
- [Migrating documentation from other platforms](#migrating-documentation-from-another-knowledge-base-platform)
- [Designing a PDF template](#pdf-design-templates)
- [Compiling content for PDF](#compliling-content-for-pdf)
- [Analytics](#analytics)
- [Articles analytics](#articles-analytics)
- [Eddy AI search analytics](#eddy-ai-search-analytics)
- [Search analytics](#analytics-search)
- [Reader analytics](#reader-analytics)
- [Team accounts analytics](#analytics-team-accounts)
- [Feedback analytics](#feedback)
- [Links status analytics](#links-status)
- [Ticket deflector analytics](#ticket-deflector-overview)
- [Managing API documentation](#manage-api-documentation)
- [Edit, Clone, and Delete widget](#edit-clone-and-delete)
- [Managing and customizing the Knowledge base widget](#managing-and-customizing-the-knowledge-base-widget)
- [URL Mapping](#url-mapping)
- [Customizing the Knowledge base widget using Custom CSS/JavaScript](#customizing-the-kb-widget-using-custom-css-javascript)
- [FAQ - Knowledge base widget](#faq-knowledge-base-widget)
- [Knowledge base site 2.0](#knowledge-base-site-20)
- [Customize site](#customize-site)
- [KB site 2.0 migration](#kb-site-20-migration)
- [Web Content Accessibility Guidelines (WCAG)](#web-content-accessibility-guidelines-wcag)
- [Header - Primary navigation](#header-primary-navigation)
- [Header - Secondary navigation](#header-secondary-navigation)
- [Footer](#footer-navigation)
- [Custom footer](#custom-footer)
- [RSS Feeds](#rss-feeds)
- [Main pages](#main-pages)
- [Hero section](#hero-section)
- [Rich text blocks](#text-block)
- [Multicolumn card section](#text-columns-block)
- [Image with text block](#image-and-text)
- [Custom code section](#html-block)
- [Knowledge base categories block](#knowledge-base-categories)
- [Widgets block](#widgets)
- [Error pages](#error-pages)
- [404 page](#404-page)
- [Access denied page](#access-denied-page)
- [Unauthorized page](#unauthorized-page)
- [IP restriction page](#ip-restriction-page)
- [Custom CSS & JavaScript](#custom-css-javascript)
- [CSS Snippets](#css-snippets)
- [Callout styles](#callout-styles)
- [Body font style](#body-font-style)
- [Image alignment](#image-alignment)
- [Header font style](#header-font-style)
- [Table style](#table-style)
- [Article redirect rule](#article-redirect-rules)
- [Article settings & SEO](#configuring-the-article-settings)
- [Article header](#article-header)
- [Site header-What's new](#document-header)
- [Follow articles and categories](#follow-articles-and-categories)
- [Search in Knowledge base site](#search-in-knowledge-base-site)
- [Liking or disliking an article](#liking-or-disliking-an-article)
- [Smart bars](#smart-bar)
- [Cookie consent](#cookie-consent)
- [Accessing the ticket deflectors in portal](#accessing-the-ticket-deflectors)
- [Adding a new ticket deflector](#adding-a-new-ticket-deflector)
- [Integrations in Document360](#integrations-getting-started)
- [Code inclusion and exclusion conditions](#advanced-insertion-rules-in-integration)
- [LiveChat](#livechat)
- [Olark](#olark)
- [Freshchat](#freshchat)
- [Crisp](#crisp)
- [Chatra](#chatra)
- [Doorbell](#door-bell)
- [Gorgias](#gorgias)
- [Belco](#belco)
- [Sunshine Conversations](#sunshine)
- [Kommunicate](#kommunicate)
- [Google Analytics](#google-analytics-integration)
- [Google Analytics (GA4)](#google-analytics-new)
- [Google Tag Manager](#google-tag-manager)
- [Heap](#heap)
- [Segment](#segment-integration)
- [Hotjar](#hotjar)
- [Amplitude](#amplitude)
- [FullStory](#fullstory)
- [Mixpanel](#mixpanel)
- [VWO](#vwo)
- [Freshmarketer](#freshmarketer)
- [ZOHO PageSense](#zoho-page-sense)
- [GoSquared](#gosquared)
- [Commento](#commento)
- [Disqus](#disqus)
- [Document360 Extensions - Getting started](#all-extensions)
- [Freshdesk](#freshdesk)
- [Freshservice](#freshservice)
- [Zendesk](#zendesk)
- [Intercom](#intercom-integration)
- [Salesforce](#salesforce)
- [Cases page](#cases-page)
- [Slack](#slack)
- [Microsoft Teams](#microsoft-teams)
- [Drift](#drift)
- [Zapier - Setup guide](#zapier-setup-guide)
- [Integrating Google Docs with Document360](#google-docs-document360-integration)
- [Integrating Google Sheets with Document360](#document360-with-google-sheets-integration)
- [Integrating Document360 with Google Drive](#google-drive-document360)
- [Integrating Trello with Document360](#document360-with-trello-integration)
- [Integrating GitHub with Document360](#github-document360)
- [Integrating Confluence Server with Document360](#confluence-document360)
- [Integrating Zoho CRM with Document360](#zoho-crm-document360)
- [Integrating Pipedrive with Document360](#pipedrive-document360)
- [Integrating Hubspot with Document360](#hubspot-document360)
- [Integrating Asana with Document360](#asana-document360)
- [Integrating Monday.com with Document360](#mondaycom-document360)
- [Integrating Typeform with Document360](#typeform-document360)
- [Integrating Gmail with Document360](#document360-gmail)
- [Integrating Mailchimp with Document360](#document360-mailchimp)
- [Make - Setup guide](#make-setup-guide)
- [Integrating Asana with Document360](#asana-and-document360-integration)
- [Integrating Monday.com with Document360](#monday-document360-integration)
- [Integrating Typeform with Document360](#typeform-and-document360-integration)
- [Integrating Google Docs with Document360](#google-docs-and-document360-integration)
- [Integrating Jira with Document360](#jira-and-document360-integration)
- [Chrome](#chrome-extension)
- [Crowdin](#crowdin)
- [Phrase](#phrase)
- [General project settings](#general-project-settings)
- [Team auditing](#team-auditing)
- [Localization - Getting started](#localization-getting-started)
- [Setting up a Multi-lingual knowledge base](#setting-up-a-multi-lingual-knowledge-base)
- [Localization variables](#localization-variables)
- [Workspaces](#workspaces)
- [Backup and restore](#backup-restore)
- [Notifications](#notifications)
- [Webhook notification channel](#webhook-notification-channel)
- [Slack notification channel](#slack-notification-channel)
- [Microsoft Teams notification channel](#microsoft-teams-notification-channel)
- [SMTP notification channel](#smtp-email-notification-channel)
- [Notification mapping](#notification-mapping)
- [Notification history](#notification-history)
- [Email domain](#send-notifications-from-custom-email-domain)
- [How to use Postman?](#how-to-use-postman)
- [How to use Swagger?](#how-to-use-swagger)
- [Portal search](#full-portal-search)
- [Article-portal search](#article-full-portal-search)
- [Drive-portal search](#drive-full-portal-search)
- [Users & groups-portal search](#users-groups-full-portal-search)
- [Tags-portal search](#tags-full-portal-search)
- [Settings-portal search](#settings-full-portal-search)
- [Custom domain mapping](#custom-domain-mapping)
- [Hosting Document360 on a sub-directory](#document360-on-a-sub-folder)
- [Nginx server - Subfolder hosting](#nginx-server)
- [ASP.NET Core server](#aspnet-core-server)
- [Microsoft - IIS server](#microsoft-iis-server)
- [Apache HTTP server](#apache-http-server)
- [Readers self registration](#reader-self-registration)
- [Managing reviewer accounts](#managing-reviewer-accounts)
- [Account locked](#account-locked)
- [Block inheritance](#block-inheritance)
- [IP restriction](#ip-restriction)
- [Single Sign-On (SSO)](#single-sign-on-sso)
- [Login using SSO - Knowledge base portal](#login-using-sso-knowledge-base-portal)
- [Login using SSO - Knowledge base site](#login-using-sso-knowledge-base-site)
- [Inviting or Adding SSO users](#inviting-or-adding-sso-users)
- [Mapping an existing SSO configuration to other projects](#mapping-an-existing-sso-configuration-to-other-projects)
- [Disable Document360 login page](#disable-document360-login-page)
- [Auto assign reader group](#auto-assign-reader-group)
- [Convert to SSO account](#convert-to-sso-account)
- [Sign out idle SSO team account](#team-account-idle-timeout)
- [SAML](#saml)
- [SAML SSO with Okta](#saml-sso-with-okta)
- [SAML SSO with Entra](#saml-sso-with-entra)
- [SAML SSO with Google](#google-sso-saml-configuration)
- [SAML SSO with OneLogin](#saml-sso-with-onelogin)
- [SAML SSO with ADFS](#saml-sso-with-adfs)
- [SAML SSO with other configurations](#saml-sso-with-other-configurations)
- [Identity Provider (IdP) initiated sign in](#idp-initiated-login)
- [Removing a configured SAML SSO](#removing-a-configured-saml-sso)
- [OpenID](#openid)
- [Okta with OpenID SSO](#okta-with-openid-sso)
- [Auth0 with OpenID SSO](#auth0-with-openid-sso)
- [ADFS with OpenID SSO](#adfs-with-openid-sso)
- [Other configurations with OpenID SSO](#other-configurations-with-openid-sso)
- [Removing a configured OpenID SSO](#removing-a-configured-openid-sso)
- [Setting up JWT SSO](#configuring-the-jwt-sso)
- [JWT reader groups](#jwt-reader-groups)
- [How to enlarge the pdf preview in the article?](#how-to-enlarge-the-pdf-preview-in-the-article)
- [How to change the color of the hyperlinks in Dark mode?](#how-to-change-the-color-of-the-hyperlinks-in-dark-mode)
- [How to change the highlighted search result color in articles?](#how-to-change-the-highlighted-search-result-color-in-articles)
- [How to hide the project's workspace dropdown in the Knowledge base site?](#how-to-hide-the-project-versions-dropdown-in-the-knowledge-base-site)
- [How to add a vertical scrollbar to the code blocks?](#how-to-add-a-vertical-scrollbar-to-the-code-blocks)
- [How to set the default height and width of the embedded PDF?](#how-to-set-the-default-height-and-width-of-the-embedded-pdf)
- [How to make the table border bold in knowledge base?](#how-to-make-the-table-border-bold-in-knowledge-base)
- [How to vertically align table contents at the top in the Knowledge base?](#how-to-vertically-align-table-contents-at-the-top-in-the-knowledge-base)
- [How to restrict the readers from copying the content?](#how-to-restrict-the-readers-from-copying-the-content)
- [How to keep dark mode for the Knowledge base site by default?](#how-to-keep-dark-mode-for-the-knowledge-base-site-by-default)
- [How to center align the text in Markdown?](#how-to-center-align-the-text-in-markdown)
- [How to change the color of the text in Markdown?](#how-to-change-the-color-of-the-text-in-markdown)
- [How to change the language name text in code blocks?](#how-to-change-the-language-name-text-in-code-blocks)
- [How to change the callouts color in dark mode?](#how-to-change-the-callouts-color-in-dark-mode)
- [How to center align the heading in the articles?](#how-to-center-align-the-heading-in-the-articles)
- [How to change the color of the table header?](#how-to-change-the-color-of-the-table-header)
- [How to add accordion in Markdown?](#how-to-add-accordion-in-markdown)
- [How to add extra space in Markdown?](#how-to-add-extra-space-in-markdown)
- [How to align the image in Markdown?](#how-to-align-the-image-in-markdown)
- [How to add a background image for a text content?](#how-to-add-a-background-image-for-a-text-content)
- [How to change the color of the table of contents?](#how-to-change-the-color-of-the-table-of-contents)
- [How to sort the contents of a table?](#how-to-sort-the-contents-of-a-table)
- [How to customize the hyperlink size?](#how-to-customize-the-hyperlink)
- [How to make all links open in new tab?](#how-to-make-all-links-open-in-new-tab)
- [How to set a default featured image in knowledge base?](#how-to-set-a-default-featured-image-in-knowledge-base)
- [How to add shadows to an image in Markdown?](#how-to-add-shadows-to-an-image-in-markdown)
- [How to add borders to an image in Markdown?](#how-to-add-borders-to-an-image-in-markdown)
- [How to embed YouTube Shorts?](#embed-youtube-shorts)
- [How to embed a Loom video?](#how-to-embed-loom-video)
- [How to embed an Excel file?](#how-to-embed-an-excel-file)
- [How to change the color of Feedback buttons?](#how-to-change-the-color-of-feedback-buttons)
- [How to hide footer in mobile view?](#how-to-hide-footer-in-mobile-view)
- [How to change the hover color of the header options?](#how-to-change-the-hover-color-of-the-header-options)
- [How to move the related articles above the feedback section?](#how-to-move-the-related-articles-above-the-feedback-section)
- [How to hide the change password option for readers?](#how-to-hide-the-change-password-option-for-readers)
- [How to hide the category manager?](#how-to-hide-the-category-manager)
- [How to configure a custom font in the knowledge base?](#how-to-configure-a-custom-font-in-the-knowledge-base)
- [How to hide the left navigation bar in the knowledge base site?](#how-to-hide-the-left-navigation-bar-in-knowledge-base-site)
- [Plans and pricing](#plans-and-pricing)
- [Upgrading your subscription plan](#upgrading-your-plan)
- [Downgrading your subscription plan](#downgrading-your-plan)
- [Purchasing add-ons](#add-ons)
- [Upgrading from trial version](#upgrading-from-trial-version)
- [Changing payment information](#changing-payment-information)
- [February 2025 - 11.1.2](#february-2025-1112)
- [January 2025 - 11.01.1](#january-2025-1111)
- [December 2024 - 10.12.1](#december-2024-10121)
- [November 2024 - 10.11.1](#november-2024-10111)
- [October 2024 - 10.10.1](#october-2024-10101)
- [September 2024 - 10.9.1](#september-2024-1091)
- [September 2024 - 10.8.2](#september-2024-1082)
- [August 2024 - 10.8.1](#august-2024-1081)
- [July 2024 - 10.7.1](#july-2024-1071)
- [July 2024 - 10.6.2](#july-2024-1062)
- [June 2024 - 10.6.1](#june-2024-1061)
- [June 2024 - 10.5.2](#june-2024-1052)
- [May 2024 - 10.5.1](#may-2024-1051)
- [May 2024 - 10.4.2](#may-2024-1042)
- [April 2024 - 10.4.1](#1041-release-note)
- [April 2024 - Minor release](#april-2024-minor-release)
- [March 2024](#march-2024)
- [February 2024](#february-2024)
- [January 2024](#january-2024)
- [December 2023](#december-2023)
- [November 2023](#november-2023)
- [August 2023](#august-3)
- [July 2023](#july-2)
- [June 2023](#june-3)
- [May 2023](#may-1)
- [April 2023](#april-3)
- [March 2023](#march-4)
- [February 2023](#february-3)
- [January 2023](#january-2)
- [December 2022](#december-2022-release-note)
- [November 2022](#november-2022-release-note)
- [October 2022](#october-2022-release-note)
- [September 2022](#september-2022-release-note)
- [August 2022](#august-2022-release-note)
- [July 2022](#july-2022-release-note)
- [June 2022](#june-2022-release-notes)
- [May 2022](#may-2022-release-note)
- [April 2022](#april-2022-release-note)
- [March 2022](#march-2022-release-note)
- [February 2022](#february-2022-release-note)
- [January 2022](#january-2022-release-note)
- [December 2021](#december-2021-release-note)
- [November 2021](#november-2021-release-note)
- [October 2021](#october-2021-release-note)
- [September 2021](#september-2021-release-note)
- [August 2021](#august-2021-release-notes)
- [July 2021](#july-2021-release-note)
- [June 2021](#june-2021-release-note)
- [May 2021](#may-2021-release-note)
- [April 2021](#april-2021-release-note)
- [March 2021](#march-2021-release-note)
- [February 2021](#february-2021-release-note)
- [January 2021](#january-2021-release-note)
- [November 2020](#november-2020-release-note)
- [October 2020](#october-2020-release-note)
- [August 2020](#august-2020-release-note)
- [June 2020](#june-2020-release-note)
- [May 2020](#may-2020-release-note)
- [April 2020](#april-2020-release-note)
- [March 2020](#march-2020-release-note)
- [February 2020](#february-2020-release-note)
- [January 2020](#january-2020)
- [December 2019](#december)
- [November 2019](#november)
- [October 2019](#october)
- [September 2019](#september-2019)
- [August 2019](#august)
- [July 2019](#july)
- [June 2019](#june)
- [May 2019](#may-2019)
- [April 2019](#april-2019)
- [March 2019](#march)
- [February 2019](#february)
- [January 2019](#january-2019)
- [Support ticket](#support-ticket)
- [Generating a HAR file](#document360-support-generating-a-har-file)

---

<a id="document360-getting-started"></a>

## What is Document360?

Document360 is a knowledge management platform for creating self-service public, private, or mixed access knowledge bases.

When using Document360, you'll interact with several key interfaces:

* #### [My Projects](/help/docs/document360-getting-started#my-projects)
* #### [Knowledge base portal](/help/docs/document360-getting-started#knowledge-base-portal)
* #### [Knowledge base site](/help/docs/document360-getting-started#knowledge-base-site)
* #### [Document360 AI - Eddy AI](/help/docs/ai-features)
* #### [Resources](/help/docs/document360-getting-started#other-resources)

---

## My projects

The **project dashboard** is the first thing you see when logging in to [**Document360**](https://portal.document360.io). It shows all projects you own, projects associated with team accounts, and projects you're a reader for. Each project has a visibility tag indicating its type (public, private, or mixed).

![1_Screenshot-My_projects](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-My_projects.png "My-Projects.png")

---

## Knowledge base portal

The **Knowledge base portal** is where you:

* **Create** categories, articles, and templates
* **Manage** files, team accounts, and readers
* **Set up** branding, domain, security, and more for the knowledge base site

  ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-What_is_Document360.png)

Here are the elements you'll find on the knowledge base portal:

1. Dashboard
2. Documentation
3. API Documentation
4. Analytics
5. Widgets
6. Drive
7. Settings
8. Search
9. Open Site

> NOTE
>
> Anything created or configured on the Knowledge base portal affects what end-users see on the Knowledge base site.

### 1. Dashboard

This page provides an overview of your project and serves as a hub for contributors. In the **Overview** section, team accounts can access information such as created articles, published articles, drafts, and performance insights (views, reads, likes, and dislikes). Use the filter option to select the time frame. You can also view project-related information including **Recently seen**, **Team accounts**, **Readers**, **Drive capacity**, **Broken links**, **No result searches** and **Last backed up** date.

![3_Screenshot-Knowledge_base_portal_dashboard_overview](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Knowledge_base_portal_dashboard_overview.png)

In the **My contribution** section, users can view their contributions to the project, article performance metrics, workflow assignments, review reminders, feedback, and broken links.

![Document360 dashboard showing article metrics summary with number of articles created, published or drafted, and an area to display assigned tasks.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Knowledge_base_portal_dashboard_my_contribution.png)

---

### 2. Documentation

The **Documentation** page is where you create and maintain the tree-view folder structure of categories that keeps your articles organized. Start a knowledge base by creating a category, then populate it with subcategories and articles.

Drag and drop categories and articles to reorder, hide, rename, and delete them using the More options menu that appears when you hover over any item in the Category manager (left navigation pane).

![Document360 user interface showing navigation menus for managing articles, workflow assignments, starred items, recycle bin, site builder, content tools, and categories/articles hierarchy.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Knowledge_base_portal_documentation_view.png)

#### a. All articles

The **All articles** section allows you to perform bulk operations (publish, hide, move, delete, etc.) on multiple articles at once, saving time compared to performing these actions individually.

![Document360's 'All articles' interface showing a list of articles with editing options like publish, hide, move, delete, review reminder, and live status, as well as features for reusing content through templates, variables, snippets, and a glossary.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Knowledge_base_portal_documentation_view_all_articles.png)

#### b. Workflow assignments

The Workflow assignments section shows what the team is currently working on and any recently published articles.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Knowledge_base_portal_documentation_view_workflow_assignments.png)

Articles assigned to you appear on this page. You can filter articles by workflow status: **Draft**, **In review**, or **Published**. Articles with missed review due dates appear under the **Overdue** category.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7.1_Screenshot-Knowledge_base_portal_workflow_assignments_page.png)

#### c. Starred

The Starred section contains articles you've marked as favorites for quick access.

![Document360's 'Starred' interface showing a list of articles with the respective tags and article status, along with an arrow pointing at 'Starred' on the left navigation panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Knowledge_base_portal_documentation_view_starred.png)

#### d. Recycle bin

The Recycle bin section includes articles and categories deleted in the past 30 days. You can restore deleted items within this timeframe.

![Document360's 'Recycle bin' interface showing an empty recycle bin, along with an arrow pointing at 'Recycle bin' on the left navigation panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Knowledge_base_portal_documentation_view_recycle_bin.png)

#### e. Site builder

Personalize the look and feel of your knowledge base site from the **Site builder** section.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Knowledge_base_portal_documentation_view_site_builder.png)

Choose your logo and icon. Customize brand colors, fonts, and styling from this section.

#### f. Content tools

The **Content tools** contain everything needed to manage article and project content.

![5_Screenshot-Knowledge_base_portal_Content_tools](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/11_Screenshot-Knowledge_base_portal_documentation_view_content_tools.png)

Manage these features from this menu:

* **Content reuse** - Variables, snippets, templates, and glossary
* **Import and Export** - Project import/export activities, PDF export, and migration from other tools
* **Content essentials** - Project-level find and replace, review reminders, tags, and SEO descriptions
* **Feedback manager** - View and respond to article and search feedback
* **Workflow designer** - Create workflow statuses and sequences

#### g. Categories & Articles (Category manager)

Writing and publishing articles in Document360 is simple: pick your category, create an article (title and slug), add SEO details, and publish.

When you update or edit an article, Document360 creates a new revision without affecting the live workspace.

![12_Screenshot-Knowledge_base_portal_documentation_view_categories_and_articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/12_Screenshot-Knowledge_base_portal_documentation_view_categories_and_articles.png)

Make changes and republish when ready. Identify articles using status indicators (yellow dot). Document360 maintains all workspaces to check differences.

---

### 3. API documentation

Create and manage API references with Document360's API documentation feature. This allows you to create high-quality API documentation that helps users understand and consume your APIs.

![13_Screenshot-Knowledge_base_portal_api_documentation](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/13_Screenshot-Knowledge_base_portal_api_documentation.png)

The API module includes the **Try it!** feature, allowing users to test API endpoints within the knowledge base site. Create dedicated versions of your API documentation. Upload API references as URLs or JSON/YAML files through an intuitive interface. After uploading the OpenAPI definition, interactive API endpoint articles are created in the portal. End users can access the **Try it!** option with available endpoints, parameters, and responses.

---

### 4. Analytics

Document360 includes an **Analytics** menu to help understand end-user engagement with your knowledge base.

![12_Screenshot-Knowledge_base_portal_Analytics](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/14_Screenshot-Knowledge_base_portal_analytics.png)

Track these metrics and modules with the Analytics tool:

* **Articles**
* **Eddy AI**
* **Search**
* **Team accounts**
* **Feedback**
* **Links status**
* **Page not found**
* **Ticket deflector**

---

### 5. Widget

The Knowledge base widget (formerly *Knowledge base assistant* or *In-app assistant*) helps readers find answers without leaving your site or application.

![8_Screenshot-Knowledge_base_portal_Widget](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/15_Screenshot-Knowledge_base_portal_widgets.png)

Update these widget settings from this menu:

* **Installation & setup**
* **Custom CSS**
* **Custom JavaScript**
* **URL mapping**

---

### 6. Drive

Centralized cloud storage for Document360 projects that stores and lets team members manage all knowledge base artifacts (files). If you've used Google Drive or OneDrive, getting accustomed to Document360 Drive should be straightforward. Access your Drive by clicking the Drive icon in the left menu.

![7_Screenshot-Knowledge_base_portal_Drive](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/16_Screenshot-Knowledge_base_portal_drive.png)

---

### 7. Settings

Set and configure all aspects of the project and knowledge base in **Project settings**: invite team members, edit notification settings, configure domains, set up article redirects, and more.

![9_Screenshot-Knowledge_base_portal_Settings](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/17_Screenshot-Knowledge_base_portal_settings.png)

Features are organized under these classifications in the Settings menu:

* **Knowledge base portal**
* **Knowledge base site**
* **Users & Security**
* **AI Features**

---

### 8. Search

Search the entire project content from a dedicated space on the Knowledge base portal. Perform combined searches across all workspaces and languages simultaneously. The search bar is available at the top of all modules and pages.

![10_Screenshot-Knowledge_base_portal_Search](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/18_Screenshot-Knowledge_base_portal_search.png)

The search engine works like other portal search functions. Type keywords and narrow results using filters such as workspace, language, visibility, tags, and date range. Preview articles/categories, then navigate to the article in the Editor.

![11_Screenshot-Knowledge_base_portal_Search_results](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/19_Screenshot-Knowledge_base_portal_search_bar_dropdown.png)

Since search covers the entire project, it includes files. Switch between article and Drive search using tabs below the search bar.

---

### 9. Open site

The Open site action navigates to and views the Knowledge base site. Clicking the icon takes you to the Knowledge base site of the workspace currently open in your portal. If you're in the API documentation workspace, you'll go to the API documentation home page. If no home page exists, you'll be directed to the first article or category page.

---

## Knowledge base site

The Knowledge base site is the website end-users access to read articles and find helpful answers.

Set your knowledge base access to public, private, or mixed. **Public** means anyone on the internet can access it. **Private** restricts access through login screens. **Mixed** combines public and private elements.

![14_Screenshot-Knowledge_base_site_overview](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/20_Screenshot-Knowledge_base_site_preview.png)

---

## Document360 AI - Eddy AI

Eddy AI is an AI writing assistant integrated into Document360. It helps with **writing articles**, **generating SEO descriptions**, and **recommending article tags**, **titles**, and **related articles**. Eddy AI is also available on the knowledge base site, helping readers find information faster through **assistive search** and the **article summarizer**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/24_Screenshot-Eddy_settings_aifeatures_eddy.png)

---

## Other Resources

### Got Feedback?

We maintain a public [**product feedback portal**](https://feedback.document360.com/) for customer feedback. It also features our roadmap.

![27_Screenshot-An_overview_of_project_feedback](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/21_Screenshot-User_feedback.png)

### Quick start (Feature explorer)

The **Quick start** is a learning wizard available on all Document360 trial projects. It helps track your progress as you learn about various features. Each time you use or explore a new part of the product, the Feature Explorer automatically updates your progress.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenShot-What_is_Document360.png)

---

### Need Help?

If you need help or have questions, contact us. Click your profile avatar to:

![21_Screenshot-My_projects_Help_module](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/23_Screenshot-Resources_need_help.png)

* Send an **in-app chat**
* Email [**support@document360.com**](mailto:support@document360.com)
* Read our [**documentation**](https://docs.document360.com/docs)
* Watch [**tutorial videos**](https://document360.com/tutorial-videos/)

---

### FAQs

#### **What is Document360?**

Document360 is a knowledge management platform that allows you to create and curate self-service public, private, or mixed access knowledge bases.

#### **What can I do in the Knowledge base portal?**

Create categories, articles, and templates. Manage files, team accounts, and readers. Set up branding, domain, and security for your Knowledge base site.

#### **What features are available in the Analytics section?**

Track metrics such as articles, user engagement, search performance, team accounts, feedback, and link status.

#### **Can I restore deleted articles in Document360?**

Yes, restore articles and categories deleted within the past 30 days from the Recycle bin section.

#### **Is there an AI feature in Document360?**

Yes, Document360 includes Eddy AI, an AI writing assistant that helps with writing articles, generating SEO descriptions, and assisting readers in finding information.

#### **What is a knowledge base?**

A centralized repository of information designed to provide answers, guidance, and support. Contains structured content like articles, FAQs, guides, and documentation. Allows users to search and access information to solve problems or learn about products, services, or topics. Commonly used in customer support, internal training, and product documentation.

#### Why does it show 'Maintenance' on the top navigation bar in the knowledge base portal?

The **Maintenance** badge indicates scheduled maintenance of the Knowledge base portal. The portal will be unavailable during scheduled times, but the Knowledge base site remains accessible.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/26_ScreenShot-What_is_Document360.png)

For assistance, contact the Document360 support team: [Contact Document360 Support](https://document360.com/support/).

Organizes related articles under a common theme in the knowledge base.

A written document on a specific topic in your knowledge base, serving as a unit of organized information.

Pre-designed article structures that team accounts can use to create consistent articles.

The platform where project members manage and create content. Allows users to create categories, articles, and templates; manage files, team accounts, and readers; and configure site settings.

The public-facing website where end-users access articles and find answers.

Organizes related articles under a common theme in the knowledge base.

A secondary category used to organize groups of related articles. Acts as folders within primary categories.

A written document on a specific topic in your knowledge base.

A tool for managing article-category relations.

Optimizing content to improve visibility in search results. SEO elements can be added for each article through settings.

Creating a new version of an article containing original content for revision.

View and manage article revision history, workflow updates, and compare versions.

Custom styling code used to modify webpage appearance.

A tool for drafting and formatting content. Document360 offers Markdown, WYSIWYG, and Advanced WYSIWYG editors.

<a id="sign-up-to-document-360"></a>

## Sign up to Document360

Create a Document360 account before using the platform. Navigate to the [**signup page**](https://document360.com/signup/).

---

## **Signing Up to Document360**

### **Navigate to the Signup page**

1. On the signup page, provide basic details:

   * First Name
   * Last Name
   * Work Email
   * Job Title
   * Implementation timeline
   * Phone Number
2. Click the **Start Free Trial** button.

![Exploring the onboarding experience while signing up the Document360](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Initial_step_of_onboarding.png)

### **Email verification**

3. You'll receive a 6-digit verification code in your email. Enter this code on the verification page.
4. Click **Verify.**

> NOTE
>
> Entering the wrong verification code five times locks your account activation. Contact Document360 support for help.

### **Set your account password**

5. After verifying your email, create a password for your Document360 account. Requirements:

   * At least 8 characters long
   * Includes at least one number
   * Includes at least one special character
   * Includes both uppercase and lowercase letters
6. Re-enter your password to confirm, then click **Get Started**.

### **Choose your use case**

7. Select your primary use case by clicking **Get started.**

|  |  |
| --- | --- |
| **Knowledge base platform** | Create a centralized hub for team knowledge and resources. Helps teams find answers quickly and enhances customer self-service. |
| **Software documentation/Technical documentation** | Organize and maintain software or technical documentation. Helps document product features, APIs, release notes, and more. |
| **SOP documentation** | Create detailed SOPs for consistent team procedures. Ensures everyone follows the same processes and reduces errors. |
| **User manual** | Develop comprehensive user manuals with step-by-step instructions and troubleshooting tips. Reduces support queries. |
| **API Documentation** | Document API endpoints, request/response formats, authentication methods, and examples. Ensures developers understand integration. |
| **Others** | Choose if your use case doesn't fit predefined categories. Customize based on specific organizational needs. |

### **Select a Template**

8. Select the type of content you'll create. Pick up to two templates.

> NOTE
>
> Selected templates are embedded within your project during creation.

**Knowledge base platform templates**

Choose any two templates from:

|  |  |
| --- | --- |
| **Getting started guides** | Help new users understand and begin using your product with clear instructions. Ensures smooth onboarding. |
| **How-to guides** | Provide detailed instructions for specific tasks. Enables users to fully utilize product features. |
| **FAQs** | Address common questions at any stage of the user journey. Helps users find quick answers. |
| **Policy & procedures** | Outline essential organizational protocols. Helps users understand company guidelines. |

**Software/Technical documentation templates**

Choose any two templates from:

|  |  |
| --- | --- |
| **Release notes** | Keep users informed about updates, new features, bug fixes, and improvements with each release. |
| **Software Design Documentation (SDD)** | Outline software architecture and design, including diagrams and specifications. |
| **Software Requirement Documentation** | Describe software purpose, functionalities, and environment. Ensures development aligns with goals. |
| **Product Requirement Documentation (PRD)** | Define product purpose, value, and functionalities. Meets user needs and business objectives. |
| **Process documentation** | Detailed steps and procedures involved in software development. Standardizes workflows. |
| **User guide** | Comprehensive instructions on using your product. Covers all features and functionalities. |

**SOP documentation templates**

Choose any two templates from:

|  |  |
| --- | --- |
| **Compliance policies and procedures** | Ensure organizational compliance with regulatory requirements. |
| **Operation SOP** | Standardize operational procedures across your organization. |

**User manual templates**

Choose any two templates from:

|  |  |
| --- | --- |
| **Installation manual** | Provides setup information including product overview, specifications, and assembly instructions. |
| **Instruction manual** | Offers step-by-step assembly and usage instructions with diagrams and safety warnings. |
| **Maintenance manual** | Provide detailed instructions for regular upkeep, troubleshooting, and repair procedures. |
| **Training manual** | Provides comprehensive guidance on installation, operation, and troubleshooting. |
| **Operations manual** | Provide detailed instructions for daily maintenance and troubleshooting. |

### **Personalize your Knowledge base**

9. Enter your preferred website URL. Skip this step to default to the domain linked to your registration email.

### **Brand guidelines**

10. Your project name, default language, branding logo, and brand colors are automatically set based on your provided URL. Edit fields if needed.

    Your browser's language settings determine the default language. English is selected if other languages don't support your browser's language.

> NOTE
>
> * Spanish or Brazilian Portuguese as default language sets the portal language accordingly. Otherwise, English is default.
> * Branding logo and colors are extracted from your website. Skipping applies Document360's default logo and colors.

11. Preview your Knowledge base on the right side of the screen.

### **Set documentation privacy**

12. Choose privacy settings for your site:

    * **Private**: Restrict access so only team accounts can view content.
    * **Public**: Make accessible to everyone, including external users.
    * **Mixed**: Combine private and public access.
13. Click **Next** to proceed.

### **Access the Document360 Knowledge base portal**

Enter the portal after setup completion. Find pre-loaded articles based on your selected use case and templates.

> NOTE
>
> Articles are tailored to your selected use case and templates.

![Exploring the onboarding experience while signing up the Document360](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Final_onboarding_process.gif)

---

### FAQs

**Does Document360 support different languages in the onboarding flow?**

Yes, multi-lingual support includes English, Spanish, Brazilian Portuguese, German, and Swedish. Portal language support is currently limited to English, Spanish, and Brazilian Portuguese.

**Do I need to pay to create a Document360 account?**

No payment required. Get a 14-day trial account. Upgrade to continue using beyond trial.

**What plans can I upgrade to?**

Four plans: Free, Professional, Business, and Enterprise. Learn about pricing and features [**here**](https://document360.com/pricing/).

**I haven't received the verification code. How do I continue?**

Click **Resend Code** on the **Email verification** page. Check spam/junk folder. Contact Document360 support if still missing.

**I have an existing knowledge base. How should I migrate?**

Fill out the migration request form before signing up. Migration experts will contact you. If you have a trial account, navigate to **Documentation** > **Content tools** > **Import & Export** > **Migrate content**. Follow on-screen instructions.

**My Document360 trial period ended. Can I still access my data?**

No access to created content after trial ends. Upgrade to a subscription plan to regain access.

**What happens if I don't complete the password setup during signup?**

The system recognizes your previous session and redirects you to the password creation screen.

<a id="system-and-browser-requirements"></a>

## System and browser requirements

## Recommended

System and browser requirements for efficient Document360 Knowledge base portal function.

> NOTE
>
> Access the portal and site with earlier browser versions, but advanced features may perform poorly.

---

### Operating System and Hardware

Ensure your computer has one of these operating systems:

| # | **Operating system requirements** |
| --- | --- |
| 1 | **Windows 7.0** or **higher** |
| 2 | **OSX Mavericks** or **higher** |
| 3 | **Linux** |
| 4 | **Android 5.0** or **higher** |
| 5 | **iOS 12.0** or **higher** |

| # | **Hardware requirements** |
| --- | --- |
| 1 | **2 core CPU** or **higher** |
| 2 | **4 GB RAM** or **higher** |

---

### Web browser requirements

Document360 works well on latest versions of these browsers:

| # | **Supported web browsers** | **Knowledge base portal** | **Knowledge base site 1.0** | **Knowledge base site 2.0** |
| --- | --- | --- | --- | --- |
| 1 | **Google Chrome** version 91.0.4472 or higher | Yes | Yes | Yes |
| 2 | **Firefox** version 79.0 or higher | Yes | Yes | Yes |
| 3 | **Safari** version 13.1.2 or higher | Yes | Yes | Yes |
| 4 | **Microsoft Edge** version 88 or higher | Yes | Yes | Yes |
| 5 | **Internet Explorer** version 11 | No | No | No |
|  | Other web browsers |  |  |  |

#### Browser features

Ensure these browser attributes:

* **JavaScript** must be **enabled**

  > Limited access when disabled
* **Cookies** must be **enabled**
* **Session Storage** must be **enabled**
* **Local Storage** must be **enabled**
* **IndexedDB** must be **enabled**
* **HTTPS - TLS v1.2** or **higher**

---

### Support and feedback

Contact [support@document360.com](mailto:support@document360.com) for difficulties or unspecified issues.

## Troubleshooting

If you encounter issues logging into the Knowledge base portal, refer to common errors and solutions:

### reCAPTCHA Error: "Having trouble?"

**Error**: "Having trouble?" message while interacting with reCAPTCHA verification. Caused by browser restrictions, VPN interference, or network blocks.

![Login form displaying an error message from Cloudflare regarding login issues.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Troubleshooting_srecaptcha_error.png)

**Steps to resolve**:

1. Try accessing in a different browser. If successful, disable extensions in affected browser.
2. Disconnect VPN and attempt login again.

If issue persists:

* Generate HAR file following [these steps](https://docs.document360.com/docs/document360-support-generating-a-har-file)
* Screenshot console errors
* Contact [**support@document360.com**](mailto:support@document360.com) with HAR file and screenshots

![Document360 console interface displaying support articles and troubleshooting options for users.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Browser_console.png)

### Access blocked: "Sorry, you have been blocked" / "You are unable to access us.document360.io"

**Error**: "Sorry, you have been blocked" or "You are unable to access us.document360.io" with **Cloudflare Ray ID**. Indicates access restriction due to network, browser, or security issues.

![Access denied message indicating a block by Cloudflare with a Ray ID.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Troubleshooting_cloudfare_error.png)

**Steps to resolve**:

1. Check accessibility using different browser, network, or computer:

   * If accessible in another browser, provide **browser name and version**
   * If accessible on different computer, provide **operating system name and version**
   * If accessible on different network, provide **network setup and IP address**
2. Generate HAR file following [these steps](https://docs.document360.com/docs/document360-support-generating-a-har-file)
3. Screenshot console errors
4. Contact [**support@document360.com**](mailto:support@document360.com) with HAR file, screenshots, and details from Step 1

![Document360 console interface displaying support articles and troubleshooting options for users.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Browser_console.png)

### Login issue: Knowledge base portal keeps loading

**Error**: Unable to log in because the login page keeps loading indefinitely. Caused by browser cache, extensions interfering, or incorrect system time.

**Steps to resolve**:

1. Clear browser cache and cookies. Check if affects all team accounts or specific users:

   * **Google Chrome:** Menu > Settings > Privacy and security > Clear browsing data
   * **Mozilla Firefox:** Menu > Settings > Privacy & Security > Clear Data
   * **Microsoft Edge:** Menu > Settings > Privacy, search, and services > Choose what to clear
   * **Safari (Mac):** Safari > Preferences > Privacy > Manage Website Data > Remove All
   * **Safari (iPhone/iPad):** Settings > Safari > Clear History and Website Data
   * **Opera:** Menu > Settings > Advanced > Privacy & Security > Clear browsing data
2. Try accessing portal in incognito/private browser window. Some extensions may block login.
3. Inspect page for loading time issues:

   * Right-click and select **Inspect**
   * Check console for error messages
   * Monitor loading times
4. Ensure system time zone is correct. Incorrect clock or mismatch causes login failures.
5. If issue persists, capture diagnostic data:

   * Generate HAR file following [these steps](https://docs.document360.com/docs/document360-support-generating-a-har-file)
   * Share with [**support@document360.com**](mailto:support@document360.com)

---

### FAQs

#### **Can I download the Document360 desktop application?**

Document360 is available only as a **web application** accessible through desktop browsers.

#### **Can I access the Knowledge base portal on smartphones and tablets?**

Yes, accessible via mobile browser. Best experience not recommended through web-view workarounds.

#### **How do I clear the Document360 project cache?**

Clear cache to resolve display or functionality issues:

1. Navigate to specific location in Knowledge base portal
2. Open developer tools:

   1. Windows: Press `Ctrl+Shift+I`
   2. macOS: Press `Cmd+Shift+I`
3. Right-click and hold **refresh** button
4. Select **Empty Cache and Hard Reload**

#### Why am I unable to log in to my Document360 account? The callback URL is not working.

Caused by intermittent cache issues or incorrect system time. If internal clock isn't synchronized, login failures occur including callback URL issues (`portal.document360.io/callback`).

**Steps to resolve:**

* Clear browser cache and cookies, then try logging in again
* Verify system time settings and ensure correct synchronization

![Webpage displaying a loading document360 icon and a highlighted URL in the address bar.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Callback_while_logging.png)

<a id="document360-my-projects"></a>

## Project dashboard

**Plans supporting access to Your projects page**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

### What is Document360 - Your projects?

"Your Projects" serves as your main dashboard upon logging into Document360. Provides a centralized view of all projects you're associated with, whether as owner, team member, or reader, along with essential navigation tools.

---

## Navigating the 'Your projects' page

Upon logging in, you see tiles representing each Document360 project you have access to. These include projects you own or are associated with as team account or reader. Here's what you can do:

### 1. **Create New or Sandbox Project**

Initiate a new [Project](/help/docs/creating-a-project) or [Sandbox project](/help/docs/creating-a-sandbox-project) using buttons at the top right corner.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/My projects.png "My projects.png")

---

### 2. Projects

Document360 projects you own and those you're associated with as team account or reader are available. Click project tiles to navigate easily.

#### Project tile elements - Team account

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Project tile elements.png "Project tile elements.png")

1. **Logo:** Project logo for quick identification
2. **Project name:** Clearly labeled to identify each project
3. **Project site access:** Indicates Public, Private, or Mixed access
4. **Settings:** Manage project-specific settings directly from tile
5. **Documentation editor:** Access knowledge base portal to create and manage documentation
6. **View in knowledge base site:** Navigate directly to associated knowledge base site

---

### 2. Profile

Manage personal account settings and log out using the profile menu.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Profile.png "Profile.png")

---

### 3. Release updates

Stay informed about latest Document360 product enhancements by clicking the Release updates icon. Expand release posts to read detailed updates.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Release updates(1).png "Release updates(1).png")

---

### 4. Help

Access support resources from the Help menu:

* **Documentation:** Access detailed guides and resources
* **Issues/Clarifications:** Report issues or seek clarifications
* **Submit a Feature Request:** Suggest new features or improvements
* **System Status:** Check current platform status and performance

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Help.png "Help.png")

This dashboard serves as a central hub for managing and accessing all Document360 projects, ensuring streamlined navigation and efficient project management.

<a id="top-right-menu-overview"></a>

## Top-right menu overview

**Plans supporting access to My profile page**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

The top-right corner provides quick access to key features: view and edit profile, check access levels, change password, stay informed about updates, and explore help resources.

## Key features in the top-right menu

* **My profile**: View and edit personal information, profile picture, and biography. Displays assigned portal and content roles/permissions.
* **View access and permissions**: Check assigned roles and permissions. Ensures appropriate access levels.
* **Change password**: Securely update login credentials. Choose strong password for account protection.
* **Release updates**: Stay informed about latest updates and feature releases.
* **Help menu**: Access helpful resources including:

  + **Documentation:** Explore user guides and feature instructions
  + **Support portal**: Raise support tickets and seek assistance
  + **Contact support**: Directly reach out for help

![Document360 interface showing user profile settings.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Top_right_menu_overview.png)

---

## Accessing profile options

Access the first three options — **My profile**, **View access and permissions**, and **Change password** — by clicking your **profile picture** in the top-right corner.

> NOTE
>
> Icon displays your profile image or default placeholder. Shows initials until image upload.

### My profile

The **My profile** section allows you to view and edit personal information.

To access:

1. Click profile picture
2. Click **My profile** from dropdown menu. Opens **My profile** side panel.

![Document360 interface showing user profile access menu.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Top_right_menu_my_profile.png)

#### Features available in my profile

* **Profile image** - Update or delete profile picture
* **First and last name** - View and edit name
* **Email ID** - View email address
* **Author page URL** - View and edit author page URL
* **Author bio** - Add or update biography. Blank if none added
* **Edit button** - Update or delete profile image, name, URL slug, and biography
* **Portal language** - Change knowledge base portal language. Available: English, Spanish, Portuguese (Brazil). Applies only to portal view
* **Portal role** - View assigned role (Owner, Admin, Contributor)
* **Content role & access** - Check content roles and access levels including workspace names, languages, and categories
* **View contributions** - Click hyperlink to view contributions in Team Accounts module under Analytics

![User profile settings showing role, language, and access details in Document360.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-My_profile_side_panel.png)

> NOTE
>
> Email IDs cannot be edited for SSO users.

### View access and permissions

Check assigned permissions within Document360 for Portal role and Content role. Portal roles manage administrative settings. Content roles control access and actions related to content management.

![User interface showing access permissions in Document360.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Top_right_menu_view_access_permissions.png)

To view permissions:

1. Click profile picture in top-right corner
2. Click **View access and permissions** in dropdown menu. Opens popup window

View permissions assigned for each feature under Portal role and Content role.

Edit/update permissions from Team accounts & groups page in Document360 settings. Changes require appropriate Portal role permissions (Owner or Admin).

Read the article on Roles & permissions for more information.

![Access permissions for project settings, team auditing, and event notifications overview.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-View_access_permissions_window.png)

> NOTE
>
> Available only when accessing top-right menu from within a project.

### Change password

Securely update login credentials.

![User interface showing the option to change password in settings.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Top_right_menu_change_password.png)

To update password:

1. Click profile picture in top-right corner
2. Click **Change password** from dropdown menu. Opens popup window
3. Enter **current password**
4. Enter **new password** meeting security requirements

> NOTE
>
> New password should:
>
> * Be at least 8 characters long
> * Contain at least 1 UPPERCASE letter
> * Contain at least 1 lowercase letter
> * Contain at least 1 number
> * Contain at least 1 special character

5. Confirm new password by re-entering
6. Click **Save**

> NOTE
>
> Changing password logs you out immediately. Log in with updated password.

#### Best practices for updating your password

**Dos**

* Create unique password combining numbers, words, symbols, uppercase and lowercase letters

> **Example:** En37df_n4r-hufling

**Don'ts**

* Don't use easily guessed passwords like "password," "123456," or "user"
* Don't choose passwords based on easily obtainable details (birth date, phone number, family names)
* Don't use dictionary words. If necessary, add numbers and special characters
* Don't use simple adjacent keyboard combinations like "qwerty" or "123456"

---

## Release updates

Stay up-to-date with latest Document360 updates and announcements.

To read latest updates:

1. Click **Release updates** icon in top-right corner. Popup displays three latest releases
2. Click any update to read summary. Click **Read the whole post** for full details
3. Click **Document360 updates** to redirect to [**Document360 Updates - Changelog**](https://changelog.document360.com/?utm_medium=widget) page

![Document360 interface showing recent updates in a sidebar.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Top_right_menu_release_updates.png)

> NOTE
>
> Read latest Document360 release note [**here**](https://docs.document360.com/docs/release-note).

---

## Help menu

Several tools to assist users in resolving queries, accessing resources, and staying informed.

Click **HELP** in top-right corner to access help menu.

### Options available in the help menu

1. **Get assistance:** Opens side-panel widget to search for answers or access documentation
2. **Documentation:** Redirects to Document360 knowledge base at `https://docs.document360.com/docs`
3. **Chat with us:** Opens chat widget connecting you with customer support
4. **Issues and clarification:** Launches widget to create support tickets with details and attachments
5. **Submit a feature request:** Platform to share feedback and suggest features. Visible to other users who can vote
6. **System updates:** Redirects to `https://status.document360.com/` for operational status

![Document360 interface showing help features for users.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Top_right_menu_help_menu.png)

> NOTE
>
> Contact support directly via email at [support@document360.com](mailto:support@document360.com).

---

### FAQs

#### What happens if the browser does not support the selected portal language?

Document360 defaults to English.

#### What if I select Spanish as my portal language but my browser's preferred language is set to English?

All projects display in Spanish following user preference. Browser language setting doesn't override portal selection.

<a id="creating-a-project"></a>## Creating a project in Document360

#### Plans supporting project creation

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

A project in Document360 serves as a container for all your documentation needs. It encapsulates articles, categories, subcategories, home page, team accounts, readers, groups, and custom configurations.

## How to create a knowledge base project

Projects streamline documentation management. Whether creating user manuals, internal processes, or API documentation, Document360 provides the framework. Follow these steps:

### Access dashboard

1. Log in to [**Document360 portal**](https://portal.document360.io/) to access **Dashboard**
2. If in different project's Knowledge base portal, click Document360 icon at top left to return to **Dashboard**
3. Click **+Project** button at top right

![Document360 interface showing projects dashboard.](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/My projects.png)

### Choose use case

4. Select primary use case by clicking **Get started**

| Use case | Description |
| --- | --- |
| **Knowledge base platform** | Centralized hub for team knowledge and resources. Enables quick answers and enhances customer self-service. |
| **Software documentation** | Organize technical documentation. Document product features, APIs, and release notes for developers and users. |
| **SOP documentation** | Create detailed procedures. Ensures consistent processes, reduces errors, and helps onboard new employees. |
| **User manual** | Develop comprehensive guides. Reduces support queries with step-by-step instructions and troubleshooting. |
| **API Documentation** | Document endpoints, request/response formats, authentication, and examples for developer integration. |
| **Others** | Customize knowledge base for specific organizational needs outside predefined categories. |

### Select template

5. Choose content type for your project. Select up to two templates.

> NOTE
>
> Templates embed during project creation based on selection.

**Knowledge base platform templates**

Select two templates if using Knowledge base platform:

| Template | Purpose |
| --- | --- |
| **Getting started guides** | Step-by-step instructions for new users to begin using your product. |
| **How-to guides** | Detailed instructions for specific tasks to utilize product features. |
| **FAQs** | Common questions and answers to reduce support queries. |
| **Policy & procedures** | Organizational protocols and guidelines. |

**Software/Technical documentation templates**

Select two templates if using Software/Technical documentation:

| Template | Purpose |
| --- | --- |
| **Release notes** | Updates on new features, bug fixes, and improvements with each release. |
| **Software Design Documentation** | Software architecture and design including diagrams and specifications. |
| **Software Requirement Documentation** | Software purpose, functionalities, and environment description. |
| **Product Requirement Documentation** | Product purpose, value, and functionalities definition. |
| **Process documentation** | Software development steps and procedures. |
| **User guide** | Comprehensive instructions covering all features and functionalities. |

**SOP documentation templates**

Templates available for SOP documentation:

| Template | Purpose |
| --- | --- |
| **Compliance policies** | Regulatory requirement documentation to enforce compliance. |
| **Operation SOP** | Standardized operational procedures for efficiency. |

**User manual templates**

Select two templates if using User manual:

| Template | Purpose |
| --- | --- |
| **Installation manual** | Product setup information including overview and assembly instructions. |
| **Instruction manual** | Assembly and usage instructions with diagrams and safety warnings. |
| **Maintenance manual** | Upkeep, troubleshooting, and repair procedures. |
| **Training manual** | Installation, operation, and troubleshooting guidance. |
| **Operations manual** | Daily maintenance and troubleshooting instructions. |

### Personalize knowledge base

6. Enter preferred website URL. Skip to default to domain linked to registration email.

### Brand guidelines

7. Project name, default language, branding logo, and colors auto-set based on URL. Edit fields if needed.
8. Browser language determines default language. English selected if browser language unsupported.

> NOTE
>
> * Spanish or Brazilian Portuguese portals auto-set if chosen as default language
> * Branding elements extracted from website. Skip to apply Document360 defaults
> * Preview knowledge base on right side of screen

### Set documentation privacy

9. Choose privacy settings:

   * **Private**: Internal access only
   * **Public**: Open access to all
   * **Mixed**: Combination of private and public sections
10. Click **Next**

### Access knowledge base portal

Once setup completes, enter Document360 Knowledge base portal. Pre-loaded articles based on selected use case and templates appear.

> NOTE
>
> Articles tailored to your selections provide head start on content creation.

![Onboarding process in Document360](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Final_onboarding_process.gif)

---

## Switching between projects

Work on multiple projects or switch between them for various tasks.

Two ways to switch projects:

1. Projects dropdown
2. Projects dashboard

### Switch using dropdown

1. Click project dropdown at top-left from any Knowledge Base module
2. View project name, site access (Public, Private, Mixed), and Sandbox label
3. Click desired project

![Project switching dropdown](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Switching%20between%20projects%20-%201.png)

### Switch from dashboard

1. Click Document360 logo at top-left

![Dashboard navigation](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Switching%20between%20projects%20-%202.png)

Redirected to "My Projects" page showing all projects.

2. Click desired project

![Project list](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Switching%20between%20projects%20-%203.png)

---

### FAQs

#### Does Document360 support different languages in onboarding?

Yes. Multi-lingual support includes English, Spanish, Brazilian Portuguese, German, and Swedish. Portal language support limited to English, Spanish, and Brazilian Portuguese.

#### Can I customize project appearance and structure?

Yes. Customize home page, themes, branding, and organize articles hierarchically.

#### Is access control possible within projects?

Absolutely. Assign roles and permissions to restrict or grant access based on responsibilities.

#### How does version control work?

Article revisions automatically save and track changes, allowing reverts to previous versions.

#### How do I identify current project?

Project name displays at top-left of Knowledge Base portal.

#### What if desired project doesn't appear?

Verify access permissions. Contact administrator if issue persists.

#### What is a Sandbox project?

Test environment for experimenting without affecting live projects. Labeled in project dropdown.

#### What does Site Access mean?

Indicates Public, Private, or Mixed accessibility level.

#### How to request project access?

Contact team administrator or project owner.

Application Programming Interface - Rules enabling software application communication.

<a id="dashboard"></a>

## Dashboard

**Plans supporting Dashboard**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Dashboard provides insights on projects, team members, and tasks. Two tabs available: **My contribution** and **Overview**.

* **My contribution**: Your articles and contributions
* **Overview**: All team accounts associated with project

## My contribution tab

Shows your contributions to associated Document360 project including workspaces and languages.

View contributions in terms of:

* Article summary (created, published, performance metrics)
* Assigned articles
* Review reminders
* Feedback to address
* Broken links

![Dashboard interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_GIF-Dashboard_my_contribution_overview.gif)

> NOTE
>
> Filter data by workspace and language using dropdown. Select "All workspaces" and "All languages" for complete view.

### Article summary

Left section shows articles you've worked on:

* **Created articles**: Number of created articles
* **Published articles**: Number of published articles
* **Draft articles**: Number of updated but unpublished articles

Performance metrics include:

* Overall views
* Reads
* Likes
* Dislikes

> NOTE
>
> Use **Date** filter (top right) to view statistics for last week, month, or custom range.

### Assigned to me

Shows all articles assigned to you across workspaces and languages. Displays current workflow status and due dates.

### Review reminders

Articles marked stale after set period without updates appear here with stale date.

### Feedback

User feedback assigned to you from Feedback manager appears in this tab with status and assignment date.

### Broken links

Articles containing broken links listed here with workspace, language, and broken link count.

## Overview tab

Team members with Owner or Admin roles view key project information:

* Article contributions
* Performance metrics
* Drive capacity
* Team accounts
* Reader count
* Broken links

Metrics include:

* Article summary (created, published, performance)
* Project overview (recently seen, team accounts, readers, drive capacity, broken links, no result searches, last backup)

![Project overview dashboard](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Project_dashboard_overview_page.png)

> NOTE
>
> Filter data by workspace and language using dropdown. Select "All workspaces" and "All languages" for complete view.

### Article summary

Shows total articles created, published, and draft plus performance metrics for selected timeframe. Filter by contributor.

### Project overview

Manage project with important information:

* **Recently seen**: Contributors who recently accessed project
* **Team accounts**: Total team accounts. Click **View all** for Users & security page
* **Readers**: Total readers. Click **View all** for Readers & groups page
* **Drive capacity**: Used vs. available capacity. Click **View all** for Drive module
* **Broken links**: Total broken links. Click **View all** for Link status page
* **No result searches**: Searches returning no results. Click **View all** for Search analytics
* **Last backed up**: Most recent backup date

---

### FAQ

**How to filter My Contribution data?**

Select specific workspace and language from dropdown, or choose "All workspaces" and "All languages".

<a id="getting-started-with-multi-lingual-knowledge-base"></a>

## Multilingual Knowledge bases

**Plans supporting multilingual knowledge base**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

### What is a multilingual Knowledge base?

Provides content in multiple languages for integrated user experience.

> NOTE
>
> Document360 supports internationalization (i18n) of project Knowledge base sites.

---

## Adding multiple languages to workspace

Add multiple languages to single project workspace.

Navigate to Settings > **Knowledge base portal** > **Localization & workspaces**

Two methods to add new language:

#### Method 1 - Edit workspace

1. Click **Edit** (🖉) icon for workspace
2. Click **New language** at bottom
3. Search for desired language(s)
4. Select checkbox and click **Apply**
5. Click **Update**
6. Click **More** () icon for edit options:

   * **Set as default**: Make language default for workspace
   * **Edit display name**: Modify language display name
   * **Right to left**: Enable for languages written right-to-left
   * **Hide**: Hide language (indicated by strikethrough)
   * **Remove**: Delete language from workspace

![Multilingual setup](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-Multilingual_Knowledge_Base.gif)

#### Method 2 - Localization icon

1. Click **Add new language** () icon
2. Search and select desired languages
3. Click **Add**

> NOTE
>
> Languages display in native script except English.

![Language selection](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenShot-Multilingual_language_base.gif)

> NOTE
>
> Categories and articles from default language available in new languages. Manual translation required using machine translation or extensions like Crowdin.

---

## FAQ

**How many languages per workspace?**

Default languages per plan:

* **Professional**: 2 languages
* **Business**: 3 languages
* **Enterprise**: 5 languages

Additional languages available as add-on.

Knowledge base - Public website where end-users access articles and find answers.

Knowledge base - Online library for product, service, department, or topic information.

Knowledge base portal - Platform where project members manage content, create categories/articles, manage files, and configure settings.

<a id="creating-a-sandbox-project"></a>

## Creating a sandbox project

**Plans supporting Sandbox project**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

### What is a Sandbox project?

Isolated test environment to explore features without impacting live knowledge base.

Use sandbox to:

* Test new features and settings
* Identify issues early
* Refine setup and train team

Example: Redesign Knowledge base layout, test with internal teams, adjust before live implementation.

---

## Creating a Sandbox project

1. Navigate to **Settings** > **Knowledge base portal** > **General**
2. In **Sandbox** section, click **Create Sandbox**
3. Enter project name (30 character limit, A-Z, a-z, 0-9, hyphens, spaces only)
4. Select language
5. Optional: Select **KB site 1.0** checkbox
6. **Knowledge base visibility** defaults to [**Private**](/docs/site-access#private-access)
7. Click **Next**
8. Optional: Invite team accounts (separate emails with commas)
9. Select role for each team account
10. Click **Create project**
11. Click **Open Sandbox** to access

![Sandbox creation process](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/New_UI_1_ScreenGIF-Creating_a_Sandbox_project.gif)

**Sandbox** badge appears next to **Open site** in top bar and beside workspace name.

![Sandbox badge](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-New_Sandbox_badge_in_the_top_bar.png)

> NOTE
>
> SSO users cannot create sandbox projects due to authentication requirements.

### Reasons for sandbox project

* **Reduced Risk**: Isolated testing environment
* **Increased Efficiency**: Pre-launch testing ensures smooth transitions
* **Safe Exploration**: Test Document360 features without live disruptions
* **Training Platform**: Hands-on experience without unintended impacts

---

### FAQs

#### How to configure Sandbox subdomain?

Subdomain includes `sandbox` prefix. Modify using [custom domain mapping](https://docs.document360.com/docs/custom-domain-mapping).

#### How does Sandbox improve management?

Controlled environment to assess features before live implementation, enhancing content quality.

#### Can I test configurations safely?

Yes. Evaluate templates, integrations, and scripts without impacting primary knowledge base.

#### How does Sandbox prevent customer impact?

Verify navigation menus and search algorithms before customer exposure.

#### Can I migrate sandbox to production?

No direct migration option. Export data from sandbox and import to production manually.

#### Why can't SSO users access Sandbox?

Request team member with standard account to create user account for you.

<a id="quick-summary-of-the-security-and-infrastructure-aspects"></a>## Using Markdown in your Knowledge base

Refer to [**Editor choices in Document360**](/help/docs/using-the-text-editor) for detailed comparison of editing options.

* Use Markdown syntax manually or format text using the Markdown toolbar.
  For example, make text **Bold** by typing `**word**` or clicking the **Bold** icon.
* Syntax must match required character arrangement exactly.
* See [**Markdown basic syntax**](https://www.markdownguide.org/basic-syntax/) for comprehensive reference.

> **Examples of proper syntax:**
> 
> **Bold**: `**Text**` (not `** Text **`)
> 
> **Headings**: `### Heading3` (not `###Heading3`)

---

## Markdown toolbar

The WYSIWYG toolbar provides formatting options including media insertion.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-Markdown_Editor.png)

* **Headings**
* **Basic text formatting**
* **List**
* **Insert**
* **Callouts**
* **Private notes**
* **Find and replace**
* **Insert LaTeX**
* **Content reuse**
* **Code block**
* **Glossary**
* **Video**

### Headings

* **H2**: **Heading 2**
* **H3**: **Heading 3**
* **H4**: **Heading 4**

### Basic text formatting

* **Bold:** Make text bold
* **Italic:** Make text italic
* **Strikethrough:** Cross out text
* **Blockquote:** Offset quotes with a line

  > This is an example of Blockquote.
* **Line**: Insert horizontal line

### List

* **Unordered list:** Bullet-point list
* **Ordered list:** Numbered list

### Insert

* **Insert Table:** Add table
* **Insert image:** Add image from URL, local drive, or Document360 Drive
* **Insert file:** Add PDF or Word document
* **Insert a link:** Add hyperlink to URL or Knowledge base article

### Callouts

* **Info**: Blue info box
* **Warning:** Yellow warning box
* **Error:** Red error box

### Private notes

* **Private notes**: Purple internal comment box visible only to team members

> **Example**: Add internal feedback for team members

### Insert LaTeX

* **Insert LaTeX**: Add mathematical expressions

  1. Click **Insert LaTeX** - sample syntax (a² + b² = c²) appears
  2. Type desired syntax
  3. Syntax must start and end with **$**

  > **Note**: No space between $ and syntax

  + See [**LaTeX help article**](http://docs.mathjax.org/en/latest/input/tex/macros/index.html) for commands

### Find and Replace

* **Find and Replace:** Search and replace text within article

### Content reuse

* **Content reuse:** Reuse content across project
  a. **Variable**: Text only
  b. **Snippet**: Images, tables, etc.

### Codeblock

* **Insert Codeblock**: Add code block

### Glossary

* **Glossary:** Add glossary term

### Video

* **Insert Video**: Embed YouTube, Wistia, or Vimeo video

### Scroll

* **Scroll on/off:** Enable/disable synchronized scrolling between editor and preview

---

### Spell checker in Markdown

1. Right-click misspelled word
2. Browser displays correction suggestions
3. Click suggested correction to apply

   ![5_Screenshot-Markdown_Spell_checker](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Markdown_Spell_checker.png)

---

### FAQs

#### What is a Markdown editor, and how does it differ from a regular text editor?

Markdown editor converts plain text to HTML using simple syntax. Unlike regular editors, it provides live previews. Document360 offers robust Markdown editing capabilities.

#### What are the key features of the Markdown editor in Document360?

Real-time previews, syntax highlighting, keyboard shortcuts, drag-and-drop image support, and integration with version control.

#### Is a Markdown editor suitable for beginners with no syntax-based writing experience?

Yes. Markdown's simple syntax requires no coding knowledge.

#### How do I add ASCII code to my article?

Use the **Code Block** feature.

#### Is it possible to add a code block without any heading?

Yes. Code blocks can be added without headings.

#### Can I use HTML content in the Markdown editor?

Yes, but Markdown syntax is recommended for consistency.

---

## Related blogs

#### [1. The Ins and Outs of Using Markdown for Technical Writing](https://document360.com/blog/markdown-for-technical-writing/)

#### [2. Introductory Guide to Markdown for Documentation Writers](https://document360.com/blog/introductory-guide-to-markdown-for-documentation-writers/)

A lightweight text-to-HTML conversion tool for formatting content like lists, headers, images, videos, and links. Document360 includes a powerful markdown editor as one of its two basic editors.

<a id="markdown-basics"></a>

## Basic Markdown syntax

**Plans supporting the use of Markdown editor**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

The Markdown editor creates clear, organized content in Document360. This guide covers basic commands and formatting for new and experienced users.

Markdown is a lightweight markup language for formatting text using special characters. No coding knowledge required—follow the syntax to create headings, lists, links, and more.

---

## Markdown commands

Format text using Markdown commands. **Syntax** shows how to type content. **Example** column provides reference.

Keyboard shortcuts are available for some commands (see **Notes** column).

| Feature | Syntax | Example | Output | Notes |
| --- | --- | --- | --- | --- |
| **Headings (H2, H3, H4)** | `##`, `###`, `####` before text | `## Heading 2` | Heading 2 | Create section titles with 1-6 hash symbols. Document360 reserves H1 for article titles. |
| **Bold** | `**text**` | `**bold**` | **bold** | Emphasize important text. Shortcut: Ctrl+B / Cmd+B |
| **Italics** | `*text*` or `_text_` | `*italics*` | *italics* | Highlight text subtly. Shortcut: Ctrl+I / Cmd+I |
| **Strikethrough** | `~~text~~` | `~~strikethrough~~` | ~~strikethrough~~ | Cross out text. No shortcut |
| **Numbered List** | `1.` followed by text | `1. First item` | 1. First item | Numbers auto-increment |
| **Bulleted List** | `*` or `-` followed by text | `* Bullet item` | \* Bullet item | Use asterisk `*` or hyphen `-` |
| **Link** | `[text](URL)` | `[Document360](https://docs.document360.com)` | [Document360](https://docs.document360.com) | Clickable text |
| **Blockquote** | `>` before text | `> This is a quote` | Creates callout/blockquote | For quoting or highlighting |
| **Horizontal Line** | `***` | `***` | Creates horizontal line | Separate sections |

---

## Heading levels

| Heading Level | Syntax | Example | Output |
| --- | --- | --- | --- |
| H2 | `## Heading 2` | `## This is Heading 2` | This is Heading 2 |
| H3 | `### Heading 3` | `### This is Heading 3` | This is Heading 3 |
| H4 | `#### Heading 4` | `#### This is Heading 4` | This is Heading 4 |

**TIP**: Ensure blank line above headings and space between hash symbols and text.

---

## Styling text

| Style | Syntax | Example | Output |
| --- | --- | --- | --- |
| **Bold** | `**text**` | `**bold text**` | **bold text** |
| *Italics* | `*text*` or `_text_` | `*italic text*` or `_italic text_` | *italic text* or *italic text* |
| ~~Strikethrough~~ | `~~text~~` | `~~strikethrough text~~` | ~~strikethrough text~~ |
| **Highlight** | `==text==` | `==highlighted text==` | ==highlighted text== |
| **Superscript** | `text^superscript` | `E = mc^2` | E = mc2 |
| **Subscript** | `text~subscript` | `H~2~O` | H2O |

**TIP**: Avoid spaces between syntax and text.

---

## Lists

| List Type | Syntax | Example | Output | Description |
| --- | --- | --- | --- | --- |
| **Numbered List** | `1. Item` | `1. First item` | 1. First item | Auto-incrementing numbers |
|  | `2. Item` | `2. Second item` | 2. Second item | Continue pattern for items |
|  | `3. Item` | `3. Third item` | 3. Third item |  |
| **Bulleted List** | `* Item` | `* Bullet item` | - Bullet item | Use `*`, `-`, or `+` |
|  | `- Item` | `- Another bullet item` | - Another bullet item | Any symbol creates bullet |
|  | `+ Item` | `+ Yet another bullet item` | + Yet another bullet item |  |

---

## Links and blockquotes

| Feature | Syntax | Example | Output |
| --- | --- | --- | --- |
| Link | `[text](URL)` | `[Document360](https://docs.document360.com)` | [Document360](https://docs.document360.com)` |

**Blockquote**  
Use '>' before text for quotes or highlights.  
`> This will quote the entire line of text`  
Output:

> This will quote the entire line of text

---

## Horizontal line

Use three asterisks for horizontal line.

`***`  
Output:

---

## Quick tips for beginners

1. Use Headings to structure content (sections and subsections)
   * Example: `##` for large headings, `###` for smaller ones
2. Highlight key points with **Bold** or *Italics*
3. Organize information with Lists
   * `1.` for numbered lists, `*` for bullet points
4. Direct users to resources with **Links**

---

## More elements

| Feature | Syntax | Example |
| --- | --- | --- |
| Image | `![Alt text](URL "Optional title")` | `![Logo](https://example.com/logo.png "Logo")` |
| Reference Link | `[Link text][ref]``[ref]: URL` | `[Document360][doc]``[doc]: https://docs.document360.com` |
| Escaping Characters | `\character` | `\*This is not italic\*` |
| YouTube Video | `<iframe src="https://www.youtube.com/embed/VIDEO_ID" width="560" height="315" frameborder="0" allowfullscreen></iframe>` | `<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" width="560" height="315" frameborder="0" allowfullscreen></iframe>` |
| Vimeo Video | `<iframe src="https://player.vimeo.com/video/VIDEO_ID" width="640" height="360" frameborder="0" allowfullscreen></iframe>` | `<iframe src="https://player.vimeo.com/video/76979871" width="640" height="360" frameborder="0" allowfullscreen></iframe>` |

For HTML, copy examples and replace URLs.

---

## Emoji usage

Copy and paste emojis directly from the table below.

| **Emoji** | **Description** |
| --- | --- |
| 📝 | Memo |
| ✍️ | Writing Hand |
| 📄 | Page Facing Up |
| 📚 | Books |
| 📖 | Open Book |
| 🖋️ | Fountain Pen |
| 📑 | Bookmark Tabs |
| 🔍 | Magnifying Glass |
| 📅 | Calendar |
| 💻 | Laptop |
| 📊 | Bar Chart |
| 📈 | Chart with Upwards Trend |
| 🗂️ | Card Index Dividers |
| ✏️ | Pencil |
| 😊 | Smiling Face |
| ❤️ | Red Heart |
| 🌟 | Star |
| 🔥 | Fire |
| 🎉 | Party Popper |

Paste desired emoji into document. Insert FontAwesome icons using HTML code.

---

## Using Unicode characters in the Markdown editor

Unicode characters enhance Markdown documents with symbols, special characters, and non-Latin scripts.

### Syntax for inserting Unicode characters

1. **Direct copy-paste:** Copy character from Unicode reference and paste into Markdown

   **Example:**
   ```
   ★ Star symbol
   ```
   **Output:** ★ Star symbol

2. **HTML entity code:** Use format `&#xXXXX;` where `XXXX` is hex code

   **Example:**
   ```
   &#x1F680; Rocket symbol
   ```
   **Output:** 🚀 Rocket symbol

### Common Unicode characters

| Character | Description | Unicode (Hex) | HTML entity code |
| --- | --- | --- | --- |
| ★ | Star symbol | 2605 | `&#x2605;` |
| ✔ | Check mark | 2714 | `&#x2714;` |
| ✉ | Envelope | 2709 | `&#x2709;` |
| © | Copyright | 00A9 | `&#x00A9;` |
| € | Euro sign | 20AC | `&#x20AC;` |
| → | Right arrow | 2192 | `&#x2192;` |
| ♻ | Recycling symbol | 267B | `&#x267B;` |

#### Finding more Unicode characters

See [Unicode Character Table](https://unicode-table.com/) or [Unicode.org Code Charts](https://www.unicode.org/charts/) for extensive lists.

---

## Example: Creating a simple article

```
#### Welcome to Markdown  
Learn how to use **Markdown** in Document360 to format your articles.  

#### Why use Markdown?  
* Easy to learn  
* Clean and organized formatting  
* Saves time  

#### Useful tips  
1. Use headings to structure your content.  
2. Add links for more resources: [Learn Markdown](https://markdownguide.org)  
3. Use `***` to create a divider.  
```

### Output

#### Welcome to Markdown

Learn how to use **Markdown** in Document360 to format your articles.

#### Why use Markdown?

* Easy to learn
* Clean and organized formatting
* Saves time

#### Useful tips

1. Use headings to structure your content.
2. Add links for more resources: [Learn Markdown](https://markdownguide.org)
3. Use `***` to create a divider.

---

See official [Markdown syntax guide](https://www.markdownguide.org/basic-syntax/) for advanced commands.

Tags structure subheadings in articles. H1 applies automatically to titles. H2, H3, and H4 create subheadings with progressively smaller text.

A lightweight text-to-HTML conversion tool for formatting content like lists, headers, images, videos, and links. Document360 includes a powerful markdown editor as one of its two basic editors.

<a id="wysiwyg-editor"></a>

## WYSIWYG editor

**Plans supporting the use of WYSIWYG editor**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

The **WYSIWYG (What You See Is What You Get)** editor shows content as it will appear when published.

> **Note**: Cannot switch from WYSIWYG to Markdown. Articles converted from Markdown to WYSIWYG cannot be reverted. Switching from Markdown to WYSIWYG is supported.

---

## WYSIWYG toolbar

The WYSIWYG toolbar offers various text editing and media insertion options.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-WYSIWYG_Editor(1).png)

### 1. Heading options

Available heading options:

Normal

## Heading 2

### Heading 3

#### Heading 4

### 2. Text formatting

Available text styling options:

* **Bold**: Bold text
* *Italic*: Italicize text
* Underline: Underline text
* ~~Strikethrough~~: Cross out text
* **More text**: Font size, family, color, background color, subscript, superscript, clear formatting

### 3. Paragraph formatting

Available paragraph formatting options:

* **Unordered list**: Bullet symbols: •, ○, ◘. Disc and Default are identical
* **Ordered list**: Numbered items. Supports numbers, alphabets, Roman numerals, Greek numerals. Default uses numbers
* **More paragraph**: Alignment, line height, indentations, quote text

### 4. Insert options

* **Insert link**: Add hyperlink to URL or Knowledge base article
* **Insert codeblock**: Add codeblock (e.g., JavaScript snippet)
* **Insert image**: Add image from URL, local storage, or Drive. Shortcut: Ctrl+p
* **Insert file**: Add {{glossary.File}} from Drive (Word or PDF)
* **Insert callouts**: Add info boxes (blue), warning boxes (yellow), error boxes (red)
* **Private notes**: Internal comment box visible only to team members
* **Insert LaTeX**: Add mathematical expressions using LaTeX syntax

  + Click **Insert LaTeX** - **Insert latex expression** window appears. Type LaTeX syntax and click **Insert**. See [this article](http://docs.mathjax.org/en/latest/input/tex/macros/index.html) for more information
  + Click Edit (Pencil) icon to modify expression. Make changes and click **Update**
  + Click Remove (Trashbin) icon to delete expression
* **Find & replace**: Search and replace text within article
* **Content reuse**: Reuse content with:
  + **Variable**: Text content
  + **Snippet**: Text, images, tables, code blocks, etc.
* **Glossary**: Maintain terms and definitions in Knowledge base

### **5. More rich**

* **Insert video**: Embed videos from YouTube, Wistia, Streams, or Vimeo
* **Insert table**: Add table by selecting rows and columns
* **Insert horizontal line**: Add line to article
* **Emoticons**: Insert emoticons to enhance engagement

### 6. Other options

Additional features:

* **Code view**: Switch to HTML syntax editor
* **Undo**: Undo previous action
* **Redo**: Repeat previous action

### 7. Editor switch

* Use switch editor toggle to convert article to Advanced WYSIWYG editor
* Click toggle and **Switch to New Editor** to convert
* See [Advanced WYSIWYG editor](/help/docs/advanced-wysiwyg-editor-overview) for guidance

### Additional formatting options

### 1. Image

After adding image, available options:

a. **Replace**: Replace image  
b. **Align**: Add caption to align image  
c. **Image caption**: Appears below image  
d. **Remove**: Delete image  
e. **Insert link**: Add link to image (can open, remove, edit)  
f. **Display**: Change image display (Inline or Break Text)  
g. **Style**: Border style (Rounded, Bordered, Shadow)  
h. **Alternative text**: Text shown if image fails to load  
i. **Change size**: Adjust width and height in pixels  
j. **Advanced edit**: Crop, text formatting, rotate, zoom, navigation, history, undo/redo, reset, delete functions

### 2. Video

After embedding video, available options:

a. **Replace**: Replace video  
b. **Remove**: Delete video  
c. **Display**: Change video display (Inline or Break Text)  
d. **Align**: Align video  
e. **Change size**: Adjust video size  
f. **Autoplay**: Toggle autoplay

### 3. PDF

After adding PDF, available options:

a. **Remove**: Delete PDF  
b. **Change size**: Adjust PDF size

### 4. Word file

After adding Word file, available options:

a. **Open link**: Download file  
b. **Remove**: Delete file

### 5. Table

After adding table, available options:

a. **Table header**: Toggle header row visibility  
b. **Remove table**: Delete table and content (use Undo if accidental)  
c. **Row**: Insert/delete rows  
d. **Column**: Insert/delete columns  
e. **Table style**: Dashed Borders, Alternate Rows  
f. **Cell**: Merge/split cells  
g. **Cell background**: Change background color  
h. **Vertical align**: Align content top/middle/bottom  
i. **Horizontal align**: Align content left/center/right/justified  
j. **Cell style**: Highlighted or Thick borders

---

## When, Where, and Why to Use the WYSIWYG Editor

#### Who can use the WYSIWYG editor?

Document360 users comfortable with HTML editors

#### Is the WYSIWYG editor easy to use?

Similar to word-processing applications like Microsoft Word or Google Docs.

Copy and paste content directly from Word or other sources. No special syntax required.

#### Why use the WYSIWYG editor?

* Single editing pane with live preview
* Paste large tables from third-party sites or other Knowledge bases

<a id="advanced-wysiwyg-editor"></a>

## Advanced WYSIWYG editor

**Plans supporting the use of Advanced WYSIWYG editor**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

The Advanced WYSIWYG editor combines lightweight design with rich text editing capabilities, supporting specific Markdown syntax. More visual than traditional Markdown editors but more flexible than standard WYSIWYG editors.

> **Note**: Can switch between Advanced WYSIWYG and WYSIWYG editors when article is in **Draft/New** state. Switching disabled for **Published** articles.

> **Caution**: Articles converted from Markdown to Advanced WYSIWYG cannot be reverted.

---

## Using Advanced WYSIWYG editor

Use slash commands, toolbars, and specific Markdown syntax to create and edit content.

### Slash commands

Type `/` in editor to show options. Search by typing command names. Click desired command or press Enter.

> **Note**: Type `/` at start of line or after space. Navigate with arrow keys.

Access **Eddy AI** from top of slash menu. Options categorized into three sections:

| **Format** | **Insert** | **Content Reuse** |
| --- | --- | --- |
| Heading 2 | Image | Variables |
| Heading 3 | Video | Snippets |
| Heading 4 | Link | Glossary |
| Ordered list | Table |  |
| Bullet list | Callouts |  |
| Checklist | Private notes |  |
| Inline code | Code block |  |
| Page break | Insert file |  |
|  | Accordion |  |
|  | Latex |  |
|  | Emoji |  |
|  | Divider |  |

![Updated_ScrenGIF-Slash_command_in_Adv_WYSIWYG](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Updated_ScrenGIF-Slash_command_in_Adv_WYSIWYG.gif)

---

### Markdown syntax

Advanced WYSIWYG editor supports wide range of Markdown syntax. See [Markdown basics](/help/docs/markdown-basics) for detailed list.

> **Example**: Add Heading 2 with `## Heading of the section`. Syntax renders instantly.

> **Note**: Markdown syntax works only when typed manually, not when pasted.
>
> See [Advanced WYSIWYG editor basics](/help/docs/Advanced-WYSIWYG-editor-basics#unsupported-markdown-syntax) for unsupported syntax.

---

## Toolbar

Toolbar has three sections:

* **Format**: Change layout/appearance
* **Insert**: Add elements (images, videos, tables, etc.)
* **Find & replace**: Search and replace text

> **Note**: Use Pin option to anchor toolbar to editor interface

![1_Screenshot-General_view_of_toolbar_in advanced_WYSIWYG_editor](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-General_view_of_toolbar_in%20advanced_WYSIWYG_editor.png)

### Format

![2_Screenshot-Format_seciton_toolbar](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Format_seciton_toolbar.png)

#### 1. Text styles

* **Undo**: Reverse last action
* **Redo**: Reapply last undone action
* **Clear**: Remove all styling
* **Lettercase**: Change text case

#### 2. Headings

* Apply H2 style
* Apply H3 style
* Apply H4 style
* **Paragraph**: Apply standard paragraph style

#### 3. Typography

* **Font family**: Select typeface
* **Font size**: Adjust text size

#### 4. Palette

* **Font color**: Change text color
* **Background color**: Set background color

#### 5. Formatting & Lists

* **Bold**: Bold selected text
* ***Italic***: Italicize selected text
* **Underline**: Underline selected text
* **~~Strikethrough~~**: Cross out selected text
* `Inline code`: Add inline code
* **Align left**: Left-align text
* **Center**: Center text
* **Align right**: Right-align text
* **Justify**: Evenly distribute text between margins
* **Bullet list**: Add bullet-point list
* **Ordered list**: Add numbered list
* **Checklist**: Add checkbox list

#### 6. Controls

* **Increase indent**: Move content away from margin
* **Decrease indent**: Move content toward margin
* **Subscript**: Lower text below baseline
* **Superscript**: Raise text above baseline
* **Line height**: Adjust spacing between lines
* **Letter space**: Change spacing between letters
* **Line break**: Move to next line
* **Page break**: Specify page breaks for PDF export

---

### Insert

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1736939177920.png)

* **Image**: Insert image
* **Video**: Insert video
* **Link**: Insert hyperlink (shortcut: Ctrl + k)
* **Insert file**: Insert file
* **Table**: Insert table
* **Divider**: Insert horizontal line
* **Accordion**: Add expandable/collapsible container
* **Callout**: Insert callout (defaults to info)

  + Customize with: Callout info, warning, error, success, background color, border color, delete
* **Private notes**: Insert private notes
* **Code block**: Insert code block

  + Customize with: Language dropdown, copy, delete
* **FAQs**: Insert FAQ templates
* **Latex**: Insert mathematical equations
* **Variable**: Insert variable
* **Snippet**: Insert snippet
* **Glossary**: Insert glossary term
* **Emoji**: Insert emoji

### Creating FAQs templates:

1. Navigate to article in Advanced WYSIWYG editor
2. Click **Insert** icon and select **FAQs**

   Three FAQ accordion templates inserted
3. Available options in FAQ templates:

   1. Click **Settings** icon to customize
   2. Click **Expand/Collapse** icon to toggle accordions
   3. Click **Delete** icon to remove entire FAQ section
   4. Click **Add question** to insert custom FAQs

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGif-Advanced_WYSIWYG_Editor.gif)

> **Note**:
> * FAQ templates differ from AI FAQ generator
> * See [AI FAQ generator](/help/docs/ai-faq-generator) for more information

#### Code view

* View/edit content in HTML format
* Add custom HTML elements, apply inline styles, make precise adjustments

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1736939256244.png)

> **Note**:
> * Click Save button to save code view changes. Ctrl/Cmd + S doesn't work
> * Ordered/Unordered lists lose sequential ordering
> * Nested lists unsupported when:
>   + Content copied/pasted
>   + Certain migration scenarios

---

### Adding inline comments

1. Navigate to article in Knowledge base portal
2. Select text for comment - floating menu appears
3. Click **Comment icon** (💬)
4. Use formatting tools, @mention team members
5. Click **Send** icon

> **Note**:
> Turn off mode via Knowledge base portal > Documentation > Content tools > Workflow designer. Hover over status, click Edit icon, turn off Read only toggle

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1736939279601.png)

**To view all comments**:

1. Navigate to article
2. Click **Comment icon** (💬) near publish button
3. Comments panel appears. Filter by: All comments, mentioned comments, open comments, resolved comments

Reply to comments here.

![6_Screenshot-View_all_the_comments_in_an_article](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-View_all_the_comments_in_an_article.png)

> **Note**: Only comment creator can edit, resolve, or delete

---

### Pasting from Microsoft Word

Choose to retain or clear formatting when pasting from Word.

1. Click **Paste with formatting** to retain Word formatting
2. Click **Paste as plain text** to clear formatting

![Copy and pasting content from Microsoft Word](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Screenshot-copy_pasting_from_Microsoft_word.png)

---

### FAQs

#### Can I add a code block without heading?

Not possible in Advanced WYSIWYG editor. Hide name using Custom CSS in settings. Applies to all code blocks.

Use Markdown editor for code blocks without names.

#### How to add spaces in LaTex formulas?

Use `\;` between terms.

**Example**: `Area = length\;*\;width`

#### How to add numbering?

Three methods:

1. Type `1.` and press space
2. Shortcut: Ctrl + Shift + 7 or Ctrl + Shift + O
3. Format menu: Select content, choose Numbered list icon

Available numbering styles: Default, Lower Alpha, Lower Greek, Lower Roman, Upper Alpha, Upper Roman.

The platform where project members manage and create knowledge base content. Create categories, articles, templates; manage files, team accounts, readers; configure branding, domain, security.

<a id="advanced-wysiwyg-editor-basics"></a>

## Advanced WYSIWYG editor basics

**Plans supporting the use of Advanced WYSIWYG editor**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

## Keyboard shortcuts overview

To view shortcuts:

1. Navigate to article in Advanced WYSIWYG editor
2. Click **More** icon (•••) next to **Publish** button
3. Select **Keyboard shortcuts** from dropdown

#### Windows view

![image](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Keyboard_shortcuts_overview%281%29.png)

#### Mac view

![Updated_Portal_Screenshot-Mac_Keyboard_Screenshot](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Keyboard_shortcuts_overview_macos.png)

### General

| No. | Command | Windows | Mac |
| --- | --- | --- | --- |
| 1 | Copy | Ctrl + C | ⌘ + C |
| 2 | Cut | Ctrl + X | ⌘ + X |
| 3 | Paste | Ctrl + V | ⌘ + V |
| 4 | Paste as plain text | Ctrl + Shift + V | ⌘ + Shift + V |
| 5 | Undo | Ctrl + Z | ⌘ + Z |
| 6 | Redo | Ctrl + Shift + Z | ⌘ + Shift + Z |
| 7 | Add line break | Shift + Enter | Shift + Enter |
| 8 | Insert link | Ctrl + K | ⌘ + K |

### Text formatting

| No. | Command | Windows | Mac |
| --- | --- | --- | --- |
| 1 | Bold | Ctrl + B | ⌘ + B |
| 2 | Italicize | Ctrl + I | ⌘ + I |
| 3 | Underline | Ctrl + U | ⌘ + U |
| 4 | Strikethrough | Ctrl + Shift + X | ⌘ + Shift + X |
| 5 | Highlight | Ctrl + M | ⌘ + M |
| 6 | Code | Ctrl + E | ⌘ + E |

### Paragraph formatting

| No. | Command | Windows | Mac |
| --- | --- | --- | --- |
| 1 | Paragraph style | Ctrl + Alt + 0 | ⌘ + Alt + 0 |
| 2 | Heading 1 | Ctrl + Alt + 1 | ⌘ + Alt + 1 |
| 3 | Heading 2 | Ctrl + Alt + 2 | ⌘ + Alt + 2 |
| 4 | Heading 3 | Ctrl + Alt + 3 | ⌘ + Alt + 3 |
| 5 | Heading 4 | Ctrl + Alt + 4 | ⌘ + Alt + 4 |
| 6 | Heading 5 | Ctrl + Alt + 5 | ⌘ + Alt + 5 |
| 7 | Heading 6 | Ctrl + Alt + 6 | ⌘ + Alt + 6 |
| 8 | Numbered list | Ctrl + Shift + 7 | ⌘ + Shift + 7 |
| 9 | Bullet list | Ctrl + Shift + 8 | ⌘ + Shift + 8 |
| 10 | Check list | Ctrl + Shift + 9 | ⌘ + Shift + 9 |
| 11 | Blockquote | Ctrl + Shift + B | ⌘ + Shift + B |
| 12 | Left align | Ctrl + Shift + L | ⌘ + Shift + L |
| 13 | Center align | Ctrl + Shift + E | ⌘ + Shift + E |
| 14 | Right align | Ctrl + Shift + R | ⌘ + Shift + R |
| 15 | Justify | Ctrl + Shift + J | ⌘ + Shift + J |
| 16 | Code block | Ctrl + Alt + C | ⌘ + Alt + C |
| 17 | Subscript | Ctrl + , | ⌘ + , |
| 18 | Superscript | Ctrl + . | ⌘ + . |

### Text selection

| No. | Command | Windows | Mac |
| --- | --- | --- | --- |
| 1 | Complete article | Ctrl + A | ⌘ + A |
| 2 | One character left | Ctrl + ← | ⌘ + ← |
| 3 | One character right | Ctrl + → | ⌘ + → |
| 4 | One line up | Ctrl + ↑ | ⌘ + ↑ |
| 5 | One line down | Ctrl + ↓ | ⌘ + ↓ |
| 6 | Article beginning | Ctrl + Shift + Home | ⌘ + Shift + Home |
| 7 | Article end | Ctrl + Shift + End | ⌘ + Shift + End |

---

## Typography

Regular symbols/syntax and outcomes:

| No. | Name | Symbol/Syntax | Outcome |
| --- | --- | --- | --- |
| 1 | Em dash | -- | — |
| 2 | Ellipsis | ... | ... |
| 3 | Opening double quote | " | " |
| 4 | Closing double quote | " | " |
| 5 | Left arrow | <- | ← |
| 6 | Right arrow | -> | → |
| 7 | Copyright | (c) | © |
| 8 | Registered trademark | (r) | ® |
| 9 | Trademark | (tm) | ™ |
| 10 | Service mark | (sm) | ℠ |
| 11 | One half | 1/2 | ½ |
| 12 | One quarter | 1/4 | ¼ |
| 13 | Three quarters | 3/4 | ¾ |
| 14 | Plus minus | +/- | ± |
| 15 | Not equal | != | ≠ |
| 16 | Laquo | << | « |
| 17 | Raquo | >> | » |
| 18 | Multiplication | 2 \* 3 | 2×3 |
| 19 | Superscript two | ^2 | ² |
| 20 | Superscript three | ^3 | ³ |
| 21 | Indian rupee | (R) | ₹ |
| 22 | Dollar | (USD) | $ |
| 23 | Pound | (GBP) | £ |
| 24 | Australian dollar | (AUD) | A$ |
| 25 | Triple bar | === | ≡ |
| 26 | Approx | (approx) | ≈ |
| 27 | Greater than or equal | >= | ≥ |
| 28 | Less than or equal | <= | ≤ |
| 29 | Pi | (pi) | π |
| 30 | Euro | (e) | € |
| 31 | Equivalent | <==> | ⇔ |

---

## Unsupported markdown syntax

Advanced WYSIWYG editor doesn't support:

**1. Tables**  
Markdown tables don't render. Example:

```
| header | header |
| --- | --- |
| cell | cell |
| cell | cell |
```

**2. Subscript**  
Apply manually using Format tools.

**3. Superscript**  
Apply manually using Format tools.

<a id="movable-blocks-in-advanced-wysiwyg-editor"></a>

## Movable blocks

**Plans supporting movable blocks**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

### What are movable blocks?

Rearrange content sections for flexible organization.

> **Note**: Block = content section ending with line break. Next content = new block.

### Accessing movable blocks

Click arrow or drag-and-drop to position content.

1. Navigate to article in Advanced WYSIWYG editor
2. Hover over intended block
3. See settings () and ellipsis () icons on left
4. Click ellipsis () to manage position:

   * Move up: Click up arrow () to move above previous block
   * Move down: Click down arrow () to move below next block
   * Delete: Click delete () icon to remove block (next block moves up)
5. Click settings () to add new blocks:

   * **Insert block above** to place new block above selected
   * **Insert block below** to place new block below selected

> **Note**: Hold reorder icon () to drag block to desired location

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Movable_blocks_all_in_one.gif)

> **Note**:
> * Dividers cannot be moved using Movable blocks
> * Entire FAQ section = single block. Individual FAQs within Eddy AI generated section cannot be moved

---

### FAQs

**How to move block to specific location?**

Hold ellipsis () icon to drag block.

**Can I add new blocks between existing sections?**

Yes. Hover over block, click settings (), choose **Insert block above**.

**What happens when I delete a block?**

Following block moves up. Use `Ctrl+Z` to undo deletion.

<a id="conditional-content-blocks"></a>

## Conditional content blocks

**Plans supporting Conditional content blocks**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

**Conditional content blocks** show/hide content based on predefined conditions (IP address, country, device type, reader groups, workspace, dates).

Tailor user experience for large, diverse audiences.

> **Examples**: Region-specific pricing, device-specific support information

> **Note**:
> * Available only for **KB site 2.0** projects
> * Condition-applied content not indexed by Eddy AI or search

---

## Set up conditional content blocks

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Navigating_to_the_conditional_content_panel.png)

1. Navigate to article in Advanced WYSIWYG editor
2. Hover over content block, click **Settings** () icon
3. Select **Conditional Content**

   **Conditional content** panel appears
4. Turn on **Enable** toggle

   In **Visibility** section, choose:

   * **Show**: Display content when condition met
   * **Hide**: Hide content when condition met

   > **Note**: **Show** = visible only to matching users. **Hide** = hidden from matching users
5. Use **AND** when all conditions required. Use **OR** when any condition triggers rule
6. Click **+ Add** to create condition
7. Select parameter from dropdown (country, date, device type, workspace, reader groups, IP address)
8. Enter relevant values:

| **Parameter** | **Conditions** | **Example 1** | **Example 2** |
| --- | --- | --- | --- |
| **Country** | Equals, Not equals, In, Not in | **Equals India** - only Indian readers see content | **Not in USA** - all except USA readers see content |
| **Date** | After, Before, Between | **Before October 1, 2024** - visible until date | **Between Sep 1 - Oct 1, 2024** - visible during period |
| **Device** | Equals, Not equals, In, Not in | **Equals Mobile** - mobile users only | **Not in Desktop** - hidden from desktop users |
| **Workspace** | Equals, Not equals, In, Not in | **Equals Marketing** - Marketing workspace users | **Not in Sales** - hidden from Sales workspace |
| **Reader groups** | Equals, Not equals, In, Not in | **Equals Admins** - Admin group users | **Not in Editors** - hidden from Editors |
| **IP address** | Equals, Not equals, Range, In, Not in | **Equals 192.168.1.1** - specific IP users | **Range 192.168.1.1-100** - IP range users |

> **Note**:
> * **Workspace** parameter appears only with multiple workspaces
> * **In**/**Not in** conditions allow multiple values selection

9. Click **Save for reuse** to save condition

   > **Note**: Useful for large knowledge bases with similar conditions across articles
10. Enter name for condition and click () icon
11. Click **Save** to apply condition
12. Click **Save as** to save condition for future use, enter name and click () icon
13. Click **Remove Condition** to delete
14. Click **Apply** when done

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Performing_Conditional_content.gif)

---

### FAQs

**What are conditional content blocks?**

Display specific content only when certain conditions met (IP, country, device, reader groups, workspace, dates).

**Can I create multiple conditions per article?**

Yes, up to 25 conditions per article.

**Do conditions remain when moving article to different workspace?**

Yes, conditions move with article.

**Can I edit conditions after publishing?**

Fork published article version to modify conditions.

**If article translated, does conditional content apply to all languages?**

Yes, but different visibility rules require language-specific conditions.

**What if no conditions met?**

Content block follows default visibility rules. Visible to all unless explicitly set to **Hide**.

**If project changes from Private to Public, what happens to conditions?**

Parameters like **IP address** or **Reader groups** automatically disabled.

**What happens to conditional content when cloning article?**

All conditions copied. Edit as needed in duplicated article.

**Can I apply multiple "Or" conditions?**

Yes. Example: **Country equals India OR Country equals USA**.

**Can conditions be time-bound?**

Yes, using **Date** parameter. Example: **Date between Dec 1-10, 2024**.

**What if reader group in condition deleted?**

Condition no longer applied.

**Can I apply conditions based on user session status?**

Not directly supported at this time.

**If moving article with conditional content between workspaces, do conditions still apply?**

Yes, but verify relevance in new workspace.

**How do conditions affect articles with multiple versions?**

Conditional content settings are version-specific. Forked versions carry over conditions.

**Is there limit to conditions per block?**

Up to 25 conditions per article. Limit complex conditions for performance/clarity.

<a id="tables-in-advanced-wysiwyg-editor"></a>

## Tables

**Plans supporting Advanced WYSIWYG editor**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Tables organize and present data clearly. Compare features, list options, summarize information.

Advanced WYSIWYG editor offers powerful table formatting and management features.

This article explores table tools: create, format, manage tables.

## Creating a table

Two methods:

* **Slash (/) command**
* **Insert option** in **Format menu**

### Slash (/) command

Type `/table` anywhere in editor, hit Enter. Inserts 3×3 table with header row at cursor location.

> **Note**: Always inserts 3×3 table with header row. Add rows/columns as needed.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_GIF-Insert_table_using_slash_command.gif)

### Insert option in Format menu

1. Click **Insert** in Format menu (right side)
2. Click **Table** option
3. Select table size from grid

> **Note**: Maximum 10×10 from Format menu. Add rows/columns manually.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_GIF-Insert_table_using_format_menu.gif)

## Formatting table content

### Inserting or deleting rows/columns

Select entire row/column. Menu shows **Insert row above/below** or **Insert column left/right** options.

Delete by selecting entire row/column and clicking **Delete row/column**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Insert_row_in_tables.png)

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Insert_column_in_tables.png)

### Merging cells

Select multiple cells. Click **Merge cells** in menu. Selected cells combine into one.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Merge_cells_in_tables.png)

### Cell alignment

Select one or more cells. Menu shows **Vertical align** and **Horizontal align** options.

#### Vertical align

Align text **Top**, **Middle**, or **Bottom**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Vertical_alignment_in_tables.png)

#### Horizontal align

Options: **Left**, **Center**, **Right**, **Justify**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Horizontal_alignment_in_tables.png)

### Fit table to page width

Select table. Click **Fit to page width** in menu. Table spans full page width with evenly distributed content.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/16_Screenshot-Fit_table_to_page_width.png)

---

## Customizing table appearance

### Changing background

1. Select one or more cells
2. Click **Background color** in menu
3. Choose color from palette

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Background_color_in_tables.png)

> **Pro Tip**: Check article preview in dark mode after background updates

### Changing border

#### Border color

1. Select one or more cells
2. Click **Border color** in menu
3. Choose color from palette

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Border_color_in_tables.png)

#### Border style

1. Select entire table
2. Click **Border style** in menu
3. Choose: **Solid**, **Dashed**, or **Dotted**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Border_style_in_tables.png)

### Header rows

Top row defaults to header with grey background.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/11_Screenshot-Header_row_in_tables.png)

* Hide header: Select table, click **Hide table header**

  ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/12_Screenshot-Hide_header_row_in_tables.png)
* Show hidden header: Select table, click **Show table header**

  ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/13_Screenshot-Show_header_row_in_tables.png)

### Alternate row style

Choose banded rows. Row colors alternate between white and light gray.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/14_Screenshot-Banded_rows_in_tables.png)

1. Select entire table
2. Click **Alternate row style** in menu

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/15_Screenshot-Alternate_rows_in_tables.png)

> **Pro Tip**: Customize further with CSS code snippets. See [Table Style](https://docs.document360.com/docs/table-style) article.

---

### FAQs

#### How to copy entire table?

Select table, click **Copy** in menu.

#### How to delete entire table?

Click top-left corner to select table. Choose **Delete** from menu.

#### Can I use automatic numbers in table?

Numbered lists possible within cells. No automatic row numbering.

#### Can I add symbols/icons in table?

Yes. Add directly from **Format** menu or using **HTML** in **Code view**.

#### Will slash commands work inside table?

Yes, all slash commands work inside tables.

#### Can I paste tables from Microsoft Word or Excel?

Supports pasting from Word and Excel web application while retaining structure.

Desktop Excel paste not supported. Use web application for formatting retention.

<a id="image-formatting-in-the-advanced-wysiwyg-editor"></a>

## Image formatting

**Plans supporting image formatting**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Advanced WYSIWYG editor offers image formatting options unavailable in Markdown editor.

Click image to access formatting options.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-floating_menu_in_image.png)

Floating menu features for selected image:

1. **Align**

   Three alignment options:

   * **Align Left**: Left-align image
   * **Center**: Center image
   * **Align Right**: Right-align image
2. **Inline options**:

   * **Inline left**: Image left of text
   * **Inline block**: Image within text flow
   * **Inline right**: Image right of text
3. **Image caption**:

   Add caption below image for context/descriptions
4. **Alt text**:

   Written copy shown if image fails to load

   Enter alternative text and click () icon to save
5. **Hyperlink images**:

   Click link icon to add hyperlinks. Paste URL, select **Open in new tab**, click **Insert**

   After linking, three options appear:
   * **Open Link**: Opens link in new tab
   * **Edit Link**: Edits attached link
   * **Unlink**: Removes link from image
6. Click [**Advanced edit**](/help/docs/image-formatting-in-the-advanced-wysiwyg-editor#advanced-editing-options-for-images) icon for resize, crop, etc.
7. **Style**:

   Three styling options:

   * **Rounded**: Rounded rectangle corners
   * **Bordered**: Light gray border
   * **Shadow**: Drop shadow effect
8. **Resize**: Customize width/height
9. **Replace**: Switch current image using any insert method
10. **Copy**: Copy selected image for use elsewhere
11. **Delete**: Remove selected image

### Advanced editing options

![Editing images in the Advanced WYSIWYG editor](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Editing_an_image(top_bottom).png)

### Top menu options

![Editing images in the Advanced WYSIWYG editor](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-top_menu_over_view.png)

1. **Zoom In/Zoom Out**: Adjust image size
2. **Hand**: Move image while editing
3. **History**: View edit history
4. **Undo**: Revert most recent action
5. **Redo**: Reapply previously undone action
6. **Reset**: Return image to original state
7. **Delete**: Remove selected edited element
8. **Delete All**: Remove all edited elements

---

### Bottom menu options

![Editing images in the Advanced WYSIWYG editor](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-bottom_menu_over_view.png)

1. **Resize**: Adjust width/height, lock aspect ratio. Click **Apply** when done
2. **Crop**: Choose cropping option (Custom, Square, etc.). Click **Apply**
3. **Flip**: Horizontal/vertical flip. Use **Reset** to revert
4. **Rotate**: Rotate 0°-360° (custom range available)
5. **Draw**: Add lines/shapes

   * **Free Draw**: Custom drawing
   * **Straight**: Straight lines
   * **Color**: Select drawing color
   * **Range Slider**: Adjust line thickness
6. **Shape**: Insert shapes (rectangles, circles, triangles)

   * **Fill Color**: Shape fill color
   * **Stroke**: Outline color and thickness
7. **Icon**: Add icons (arrows, location markers, polygons). Upload custom icons. Adjust color
8. **Text**: Add formatted text (bold, italic, underline, alignment, color, size)
9. **Filter**: Adjust parameters (grayscale, blur, brightness, sepia, contrast). Click **Save**

---

### FAQs

**What image formatting options are available?**

Alignment, inline display, captions, alt text, hyperlinking, advanced edit options, styling, resizing, replacing, copying, deleting.

**How to align image?**

Select image, choose left, center, or right alignment from floating menu.

**Can I add caption to image?**

Yes. Captions appear below images for context/descriptions.

**Can I hyperlink image?**

Yes. Click link icon, paste URL, choose new tab option.

<a id="tabs-in-the-advanced-wysiwyg-editor"></a>

## Tabs

**Plans supporting Tabs**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

**Tabs** organize related content within articles. Present lengthy/complex information clearly. Readers find content without scrolling.

---

## Creating tabs

### Adding tabs using Insert option

1. Open **Advanced WYSIWYG editor**
2. Access **Insert** from floating menu or slash command
3. Select **Tabs**
4. Default two-tab structure appears

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_GIF-Adding_new_tab_block.gif)

### Adding additional tabs

1. Hover over tab bar, click **+ button**
2. Enter title (50 characters max)
3. Repeat as needed

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_GIF-Adding_additional_tabs.gif)

> **Note**:
> * Minimum two tabs required
> * Maximum 10 tabs per structure

### Supported elements inside tabs

* **Text formatting**: Headings (H2-H4), bullet lists, numbered lists, checklists
* **Images and videos**: Insert, resize, manage
* **Tables**: Add, customize rows/columns
* **Hyperlinks**: Insert, format for navigation
* **Callouts and private notes**: Add for specific users
* **Code blocks and inline code**: Technical references
* **Variables and snippets**: Reuse content across tabs
* **Glossary terms**: Terms with definitions (hover/click)
* **Enhancements**: Emojis, dividers, accordions, LaTeX equations

---

## Editing tabs

### Duplicating tabs

1. Click **Edit** icon next to tab name
2. Select **Duplicate tab**
3. New tab appears with same title, content, color. Edit as needed

### Changing tab names

1. Click **Edit** icon next to tab name
2. Hover over **Change tab name**
3. Enter new name (50 characters max)

### Deleting tabs

1. Click **Edit** icon next to tab name
2. Click **Delete tab**

Deleted tabs can be restored using **Undo** (Ctrl + Z).

> **Note**: Cannot delete tabs when only two exist

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_GIF-Editing_tabs.gif)

---

## Customizing tabs

### Changing tab background and border color

1. Select tab content block
2. Click **Tab background color** or **Tab border color**
3. Use color picker: Preset colors, HEX values, RGB values

Click **Clear** to remove applied colors.

> **Note**: Color applies to entire tab content block. No individual tab coloring.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_GIF-Customizing_tabs.gif)

### Moving tabs

1. Find tab under **Tabs** section
2. Hover over six-dot drag icon (left of tab name)
3. Click, hold, move tab to desired position
4. Release to drop

#### Considerations when moving tabs

* **Scrolling**: Drag toward dark grey area near arrows to scroll hidden sections

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_GIF-Scrolling_while_moving_tabs.gif)

* **Moving right**: Drag until blue line appears in target position center

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_GIF-Moving_tabs_to_the_right.gif)

* **Moving left**: Drag until blue line appears in center of tab immediately to the left

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_GIF-Moving_tabs_to_the_left.gif)

* **First position**: Drag near first tab until blue line appears on top

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_GIF-Moving_tabs_to_the_first_position.gif)

> **Note**: Drag slowly for better control to avoid accidental replacements## Viewing tabs in the Knowledge base site

Tabs appear in the Knowledge base site exactly as configured in the editor:

* Switch between tabs without refreshing the page
* Colors, titles, and layouts match across site, widgets, and extensions
* Mobile-friendly navigation
* PDF exports show tab contents sequentially with titles as headings

---

### FAQ

#### Can I create tabs within another tab?

No. Nested tabs aren't supported.

#### Can I include tab headings in the table of contents?

No. Tab headings don't appear in the table of contents.

#### Can I add page breaks inside a tab?

No. Page breaks are disabled within tabs.

#### Can I use tabs inside other editor components?

No. Tabs can't be placed inside tables, accordions, or callouts.

<a id="categories-and-subcategories"></a>

## Categories and subcategories

Categories and subcategories organize articles by topic in Document360. They function as folders for related content.

**Example:** A category called *Shipping Information* might contain subcategories like *Domestic shipping*, *International shipping*, and *Shipping rates*.

![Document360 interface showing categories, articles, and their publication statuses](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Catagory_n_subcategory_in_portal.png)

---

### FAQs

#### What are categories and subcategories?

Organizational structures that group related articles by topic for easier navigation.

#### How do categories and subcategories differ?

Categories cover broad topics. Subcategories provide specific divisions within those topics.

#### Why use subcategories?

They segment information into focused groups, improving understanding and navigation.

**Example:** If "Cars" is a category, subcategories like "Sedan," "SUV," and "Convertible" help users find specific content.

#### Can I customize categories and subcategories?

Yes. Team accounts can create, edit, and delete categories/subcategories. Icon customization is available.

> **Note**: Read *Managing categories* for details.

#### How do categories improve usability?

Logical groupings simplify browsing and reduce time spent searching unrelated content.

#### Can one article belong to multiple categories?

Yes. Use the **Replicate** option to display an article in multiple locations.

#### What's the best practice for naming?

Use clear, descriptive names. Avoid jargon. Keep it user-friendly.

#### How should I organize categories?

Structure based on logical relationships and user needs. Broad categories with specific subcategories work best.

**Example:** Document360's own knowledge base follows the portal's menu structure.

#### Can I set different access permissions?

Yes. Role-based access control restricts specific categories/subcategories. Without explicit settings, permissions inherit from parent categories.

#### Can I reorder categories?

Yes. Use the drag-and-drop icon to reorder categories and subcategories.

#### Why isn't my category visible?

Categories disappear from the site when:

* All articles are hidden or unpublished
* The category contains no articles

**Troubleshooting steps:**

* Enable JavaScript in browser settings
* Clear browser cache and cookies
* Update browser to latest version
* Test on different browser or device

Organizes related articles under common themes.

Secondary organizational level that structures content within primary categories.

<a id="managing-categories"></a>

## Managing categories

**Supported plans:** Professional, Business, Enterprise

Categories and subcategories are the backbone of knowledge base organization. Document360 provides tools for creating, renaming, deleting, and moving them.

Management features include icon customization, cloning, reordering, and starring categories for quick access.

---

## Creating a category

Four methods available in the Knowledge base portal:

1. **Top bar Create button**
2. **Flywheel icon**
3. **More icon** in Categories & Articles section
4. **Create button** in Folder/Index type category

![Options for creating categories in workspace](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Creating_a_categories.png)

**Method 1: Top bar Create button**

1. Go to **Documentation**
2. Click **Create** dropdown → **Category**
3. Enter **Name**
4. Choose position in **Nest category under** dropdown
5. Click **Reset** for root level
6. Select **Type** (Folder, Index, Page, or GitHub)
7. Click **Create**

**Method 2: Flywheel icon**

1. Go to **Documentation**
2. Hover below desired category → click **Flywheel** icon
3. Click **Category**
4. Enter **Name**
5. Choose position in **Nest category under** dropdown
6. Click **Reset** for root level
7. Select **Type**
8. Click **Create**

**Method 3: More icon in Categories & Articles**

1. Go to **Documentation**
2. Hover over desired category → click **More** icon
3. Enter **Name**
4. Choose position in **Nest category under** dropdown
5. Click **Reset** for root level
6. Select **Type**
7. Click **Create**

**Method 4: Create button in Folder/Index category**

1. Go to **Documentation**
2. Click desired Folder/Index category
3. Click **Create** dropdown → **Sub category**
4. Enter **Name**
5. Choose position in **Nest category under** dropdown
6. Click **Reset** for root level
7. Select **Type**
8. Click **Create**

![Creating new category panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Creating_a_category_panel.png)

### Subcategory levels

Maximum seven levels (1 root + 6 subcategories). Beyond this, **New category** is disabled.

![Subcategory level limits](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Category_manager-Subcategory_levels.png)

> **Note**
>
> * Deep hierarchies make navigation difficult without search
> * Document360 provides tags, search, related articles, and internal linking for discoverability

> **Tip**: Use up to three subcategory levels. Two is ideal.

---

## Changing category icon

Default folder icon can be changed to emoji for better visual communication.

1. Go to **Documentation**
2. Click folder icon or emoji next to desired category
3. Select emoji from popup window

> **Note**
>
> * Click 🚫 icon to revert to folder icon
> * Emoji styles vary by browser
> * Only Folder and Index type categories support icon changes

![Changing category icons](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_ScreenGIF-Changing_the_Category_icons.gif)

---

## Deleting a category

Four deletion methods:

1. **More** icon in Categories & Articles section
2. **More** icon in Folder/Index category
3. Bulk delete in Folder/Index category
4. Delete specific article/subcategory in Folder/Index category

![Delete options interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Deleting_Categories.png)

**Method 1: Categories & Articles section**

1. Go to **Documentation**
2. Hover over desired category
3. Click **More** icon → **Delete**
4. Confirm with **Yes**

**Method 2: Folder/Index category**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Click **More** icon → **Delete**
4. Confirm with **Yes**

**Method 3: Bulk delete**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Select checkboxes for articles/subcategories
4. Click **Delete**
5. Confirm with **Yes**

**Method 4: Specific item delete**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Hover over article/subcategory
4. Click **More** icon → **Delete**
5. Confirm with **Yes**

> **Note**: Deleting root category removes all subcategories and articles. Items stay in recycle bin for 30 days.

---

## Hiding and unhiding a category

Hide categories to restrict access to team accounts only. Hidden categories show strikethrough in Documentation window.

**Example**: Hide draft feature guides until ready for public release.

Four methods available:

1. **More** icon in Categories & Articles section
2. **More** icon in Folder/Index category
3. Bulk hide/unhide in Folder/Index category
4. Hide/unhide specific article/category in Folder/Index category

![Hide options interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Hiding_Categories.png)

**Method 1: Categories & Articles section**

1. Go to **Documentation**
2. Hover over desired category
3. Click **More** icon → **Hide**
4. To unhide, click **Unhide** icon

**Method 2: Folder/Index category**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Click **More** icon → **Hide**
4. To unhide, click **Unhide** icon

**Method 3: Bulk hide/unhide**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Select checkboxes for articles/subcategories
4. Click **Hide**
5. To unhide, click **Unhide** icon

**Method 4: Specific item hide/unhide**

1. Go to **Documentation**
2. Open desired Folder/Index category
3. Hover over article/subcategory
4. Click **More** icon → **Hide**
5. To unhide, click **Unhide** icon

> **Note**: Hiding a category hides all its subcategories and articles.

---

## Renaming a category

Categories and subcategories can be renamed anytime.

1. Go to **Documentation**
2. Open desired category/subcategory
3. Click category name to edit

   Alternative: Hover over category in Categories & Articles → **More** icon → **Rename**
4. Enter new name → Click **Update**

> **Note**: Renaming doesn't affect the category slug.

![Renaming category](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/13_ScreenGIF-Renaming_a_category.gif)

---

## Moving a category

Move categories across workspaces. All subcategories and articles move with the parent category.

Five methods available:

1. **Drag and drop** icon in Categories & Articles section
2. **More** icon in Categories & Articles section
3. **More** icon in Folder/Index category
4. Bulk move in Folder/Index category
5. Move specific article/category in Folder/Index category

![Move options interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Moving_a_category.png)

**Method 1: Drag and drop**

1. Go to **Documentation**
2. Hover over desired category
3. Drag and drop to new location

> **Note**: Can't move root category into its subcategory. Drag only works within same workspace.

**Methods 2-5: Using Move option**

1. Go to **Documentation**
2. Access category through desired method
3. Click **More** icon → **Move**
4. In **Move category** panel:
   * **Workspace**: Select destination workspace
   * **Category**: Select destination category
   * **Auto update referenced links**: Check to update internal links
5. Click **Move**

![Move category panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/11_Moving_a_category_panel.png)

---

## Cloning a category

Clone creates exact copies of content as new articles. Works within or across workspaces.

Three methods:

1. **More** icon in Categories & Articles section
2. **More** icon in Folder/Index category
3. Clone specific article/subcategory in Folder/Index category

![Clone options interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Cloning_categories.png)

**All methods follow same process:**

1. Go to **Documentation**
2. Access category through desired method
3. Click **More** icon → **Clone**
4. In **Clone category** panel:
   * **Name**: Enter clone name
   * **Workspace**: Select destination workspace
   * **Category**: Select destination category
   * **Auto update referenced links**: Check to update internal links
5. Click **Clone**

![Clone category panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/12_Cloning_a_category_panel.png)

> **Note**: Security restrictions apply based on destination workspace/category.

---

## Starring a category

Frequently used categories can be starred for quick access. Functions like a favorites section.

> **Note**: Categories, subcategories, and articles can all be starred.

**To star:**

1. Go to **Documentation**
2. Select desired category
3. Click **Starred** icon next to title

   Alternative: Hover over subcategory in Folder/Index overview → click **Starred** icon
4. For page categories, click **Starred** icon near title

![Starring category](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Starring_a_category.png)

**To unstar:**

**Method 1**: Direct removal
1. Navigate to category/subcategory
2. Click **Starred** icon to toggle off

**Method 2**: Remove from Starred section
1. Go to **Documentation** → **Starred**
2. Select categories to remove
3. Click **Remove from starred**

![Removing starred categories](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_ScreenGIF-removing_starred_categories.gif)

> **Note**: With category filter applied, article status only shows for page categories, not folders or index categories.

---

### FAQs

#### What category types can I create?

Folder, Index, Page, or GitHub.

#### Category limits?

1,000 categories per workspace.

#### Subcategory limits?

Seven levels total (1 root + 6 subcategories).

#### Title character limit?

150 characters including spaces.

#### Can I change category icons to emoji?

Yes, for Folder or Index types.

#### How to remove emoji?

Click 🚫 icon in emoji popup.

#### Do emoji styles vary?

Yes, by browser.

#### Purpose of hiding categories?

Restricts access to team accounts only.

#### How to identify hidden categories?

Strikethrough in Documentation section list.

#### Hide multiple subcategories?

Yes, select multiple in Folder/Index categories → click **Hide**.

#### Hide published categories?

Yes, available even after publication.

> **Note**: Hiding affects all subcategories and articles.

#### Move categories across workspaces?

Yes.

#### Does moving include subcategories/articles?

Yes, they move with the parent.

#### Move root into subcategory?

No.

#### Security restrictions when moving?

Yes, based on destination workspace/category.

#### What are cloned categories?

Exact content copies created as new articles.

#### Clone across workspaces?

Yes.

#### Create new content in cloned category?

Yes.

#### Change cloned category type?

Yes.

#### Purpose of starring?

Quick access to frequently used items.

#### Remove multiple starred items?

Yes, from Starred page.

#### Recycle bin retention?

30 days.

#### Renaming updates slug?

No, manual update required.

#### Best practices for naming?

Clear, consistent, user-focused, logical hierarchy, avoid repetition and abbreviations.

<a id="category-types"></a>

## Category types

**Supported plans:** Professional, Business, Enterprise

Categories organize related articles. Three main types available.

---

## Types of categories

**1. Folder**  
**2. Index**  
**3. Page**

> **Note**: Choose type during creation. Switch anytime as needed.

---

**Choosing category type during creation**

1. Navigate to desired category
2. Click **More** icon → **Add sub category**
3. Select category type
4. Click **Create**

![Choosing category type](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScrenGIF-New_Choosing_a_category_type_during_category_creation.gif)

---

### 1. Folder

Primary category type. Simple container for articles and subcategories.

* Customizable icons
* No separate URL/view
* Bulk operations supported: Hide, Unhide, Delete, Move, Star

**Knowledge base portal view**  
![Folder category portal view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-New_Knowledge_base_portal_view_%20for_folder_category_type.png)

### 2. Index

Article index with dedicated URL.

**Portal view**: Shows articles with title, contributors, update date, status, tags.

1. **Unique slug**: Shareable URL with redirection support
2. **Bulk operations**: Hide, Unhide, Delete, Move, Star

![Index category portal view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-New_Knowledge_base_portal_view_%20for_index_category_type.png)

**Site view**: Shows category title and article/subcategory count.

![Index category site view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-New_Knowledge_base_site_view_%20for_index_category_type.png)

### 3. Page

Functions like regular articles. Full editor capabilities.

* Create content using Markdown, WYSIWYG, or Advanced WYSIWYG
* Publish and manage like standard articles
* Customizable title and slug

**Portal view**  
![Page category portal view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-New_Knowledge_base_portal_view_%20for_page_category_type.png)

**Site view**  
![Page category site view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-New_Knowledge_base_site_view_%20for_page_category_type.png)

---

### FAQ

**Available category types?**

Folder, Index, Page.

**Change category type after creation?**

Yes, anytime.

**Change type process?**

1. Navigate to category
2. Click **More** icon → **Change type**
3. Select new type → **Update**

**Purpose of Index category?**

Provides article index with shareable URL.

**Switching Page to Index erases content?**

No, content remains intact.

**Folder category URLs?**

No separate URL/view.

**Operations in Folder categories?**

Bulk Hide, Unhide, Delete, Move, Star.

**Difference between article and Page category?**

Page categories can contain additional categories/articles.

<a id="assigning-drive-folder-for-a-category"></a>

## Mapping categories to Drive folders

**Supported plans:** Professional, Business, Enterprise

---

## Drive folder mapping

Images uploaded from local storage or URL automatically save to designated Drive folder for article's category/subcategory.

---

## Associating Drive folder to category

1. Go to **Documentation**
2. Hover over desired category → click **More** icon
3. Click **Set drive folder**

   **Set drive folder** panel appears.
4. Select Drive folder/subfolder
5. Click **Update**

Folder now mapped to category/subcategory.

![Mapping category to Drive folder](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Screenshot-Updated_mapping_category_with_drive_folder.gif)

---

### FAQ

**Map subcategories to Drive folders?**

Yes, available for all categories/subcategories.

**Difference from Editor folder?**

Mapped Drive folder takes precedence. Without mapping, images save to Editor folder.

**Article-level Drive mapping?**

No, only available for categories/subcategories.

**Change/remove Drive mapping?**

Yes, anytime. Previous images remain in original folder.

**Subcategory vs parent category mapping?**

Immediate mapping takes precedence. Subcategory mapping overrides parent.

> **Preference order:**
>
> 1. Subcategory Drive mapping
> 2. Parent category Drive mapping
> 3. Editor folder

<a id="downloading-category-and-article-in-kb-site"></a>

## Downloading categories and articles

**Supported plans:** Professional, Business, Enterprise

Generate PDF exports of entire categories/articles with customizable templates.

> **Note**: Exclusive to private projects and private workspaces in mixed projects (KB site 2.0).

---

## Enabling PDF download

1. Go to **Settings** → **Knowledge base site** → **Article settings & SEO** → **Article settings**
2. Enable **Show download as PDF button**
3. Check **Allow PDF template selection during export**

> **Note**: To manage templates, go to **Documentation** → **Content tools** → **Export to PDF** → **PDF template** section.

![Enabling PDF download button](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Settingup_Knowledge_base_portal_new.png)

---

## Downloading process

1. Navigate to category → click **More** icon in category manager
2. Click **Export PDF**
3. In **Export Articles** panel:
   * Select subcategories/articles
   * Choose template from dropdown (default if none selected)
4. Click **Export PDF**

> **Note**
>
> * Site customizations don't appear in downloaded PDF
> * Mixed projects: Private categories in public workspaces can't be exported

![Downloading PDF from KB site](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Downloading_PDf_on_KB_site.gif)

---

## PDF download links

* Single article: Instant download
* Multiple articles: Email link sent
* Link expires: 48 hours

![PDF download notification](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image(150).png)

---

### FAQ

**Exceed 500 MB daily limit?**

Downloads complete but further exports blocked for 24 hours. Purchase **KB PDF download quota** add-ons for more capacity.

**Increase download capacity?**

Purchase **KB PDF download quota** add-ons from billing section.

<a id="managing-articles"></a>

## Managing articles

**Supported plans:** Professional, Business, Enterprise

Articles are knowledge base building blocks. Document360 provides tools for efficient creation, editing, and organization.

---

## Creating articles

Information grouped into user-defined categories. Create from scratch, template, or import.

> **Article limits by plan:**
>
> * Professional: 5,000 articles/workspace
> * Business: 5,000 articles/workspace
> * Enterprise: 10,000 articles/workspace
>
> Contact support@document360.com for higher limits.

Four creation methods:

1. **Top bar Create button**
2. **Flywheel** icon
3. **More** icon in Categories & Articles section
4. **Create** button in Folder/Index category

![Article creation methods](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Creating_a_new_article.png)

**All methods follow similar process:**

1. Go to **Documentation**
2. Access creation method
3. Enter article **Name**
4. Select **Category**
5. Click **Create**

![New article panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Creating_a_new_article_panel.png)

---

## Creating article templates

Save any article as reusable template. New articles inherit properties and formatting.

**Example**: Standard troubleshooting format saves time and ensures consistency.

Three creation methods:

1. **Flywheel** icon
2. **More** option
3. **Top bar Create** button

![Article from template methods](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Article_from_template_methods.png)

**Process for all methods:**

1. Go to **Documentation**
2. Access template creation method
3. Select **Article from template**
4. Choose template from list (preview available)
5. Enter article name → select category
6. Click **Create**

   Name and slug auto-populate from template title.

![Article from template panel](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Article_from_template_panel.png)

> **Note**: Manage templates via **Templates overview** page. See *Templates* article for details.

---

## Editing articles

Essential for maintaining current, accurate content.

**Publishing changes:**
1. Article appears on KB site
2. Status changes from **Draft** to **Published**

Published articles show live version, not editing pane.

**Edit process:**
1. Go to article → click **Edit** button
2. **Article status** changes to **Draft**
3. Make changes
4. Click **Publish** to update site version

![Editing article interface](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Editing_an_Article.png)

### Markdown view

View Markdown formatting without creating new version:

1. Open published article in Markdown editor
2. Click **More** → **View markdown**
3. Click **Close markdown** when done

![Markdown view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_ScreenGIF-Markdown_view_of_a_published_article.gif)

---

## Locking articles

Automatic locking prevents conflicting edits during collaboration.

**Unlocking occurs when:**
* No activity for 15 minutes
* Click **Lock** icon → **Unlock**
* Navigate away from article

![Locking article](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/14_ScreenGIF-Locking_an_Article.gif)

---

## Deleting articles

Five deletion methods:

1. **More** icon in Categories & Articles section
2. **More** icon in article
3. Bulk delete in Folder/Index category
4. Delete specific article in Folder/Index category
5. Bulk delete in **All articles** section

![Article deletion methods](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_ScreenGIF-Deleting_an_article_methods.gif)

**All methods require confirmation:**
1. Go to **Documentation**
2. Access deletion method
3. Click **More** icon → **Delete**
4. Confirm with **Yes**

> **Note**: See *All articles* article for details.

---

## Hiding articles

Hide articles to restrict access to team accounts.

**Example**: Sales pricing documents hidden from public view.

Four methods:

1. **More** icon in Categories & Articles section
2. Bulk hide in Folder/Index category
3. Hide specific article in Folder/Index category
4. Bulk hide in **All articles** section

![Hiding articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_ScreenGIF-Hiding_Unhiding_the_articles.gif)

**Process:**
1. Go to **Documentation**
2. Access desired method
3. Click **More** icon → **Hide**
4. To unhide, click **Unhide** or **Show** icon

> **Note**: See *All articles* article for details.

---

## Renaming articles

1. Go to **Documentation**
2. Open article → click name to edit

   Alternative: Hover over article in Categories & Articles → **More** icon → **Rename**
3. Enter new name → click **Update**
4. If published, confirm in **Article details confirmation** panel

![Renaming article](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/13_ScreenGIF-Renaming_an_Article_update.gif)

---

## Moving articles

Move articles across workspaces. Five methods available:

1. **Drag and drop** in Categories & Articles section
2. **More** icon in Categories & Articles section
3. Bulk move in Folder/Index category
4. Move specific article in Folder/Index category
5. Bulk move in **All articles** section

![Moving articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_ScreenGIF-Moving_an_Article.gif)

**Process:**
1. Go to **Documentation**
2. Access desired method
3. Click **More** icon → **Move**
4. In **Move article** panel:
   * Select **Workspace**
   * Select **Category**
   * Check **Auto update referenced links**
5. Click **Move**

> **Note**: Security restrictions apply to destination workspace/category.

---

## Replicating articles

Display single article across multiple categories.

1. Go to **Documentation**
2. Hover over article → click **More** icon
3. Select **Replicate**
4. Choose destination category → click **Replicate**

Article appears in selected location. Edit only the source article.

> **Note**
>
> * Security restrictions apply to destination category
> * Replicated articles have limited editing options

![Replicating articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/11_Screenshot-Replicating_an_article.png)

---

## Cloning articles

Create exact content copies as new articles. Works within or across workspaces.

Two methods:

1. **More** icon in Categories & Articles section
2. **More** icon in Folder/Index category

![Cloning articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/12_Screenshot-Cloning_an_Article.png)

**Process:**
1. Go to **Documentation**
2. Hover over article → click **More** icon
3. Select **Clone**
4. In **Clone article** panel:
   * Enter **Name**
   * Select **Workspace**
   * Select **Category**
   * Check **Auto update referenced links**
5. Click **Clone**

> **Note**: Security restrictions apply to destination workspace/category.## Embedding Google Forms in articles

Add Google Forms directly into your articles using HTML embed code. Works in Markdown and Advanced WYSIWYG editors.

**Process:**
1. Open your Google Form
2. Click **Send** () in the top right
3. Go to **Embed** tab
4. Copy the embed code
5. Paste into your article using one of these methods:

**Markdown editor:**
* Use indent method (4+ spaces)
* Paste embed code directly

**Advanced WYSIWYG editor:**
* Switch to **Code View** () → paste embed code
* Or use **Insert** () > **Embed** > paste code

> **Note**: Google Forms embedding requires the form to be publicly accessible or shared with specific users.

![Embedding Google Forms in articles](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot_Embedding_google_forms.png)## Embedding Google Forms in articles

1. Go to [Google Forms](https://docs.google.com/forms/u/0/) and log in with your Google account.
2. Create a new form or select an existing one.
3. Choose the form you want to embed.
4. Click **Send** in the top right corner.
5. Select the **<>** tab to get the embed code.
6. Click **Copy** to copy the iframe code.
7. Return to your article in the Knowledge base portal.
8. In the **Markdown** editor, paste the iframe code directly.
9. In the **Advanced WYSIWYG** editor, click **Code view** and paste the iframe code.
10. The form will appear in your article.

After publishing, readers can interact with the form for surveys, feedback, or data entry.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Embedded_form_in_Advanced_WYSIWYG_editor.gif)

**Knowledge base site view**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Embedded_form_Knowledge_base_site.png)

---

### FAQs

**How do I embed a Google Form in my Knowledge base article?**

Use the Embed HTML code block in your article.

**What steps are needed to embed a Google Form?**

Create or select a form, copy the embed code, and paste it into your article.

**Can readers interact with embedded Google Forms?**

Yes, they can fill out and submit forms for data entry, surveys, or feedback.

<a id="embedding-a-drawio-diagram"></a>

## Embedding Draw.io diagrams

**Plans supporting Draw.io diagram embedding**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

**Diagrams.net** (Draw.io) is a web-based open-source diagramming tool for creating flowcharts, UML diagrams, entity relationships, network diagrams, and mockups.

> NOTE: All references to Diagrams.net or Draw.io refer to the same tool.

Diagrams.net uses Google Drive for storage. You can embed Diagrams.net images in Document360 using HTML and an autogenerated link from the app.

> NOTE: Diagrams stored on Google Drive, Dropbox, etc. are private by default. Make them public before embedding.

---

## Method 1: Using the embed option

1. Go to [Diagrams.net](https://www.drawio.com/).
2. Click **File** > **Embed** > **Image**.
3. Click **Embed**.
4. Click **Copy** to copy the image tag.
5. Return to the Knowledge base portal.
6. In the **Markdown** editor, paste the code directly.
7. In the **Advanced WYSIWYG** editor, click **Code view** and paste the code.

> NOTE: Adjust the diagram's height and width as needed.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Using_the_embed_option_Draw_io.gif)

---

## Method 2: Exporting as an image

1. Go to [Diagrams.net](https://www.drawio.com/).
2. Click **File** > **Export as** and choose your image format.
3. Click **Export**.
4. Enter a file name and save to your preferred location (Google Drive, OneDrive, Dropbox, GitHub, GitLab, or device).
5. Click **Download**.
6. Return to your Document360 article.
7. Click **Insert image** and select **From Upload/URL**.
8. Choose your image and click **Insert**.

> NOTE: See [adding images to articles](/help/docs/adding-images-to-articles) for more details.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Embedding_Draw_io_via_image_Export.png)

---

### FAQs

**Can I embed Draw.io diagrams in Document360?**

Yes, using HTML and an autogenerated link from Diagrams.net.

<a id="all-articles-overview-page"></a>

## All articles overview

**Plans supporting bulk operations**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

The **All articles** feature lets you perform bulk actions on multiple articles and page categories simultaneously. Available actions include publishing, previewing, copying links, hiding, moving, deleting, setting review reminders, checking live status, creating tags, machine translation, downloading as PDF, and deprecating articles.

For example, publish ten articles and two page categories simultaneously for a product launch by selecting them on the **All articles** page and clicking **Publish**.

> NOTE: The **All articles** page displays all articles and page categories.

---

## Managing multiple articles

1. Go to **Documentation** > **All articles**.
2. Use the dropdown to navigate between workspaces and languages.
3. Filter articles by status using the **All articles** dropdown.
4. Click **Export** to download the article list as CSV.
5. Use **Filter** to narrow results by Status, Date, or Tags. See [Using filter in All articles page](/help/docs/filter-bulk-operations).
6. Select articles to perform bulk operations:

   - **Publish**: Publish selected new or draft articles
   - **Publish later**: Schedule selected new or draft articles
   - **View preview/View in KB**: Preview new/draft articles or view published articles
   - **Copy link**: Copy links for selected articles
   - **Hide**: Hide selected articles from the Knowledge base site
   - **Move to**: Move selected articles to different categories or workspaces
   - **Delete**: Delete selected articles (sent to recycle bin for 30 days)
   - **Review reminder**: Set review reminders for selected articles
   - **Live article status**: Define status for selected articles
   - **Add tags**: Create and assign tags to selected articles
   - **Add labels**: Create and assign labels to selected articles
   - **Machine translate**: Automatically translate selected articles
   - **Download as PDF**: Download selected articles as combined PDF
   - **Deprecate**: Mark selected articles as deprecated

> NOTE: If a page category contains articles and subcategories, you cannot hide, move, or delete it. These options work only for categories without sub-articles.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-All_articles_Overview_page(1).png)

---

### FAQs

**Can I publish multiple articles at once?**

Yes, select articles on the **All articles** page and click **Publish**.

**Can I hide multiple articles simultaneously?**

Yes, select articles and use the **Hide** option.

**How does this feature improve efficiency?**

Bulk actions eliminate the need to perform operations individually.

**Can I reuse custom filters?**

Yes, save and reuse custom filters as needed.

**Can I change published articles to draft in bulk?**

No, but you can manually change each article's status individually.

<a id="filter-bulk-operations"></a>

## Using filters in All articles

**Plans supporting bulk operations**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

---

## Available filters

1. Go to **Documentation** > **All articles**.
2. Navigate workspaces and languages using the top dropdown.
3. Filter articles by status using the **All articles** dropdown.
4. Use basic or custom filters to narrow results.

Applied filters appear at the top and include:

1. Status
2. Review reminder
3. Starred
4. Visibility
5. Read receipt
6. Contributor
7. Category
8. Date
9. Tags
10. Labels

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-FIlters_in_All_Articles.png)

---

### Filter options

**Status**
- **All**: All articles regardless of status
- **Published**: Published articles
- **Scheduled**: Scheduled articles
- **Draft**: Draft articles
- **New article**: New articles
- **Broken links**: Articles with broken links (based on recent validation)
- **Deprecated**: Deprecated articles

**Review reminder**
- **All**: All articles
- **Fresh**: Articles without "Needs review" status
- **Stale**: Articles with "Needs review" status

**Starred**
- **All**: All articles
- **Starred**: Starred articles
- **Not starred**: Non-starred articles

**Visibility**
- **All**: All articles
- **Visible**: Articles visible on the Knowledge base site
- **Hidden**: Articles not visible on the site (strikethrough in portal)

**Read receipt**
- **All**: All articles
- **Enabled**: Articles with read receipt enabled
- **Disabled**: Articles with read receipt disabled

> NOTE: Read receipt is available only for Private and Mixed projects in KB site 2.0.

**Contributor**: Search and select team members.

**Category**: Filter by category or subcategory.

> NOTE: Category selection shows only articles under that category. Select subcategory articles manually.

**Date**: Filter by last updated date using presets or custom dates.

**Tags**: Search and select specific tags.

**Labels**: Search and select specific labels.

---

## Custom filters

Save custom filters for reuse.

> Example: Create a filter for team members with specific date ranges and status indicators.

Access saved filters using the arrow next to the **Filter** button.

---

### Saving custom filters

1. Go to **Documentation** > **All articles**.
2. Select filters and click **Apply**.
3. Click **Save filter**.
4. Enter a filter name (max 30 characters).
5. Enable **Share filter with team members** to make it available to others.
6. Click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Saving_a_Custom_filter.png)

---

### Deleting custom filters

1. Click the arrow next to **Filter**.
2. Hover over the filter and click **Delete**.
3. Confirm by clicking **Yes**.

> NOTE: Custom filters cannot be edited after saving. Deletion is permanent.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Deleting_a_custom_filter(1).png)

---

## Clearing filters

Three methods to clear filters:

1. Click **Clear all** at the top
2. Use the **Filter** dropdown and click **Clear**
3. Click **X** next to individual filters

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Clear_filters_in_All_articles_page.png)

---

### FAQs

**What filters are available?**

Status, Review reminder, Starred, Visibility, Read receipt, Contributor, Category, Date, Tags, and Labels.

**Can I save custom filters?**

Yes, for future reuse.

**How do I clear all filters?**

Click **Clear all** or use the Filter dropdown.

**Why isn't Read receipt available?**

It's only available for Private and Mixed projects in KB site 2.0.

<a id="export-bulk-operations"></a>

## Export article list

**Plans supporting export functionality**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Export articles and their status as CSV files. Filter fields before exporting.

> Example: Export published articles from a specific contributor over the last month.

---

## Export process

1. Go to **Documentation** > **All articles**.
2. Navigate workspaces and languages using the top dropdown.
3. Filter articles by status if needed.
4. Apply additional filters (Status, Review reminder, Starred, Visibility, Contributor, Category, Date, Tags, Labels).
5. Click **Export**.

The file downloads in CSV format with:

- Article title
- Category title
- Article status
- Date
- Portal URLs
- Site URLs

> NOTE: View the CSV file in Excel, Open Office, Google Sheets, Notepad, or any CSV-compatible application.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-Export_articles.png)

---

### FAQs

**How do I get article titles and URLs?**

Use the [API endpoint to get all article lists](https://apidocs.document360.com/apidocs/project-version-articles).

1. Enter required details in the API request
2. Execute the query

Find the Project Version ID using the [Get Project Versions endpoint](https://apidocs.document360.com/apidocs/get-project-versions).

**How do I export draft articles?**

You cannot export draft articles individually. Export the entire category containing them:

1. Go to **Documentation** > **All articles**
2. Filter by **Draft** status
3. Use the **Category** filter to select the category
4. Click **Export**

<a id="review-reminders"></a>

## Article review reminders

**Plans supporting review reminders**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Review reminders alert team members when articles need review, keeping content accurate and up-to-date.

---

## Setting individual review reminders

1. Open the desired article.
2. Click the **More** (•••) icon > **More article options**.
3. Select the **Review reminder** tab.
4. Choose a reminder date: Now, 30 days, 3 months, or Custom date.
5. Enter a review reason (optional, max 100 characters).
6. Click **Save**.

A **Needs review** tag appears next to the article slug. Hover to see the review reason.

![Creating review reminder](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Review_reminder_in_more_options.png)

---

## Clearing review reminders

1. Open the article.
2. Click the **Needs review** tag.
3. Click **Mark as reviewed**.

The tag disappears and the article reverts to its previous status.

![Clearing review reminder](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-clearing_review_reminder.gif)

---

## Bulk review operations

### Method 1: All articles page

1. Go to **Documentation** > **All articles**.
2. Filter by **Review reminder** > **Stale**.
3. Select articles.
4. Click **Mark as Reviewed**.
5. To mark articles as **Needs review**, select them, click **Review reminder**, and choose reminder days.

![Bulk review reminders](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGIF-Marking_multiple_articles_in_all_articles.gif)

---

### Method 2: Content tools

1. Go to **Documentation** > **Content tools** > **Documentation** > **Article review reminders**.
2. Click **Create review reminder**.
3. Enter reminder name, set frequency, and add reviewers.
4. Click **Next**.
5. Select workspace and language.
6. Choose articles and click **Set reminder**.

> NOTE: Use filters to find articles by category, contributor, tags, and date.

![Content tools review](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenGIF-Articles_review_reminder_in_content_tools.gif)

---

### FAQs

**How do I set review reminders for all articles?**

Go to **Documentation** > **Content tools** > **Documentation** > **Article review reminders**.

<a id="article-seo"></a>

## Article SEO

**Plans supporting SEO settings**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

SEO helps your articles gain visibility and reach target audiences effectively.

---

## Adding SEO metadata

1. Open the desired article.
2. Click **More** (•••) > **SEO**.
3. Go to the **SEO** tab.
4. Optionally select **Exclude from external search engine results**.
5. Enter the **Meta title**.

> NOTE: Keep meta titles between 5-60 characters for optimal visibility.

6. Edit the slug if needed.
7. Enter the **Description**.

Keep descriptions compelling, informative, and within 150-160 characters.

8. Use **Ask Eddy AI** to generate SEO descriptions.

![SEO settings](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Excluding_articles_from_External_search_engines.png)

> NOTE: Generate SEO descriptions for multiple articles via **Documentation** > **Content tools** > **Documentation** > **SEO description**.

---

## Editing meta titles

Meta titles define webpage titles, affect SEO rankings, and appear in search results and browser tabs.

1. Open the desired article.
2. Click **More** (•••) > **SEO**.
3. Edit the **Meta title** field.
4. Click **Save**.

The updated title appears on the Knowledge base site.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Editing_Meta_title.gif)

---

### FAQs

**Does updating SEO description in one language affect others?**

No, you must update each language manually.

**Why is AI SEO description generator disabled?**

Articles need at least 200 words.

**Why doesn't the article name update after renaming?**

Change the SEO meta title:

1. Click **More** (•••) > **SEO**
2. Update meta title and save

<a id="excluding-articles-from-searches"></a>

## Excluding articles from search engines

**Plans supporting search exclusion**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Exclude articles from search engine results to maintain content confidentiality.

---

## Excluding from external search engines

1. Open the article or page category.
2. Click **More** (•••).
3. Select **SEO**.
4. Check **Exclude from external search engine results**.
5. Click **Save**.

![External search exclusion](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Excluding_articles_from_External_search_engines.png)

---

## Excluding from internal searches

> NOTE: AI search suite is available for Business and Enterprise plans (new pricing). Legacy users need Eddy AI assistive search add-on for exclusion toggle.

1. Open the article or category page.
2. Click **More** (•••) > **More article options**.
3. Go to **Search Visibility** section.
4. Select options:
   - **Exclude from knowledge base search**: Hides from site search
   - **Exclude from Eddy AI assistive search**: Hides from AI search
5. Click **Save**.

![Internal search exclusion](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Excluding_articles_from_Eddy_AI_assistive_and_Search_engines.png)

> NOTE: Articles remain accessible via URL or navigation menu even when excluded from searches.

---

### FAQs

**What happens to cloned articles?**

Search visibility settings copy to cloned articles.

**What about hidden articles?**

Hidden articles are automatically excluded from all searches.

<a id="changing-the-url-of-an-article"></a>

## Changing article URLs

**Plans supporting URL changes**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

By default, articles convert titles to slugs for URLs.

Example: "This is a really good content" becomes `docs.yourcompany.com/[project version]/docs/this-is-really-good-content`.

> NOTE: Changing article titles doesn't automatically update slugs.

---

## Method 1: Article settings

1. Open the desired article.
2. Click **More** (•••) > **More article options**.
3. Go to **SEO** tab.
4. Update the slug field.
5. Click **Save**.

> NOTE: Apply redirection rules for new slugs. See [Article redirect rules](/help/docs/article-redirect-rules).

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Changing_theURL_for_an_Article.png)

---

## Method 2: Editor slug field

1. Open the article.
2. Click the slug field next to the article status badge.

![Slug editor](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/article%20slug%202.png)

3. Update the URL slug.
4. Click **Update**.
5. Confirm redirection in the prompt.
6. Deselect checkbox to skip redirect rules.

> NOTE: Redirect rules are optional but recommended to avoid broken links.

---

### FAQs

**What's the default URL format?**

Based on article titles converted to slugs.

**Does title changes update slugs?**

No, slugs must be updated manually.

**Should I apply redirect rules?**

Recommended to maintain link functionality.

**Why use special characters in URLs?**

They make URLs more intuitive, language-specific, and SEO-friendly for German and other languages with umlauts.

**Why do special character URLs break?**

Special characters require percent-encoding. Copy URLs directly from the portal, not browser address bars.

**Can I use numbers in URLs?**

Yes, update slugs to numeric values following the same process.

<a id="article-tags"></a>

## Article tags

**Plans supporting tags**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Article tags are keywords users might search for in your Knowledge base. Team members can use tags to search, filter, sort, and perform bulk operations.

> NOTE: Manage all tags via the **Tags** page. Same tags apply to articles, categories, and Drive files.

---

## Adding tags

1. Open the article.
2. Click **More** (•••) > **Tags**.
3. Create new tags or select existing ones.
4. Use **Ask Eddy AI** for AI-suggested tags (requires 200+ words).

> NOTE: AI tag generation requires 200+ words.

5. Click **Save**.
6. Click **Publish** > **Configure article settings**.
7. Add or remove tags as needed.
8. Click **Yes** to publish.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Adding_tags_in_the_articles.gif)

---

## Tag guidelines

1. Maximum 30 characters including spaces
2. Allowed characters:
   - Upper and lowercase letters (multi-language)
   - Numbers
   - Spaces
   - Special characters: **\_ + - @ # % ^ & ! ()**
3. Forbidden characters: **\ / : \* ? " < > |**

---

## Tags on Knowledge base site

Published tags appear on the site. Readers can click tags to see all associated articles and categories.

![Tags reader view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Tags%20readers%20POV.png)

![Tags reader view 2](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/tags%20readers%20pov%202.png)

<a id="adding-article-labels"></a>

## Article labels

**Plans supporting labels**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Labels streamline internal content management. Use them to sort, filter, and categorize articles efficiently.

Example: Filter release notes for updates using label filters in **All articles**.

> NOTE: Labels are internal only and supported across all plans.

---

## Adding labels - Method 1: Article editor

1. Open the article.
2. Click **More** (•••) > **Labels**.
3. Enter label name and press **Enter**.
4. Or select existing labels from dropdown.
5. Click **Add**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Adding_labels_in_the_article_editor.gif)

---

## Adding labels - Method 2: All articles section

1. Go to **Documentation** > **All articles**.
2. Select articles > **More** (•••) > **Add labels**.
3. Enter label name and press **Enter**.
4. Or select existing labels.
5. Click **Add**.
6. Use **Filter** > **Labels** to sort articles.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Adding_labels_in_the_All_articles_section.gif)

---

## Adding labels - Method 3: Workflow assignments

1. Go to **Documentation** > **Workflow assignments**.
2. Select articles and click **Add labels**.
3. Enter label name and press **Enter**.
4. Use **Labels** filter to narrow results.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGIF-Adding_labels_in_workflow_assignment.gif)

---

## Adding labels - Method 4: Starred section

1. Go to **Documentation** > **Starred**.
2. Select articles and click **Add labels**.
3. Enter label name and press **Enter**.
4. For individual articles, hover > **More** (•••) > **Add labels**.
5. Click **Add**.
6. Use **Labels** filter to narrow results.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenGIF-Adding_labels_in_Starred_articles.gif)

---

## Adding labels - Method 5: Category pages

1. Open the desired category.
2. Hover over articles > **More** (•••) > **Add labels**.
3. Or select multiple articles > **Add labels**.
4. Enter label name and press **Enter**.
5. Click **Add**.

![Category labels](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_ScreenGIF_Adding_labels_from_category.gif)

---

### FAQs

**How many labels per project?**

Up to 10,000 labels.

**How many labels per article?**

Up to 10 labels.

**Can I reuse labels?**

Yes, across multiple articles.

**What's the difference between tags and labels?**

Tags appear on both portal and site for user navigation. Labels are internal only for team organization.

**Can I search articles by labels?**

No direct search, but you can filter by labels in **All articles**.

**Can I label images and videos?**

No, labels work only for articles.

**Do labels appear on the site?**

No, they're internal portal features.

<a id="related-articles"></a>

## Related articles

**Plans supporting related articles**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Related articles help readers navigate between connected content. They appear at the bottom of articles on the Knowledge base site.

> NOTE:
> - Only published articles can be related
> - Related articles appear only on the site, not in widgets

---

## Adding related articles

1. Go to **Documentation** and open any article.
2. Click **More** (•••) > **Related articles**.
3. Search for articles using keywords.
4. Click **X** to clear search terms.
5. Click **+** next to articles to add them.
6. Added articles appear under **Added articles**.
7. Click **X** to remove articles.
8. Click **Save**.

You can also add related articles during publishing:

1. Click **Publish**.
2. Expand **Configure article settings**.
3. Find **Related articles** section.
4. Click **Yes** to save and publish.

---

## Eddy AI recommendations

1. Click **Ask Eddy** for AI-suggested related articles.

> NOTE: AI recommendations require 50+ words.

2. Suggestions appear under **Suggested articles from Eddy AI**.
3. Click **+** to add articles to related list.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Related_articles.gif)

> NOTE: After purchasing Eddy AI, use **Ask Eddy AI** button below search bar for [AI-powered recommendations](/help/docs/ai-related-articles-recommender).

---

## Auto relate feature

Enable **Auto relate this article to all related articles** in **Article settings** to automatically link articles.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenShot-Related_articles.png)

---

### FAQs

**What if readers can't access related articles?**

Only accessible articles appear in the related section.

<a id="featured-image"></a>

## Featured images

**Plans supporting featured images**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Featured images are thumbnails used primarily for SEO and link previews when sharing articles externally.

---

## Adding featured images

1. Open any article.
2. Click **More** (•••) > **More article options**.
3. Select **Featured image** tab.
4. Click **Upload an image**.
5. Select image from Drive and click **Save**.

> NOTE: Image recommendations:
> - **Size**: 1200x800 to 2000x1200 pixels
> - **Format**: High-quality JPEG or PNG

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Adding_Feature_Image_in_Articles.gif)

<a id="attachments"></a>

## Attachments

**Plans supporting attachments**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

---

## Adding attachments

1. Open any article.
2. Click **More** (•••) > **More article options**.
3. Select **Attachments** tab.
4. Add external file URLs or click **Upload an attachment** for Drive files.
5. Select files and click **Insert**.
6. Reorder using drag handles.
7. Click trash icon to remove attachments.

Attachments appear near Table of Contents and Tags on the Knowledge base site.

![Adding attachments](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Adding_attachment_in_the_Knowledge_base_portal.gif)

**Site view**

![Attachment site view](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Added_attachment_in_the_Knowledge_base_side.png)

<a id="status-indicator"></a>

## Status indicators

**Plans supporting status indicators**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Status indicators appear near article titles on the Knowledge base site: **New**, **Updated**, and **Custom**.

---

## Automatic updates

Enable **Automatically set article status** to update indicators automatically:

1. Go to **Settings** > **Knowledge base site** > **Article settings & SEO**.
2. Enable **Automatically set article status**.
3. Set duration in **Show article status for** field.

> NOTE: See [Category manager](/help/docs/knowledge-base-category-manager) for details.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Automatic_Status_Indicator_update.png)

---

## Manual updates

1. Open the article.
2. Click **More** (•••) > **More article options**.
3. Select **Status indicator** tab.
4. Choose status from dropdown.
5. Set duration in **Show status for** field.
6. Click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Manually_updating_status_indicator_in_an_Article.png)

---

## Custom status settings

**Text customization:**
1. Go to **Settings** > **Knowledge base portal** > **Localization & Workspaces** > **Localization variables**.
2. Expand **Category manager**.
3. Edit **Custom** field.
4. Click **Save**.

**Color customization:**
1. Go to **Settings** > **Article settings & SEO**.
2. Select **Article settings** tab.
3. Expand **Category manager**.
4. Choose color for **Custom status indicator**.
5. Click save icon.
6. Hover over color icon to preview.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Custom_Status_Indicator_color.png)

> NOTE: See [Category manager](/help/docs/knowledge-base-category-manager) for more details.

---

## Site view

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Status_Indicator_KB_site_View.png)

- **New** (green dot): First-time published articles
- **Updated** (orange dot): Edited and republished articles
- **Custom**: Manually set by teams

<a id="article-status"></a>

## Article status

**Plans supporting article status**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Article status helps identify article progress without checking each one individually.

Example: Content managers quickly find **Draft** articles needing editing or **Needs review** articles flagged for review.

> NOTE: Articles display status indicators (New/Updated/Custom) on the Knowledge base site. See [Status indicator](/help/docs/status-indicator).

---

## Portal status indicators

Articles show one of four statuses with color-coded icons in the left navigation:

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-All_four_article_status.png)

> NOTE: Status also applies to category pages.

**New article** (blue): Created but not yet published. Accessible only to team members.

> NOTE: Category pages show as **New category page**.

**Draft** (yellow): Published article being updated while original remains live.

**Published** (green): Public articles available to readers.

**Needs review** (pink): Articles flagged for review by contributors or automated reminders. See [Article review reminder](/help/docs/review-reminders).

---

## Hidden article status

Hidden articles show with strikethrough and aren't available on the Knowledge base site. They're accessible only through the portal.

> NOTE: Articles in hidden categories are also hidden.

---

### FAQs

**Purpose of article status?**

Identify article progress and streamline knowledge base maintenance.

**Available statuses?**

New, Draft, Published, and Needs review.

**What happens to "Needs review" articles?**

They're flagged for contributor review or automated reminders.

**Do categories show status?**

Yes, they follow the same status system.

<a id="preferences"></a>

## Article preferences

**Plans supporting preferences**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

---

## Updating preferences

1. Open any article.
2. Click **More** (•••).
3. Select **Preferences** tab.
4. Toggle options:
   - **Allow comments**: Enable Disqus comments
   - **Show table of contents**: Display article TOC
   - **Enable feedback**: Allow user feedback on articles
5. Click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Preference%20tab%20overview%20page(1).png)

<a id="showhide-table-of-contents-for-an-article"></a>

## Table of contents visibility

**Plans supporting TOC control**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Control TOC visibility at site level or individual article level.

---

## Site-level TOC control

1. Go to **Settings** > **Knowledge base site** > **Article Settings & SEO**.
2. Toggle **Show table of contents** in **Article right** section.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_TOC_artcilesettings.gif)

---

## Article-level TOC control

1. Open the article.
2. Click **More** (•••) > **More article options**.
3. Select **Preferences** tab.
4. Toggle **Show table of contents**.
5. Click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Article_TOC.gif)

---

### FAQs

**Can I control TOC for entire site?**

Yes, via site-level settings.

**How to control site-level TOC?**

**Settings** > **Knowledge base site** > **Article Settings & SEO** > Toggle **Show table of contents**.

**Can I hide TOC for individual articles?**

Yes.

**How to hide individual article TOC?**

1. Open article > **More** (•••) > **More article options**
2. **Preferences** tab > Uncheck **Show table of contents**
3. Click **Save**

**Do bold headings appear in TOC?**

No, only H2, H3, and H4 headings appear.

<a id="marking-articles-as-deprecated"></a>

## Marking articles as deprecated

**Plans supporting deprecation**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

---

## What is a deprecated article?

A deprecated article is obsolete and may no longer be relevant. Usually replaced by updated information.

Example: Mark articles about removed product features as deprecated to redirect readers to current resources.

---

## Deprecating individual articles

1. Open the article.
2. Click **More** (•••) > **More article options**.
3. Select **Mark as deprecated** tab.
4. Enable **Deprecated** toggle.
5. Enter deprecation reason (optional).
6. Use formatting options: Bold, Italics, Underline, Hyperlinks.
7. Click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Article_settings_deprecating_An_article.png)

---

## Bulk deprecation

1. Go to **Documentation** > **All articles**.
2. Select articles to deprecate.
3. Click **More** (•••) > **Deprecate**.
4. Enter deprecation message.
5. Click **Apply**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Deprecating_multiple_article_at_one_go.png)

---

## Site view

Deprecated articles show a **Deprecated** tag and highlighted message at the top.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-KB_Site_view_of_Deprecated_article.png)

<a id="updating-article-contributors"></a>

## Article contributors

**Plans supporting contributor management**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Document360 automatically tracks team members who create, update, or publish articles.

Readers can click contributor avatars to see other articles by the same team member.

---

## Managing contributors

1. In article editor, click **Article information** icon next to status badge.

> NOTE: Default avatars show for team members without profile photos.

2. Click **Manage** to open contributor management.
3. Remove contributors using the trash icon.
4. Add contributors by searching names/emails.
5. Click **Add as contributor** icon.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_GIF-Add_delete_contributors.gif)

---

## Missing contributor error

This warning appears when no contributors are assigned to an article.

> PRO TIP:
> - Manually add contributors for collaborative articles
> - Delete team accounts to completely remove contributors. See [Managing team accounts](/help/docs/managing-team-account).

**Resolution steps:**
1. Open the article.
2. Click **Article information** icon.
3. Verify contributors in **Contributors** section.
4. Click **Manage**.
5. Search and select contributors.
6. Click **Add as contributor**.
7. Save changes.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-No_contributor_error_resolving.gif)

<a id="schedule-publishing"></a>

## Schedule publishing

**Plans supporting scheduled publishing**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Schedule articles for publication at specific dates and times to plan content calendars and maintain consistency.

---

## Scheduling individual articles

1. Open the article.
2. Click dropdown next to **Publish** > **Publish later**.
3. Set **Date**, **Time**, and **Time zone**.
4. Add optional comments (max 160 characters).
5. Click **Schedule**.

> NOTE: Works for articles and page categories.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Setting_up_schedule_publishing.gif)

---

## Editing scheduled publications

1. Open the article.
2. Click **Scheduled** dropdown.
3. Click **Edit schedule** icon.
4. Modify **Date**, **Time**, **Time zone**, or comments.
5. Click **Schedule**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-editing_schedule_publishing.gif)

> NOTE: Click **Publish now** to publish immediately.

---

## Canceling scheduled publications

1. Open the article.
2. Click **Scheduled** dropdown.
3. Click **Cancel** icon.
4. Confirm with **Yes**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Cancel_schedule_publishing.png)

---

## Bulk scheduling

1. Go to **Documentation** > **All articles**.
2. Select articles.
3. Click **Publish later** or **Publish**.
4. Set **Date**, **Time**, and **Time zone**.
5. Click **Schedule**.

Scheduled articles show a **Publish later** icon. Hover to see scheduled date and time.

> NOTE: Publishing starts at scheduled time but may have slight delays.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenGIF-Schedule_publish_on_multiple_articles.gif)

---

### FAQs

**How to publish scheduled articles immediately?**

Click **Scheduled** dropdown > **Publish now**.

**Can I edit scheduled articles?**

No, cancel scheduling first to make edits.

**Can I publish scheduled articles via API?**

No, scheduled articles cannot be published via customer API.

**What happens when moving scheduled articles?**

Scheduling clears when articles move to different workspaces.

<a id="article-discussion-feed"></a>

## Discussion feed

**Plans supporting discussion feeds**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Every article and category has a Discussion feed for team conversations, mentions, and collaboration.

---

## Using discussion feeds

1. Open the article.
2. Click **Discussion feed** icon.

> NOTE: Called **Discussion** in Markdown/WYSIWYG editors, **Comments** in Advanced WYSIWYG.

3. Type comments in the text box and click **Send**.
4. Comments appear as bubbles with timestamps and profile names.

> NOTE: No character limit for comments.

**Mentioning team members:**
5. Use @ to tag team accounts.
6. Select the intended member from suggestions.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Overview_page_of_discussion_feedback.png)

> NOTE: Tagged members receive email notifications with article details and comments.

---

## Deleting feed messages

Hover over message bubbles to reveal **Delete** icons.

> NOTE:
> - Only you can delete your messages
> - Click **Undo** to restore accidentally deleted messages
> - Discussion feeds disable after article publication

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Deleting_the_feedback_in_feedback_discussion.png)

---

### FAQs

**How to add comments in Advanced WYSIWYG?**

Use inline comments feature. See [Reviewing articles with inline comments](/help/docs/reviewing-an-article-inline-comments).

**Why is discussion feed disabled?**

Feeds disable after publication. Click **Edit** to re-enable commenting.

<a id="revision-history"></a>

## Revision history

**Plans supporting revision history**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

---

## Article versioning

Versioning tracks changes, supports product versions, maintains edit history, enables collaboration, allows reverts, and ensures audit compliance.

When editing published articles, Document360 creates new unpublished versions while keeping old versions in history until new ones publish.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1734605317771.png)

This system lets admins, reviewers, and contributors compare versions and revert when needed.

> NOTE: New versions don't delete existing content. Team members manually delete old versions.<a id="creating-article-version"></a>

## Creating article versions

Two methods create new article versions:

#### Method 1: From the editor

1. Open a published article in the Knowledge base portal.
2. Click **Edit** in the top-right corner.

   A new unpublished version opens in the text editor.
3. Update content as needed.
4. Click **Publish** and confirm.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Revision_history.gif)

#### Method 2: Fork from revision history

1. Navigate to the article in the Knowledge base portal.
2. Click **More** (•••) and select **Revision history**.
3. Click **Fork** on the desired version.
4. Confirm by clicking **Yes**.

   Creates a new version with selected version's content.
5. Click **Open** on the latest version to edit.
6. Update content if needed.
7. Click **Publish** and confirm.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Revision_history.gif)

---

## Article revision actions

Available options in **Article revision**:

1. **Fork**: Creates new version from existing version. Opens article in Editor for content changes.
2. **Delete**: Removes article version. Action cannot be reversed.

> NOTE: Cannot delete published versions. Only unpublished versions are deletable.

3. **Open**: Opens version in Editor. Enables restoring previous versions to published state.
4. **Workflow history**: Shows version's workflow details including stages, assignees, comments, and dates.
5. **Publish**: Makes any previous version public by opening in editor and clicking Publish.

Detailed version information includes version number, contributor, creation date, and visibility status.

![revision history](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Workflow_history.png)

---

## Comparing article versions

Compare any two article versions:

1. Go to article in Documentation editor.
2. Click **More** (•••) and select **Revision history**.
3. Select checkboxes for versions to compare.
4. Click **Compare**.

![revision history](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Article_Version_comparision.png)

### Content highlighting

**Added content:**
* Highlighted in green
* Images, videos, code blocks, PDFs, and self-closing tags show green 'Added' badge
* Table changes highlighted in green
* Highlights remain visible during scrolling

**Removed content:**
* Highlighted in red with strikethrough
* Media elements show red 'Removed' badge
* Table removals highlighted in red
* Removed content stays visible in comparison view

**Formatting changes:**
* Highlighted in blue
* Non-text formatting changes (tables, images) show blue 'Modified' badge

> NOTE: Content block movements and multiple formatting changes are not highlighted. Multi-formatting means applying italic, bold, and underline to same content block.

**Swap versions:**
* **Swap** button near version dropdowns
* Reverses comparison order instantly
* Shows changes from both perspectives
* Updates view real-time without page reload
* Preserves all highlights, filters, and settings
* Version labels update to reflect new order

> NOTE: All highlights maintain after swap. Previously "added" content shows as "removed" and vice versa.

**Exit comparison:**
* **Exit compare** button in top-right corner
* Returns to main document view without page reload
* Maintains exact location before comparison

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_ScreenGif-Revision_history.gif)

---

### FAQs

#### Why are forked article timestamps out of order?

When older versions are opened and modified, timestamps reflect recent changes accordingly.

#### Can I restore previous article revisions?

* **Published articles**: Delete forked version with recent edits to restore last published version
* **Draft/new articles**: Fork earlier revision or delete forked version with recent edits

Forking before editing preserves original version for later restoration.

#### How do I discard current changes and revert?

**Method 1:**
* If unpublished, click **Revision history**
* **Open** previous version to restore old content

**Note**: Works only if article was published at least once.

**Method 2:**
* If never published, use Backup & Restore in **Settings**
* Restores specific article content

#### Can I change published/updated dates to past dates?

No. Published and updated dates always reflect actual modification times, regardless of article version age.

---

<a id="article-analytics"></a>

## Article analytics

**Plans supporting article analytics**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  | ✓ | ✓ |

Article Analytics provides detailed insights for individual articles unlike standard Analytics that cover the entire knowledge base. Track performance across reads, views, likes, dislikes, and link status to optimize content strategy.

---

## Accessing article analytics

1. In editor, click **More** (•••) in top-right corner
2. Select **Analytics** from dropdown

   Shows detailed metrics for **Reads**, **Views**, **Likes**, **Dislikes**, and **Link Status**

---

### Understanding metrics

Each metric measures different engagement aspects:

* **Reads**: Reader engagement based on scrolling, clicking, and time spent. Counts once per day per user.

> NOTE: Time spent varies by user activity. Multiple clicks count as single read with varying time sessions.

* **Views**: Unique clicks per browser, counted once per browser per user
* **Likes**: Total likes received, indicating content relevance
* **Dislikes**: Total dislikes, showing areas for improvement

> NOTE: All metrics begin tracking from article creation.

---

### Project-wide analytics

Click **Go to Analytics** for broader project-level insights.

![Update-Screenshot-Article_Analytics](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Update-Screenshot-Article_Analytics.png)

---

### Link validation

**Link status** shows total links with breakdown:

* **Working**: Active and accessible
* **Broken**: Unreachable or incorrect URLs
* **Unknown**: Status undetermined
* **Ignored**: Intentionally excluded from validation

Use link validation to maintain reliable article links:

1. From Article Analytics, locate **Link Status**
2. Click **Validate Now** to check status
3. Identify broken links and copy URLs
4. Update links or set redirection rules

**Example**: For broken external documentation links, copy URL and navigate to **Settings > Knowledge base site > Article redirect rules** to add new rule.

---

### FAQs

#### How often does analytics data update?

Real-time updates with daily read refresh based on unique user sessions.

#### Why do read counts differ from views?

Reads include engagement activities (scrolling, clicking) while views count unique browser clicks only.

#### Can article analytics improve content engagement?

Yes. Reads, Likes, and Dislikes metrics show which articles resonate most with your audience.## Subprocessors

Eddy AI uses these subprocessors to deliver service:

* **MongoDB**: Vector database
* **OpenAI**: AI models
* **Azure**: Cloud infrastructure
* **Stripe**: Payment processing
* **Segment**: Product analytics

---

## Data Security and Privacy

Data storage and transmission use encryption. Eddy AI ensures reliable performance under load.

* **Data at rest**: Encrypted with industry-standard protocols
* **Data in transit**: Encrypted to prevent interception

---

## Resources

### 1. Cryptography policy

**Purpose**: Ensure proper use of cryptography to protect confidentiality, authenticity, and integrity.

**Scope**: Applies to all Document360 systems storing or transmitting confidential data.

**Policy Owner**: CEO

**Effective Date**: March 1, 2024

**Risk Evaluation**: Document360 evaluates risks and implements cryptographic controls where appropriate.

**Encryption Standards**: Use strong cryptography with key management per industry standards (NIST SP 800-57).

**Key Management**: Keys and secrets are tightly controlled. Specifies key types, algorithms, and lengths for web certificates, ciphers, and endpoint storage.

**Exceptions**: Submit requests to CEO for approval.

**Violations & Enforcement**: Report violations to CEO. May result in disciplinary action, including termination.

**Version History**: Version 1.0, approved by Yasser ElSaid on February 3, 2024.

**Data at Rest**: Confidential data encrypted with AES-256 for maximum 1 year.

**Passwords**: Hashed with Bcrypt, PBKDF2, scrypt, or Argon2 using 256-bit key, 10K stretch, unique salt and pepper.

---

### 2. Incident Response Plan

**Purpose and Scope**: Manage information security incidents across the company.

**Definitions**: Security event (observable occurrence) vs. security incident (event causing data loss/damage).

**Reporting and Documentation**: Report suspected incidents immediately through designated channels. Document all incidents.

**Severity Levels**: 
* S1 (Critical)
* S2 (High) 
* S3/S4 (Medium/Low)

Clear escalation and response guidelines provided.

**Incident Response Team**: Led by IT Manager or VP of Support. Centralized "War Room" for coordination. Regular meetings update incident tickets and document indicators of compromise.

**Root Cause Analysis**: Critical incidents require analysis, documentation, and CEO review. CEO decides on post-mortem meetings.

**Response Process**: Triage, investigation, containment, eradication, recovery, hardening. Focus on lessons learned and improvements.

**Physical Security**: Address isolation and backup of affected systems.

**Breach Determination and Reporting**: Only CEO determines breach status. Promptly notify relevant parties per policies and regulations.

**External Communications**: Cooperate with customers, data controllers, authorities. Legal and executive staff determine approach.

**Roles and Responsibilities**: Document specifies responder roles and duties.

**Special Considerations**: Handle internal issues, compromised communications, root account compromises.

**Incident Status and Summary**: Template documents date, time, location, personnel, information type, indicators of compromise, root cause, actions taken.

**AWS Root Account Compromise Playbook**: Guidance for managing Root AWS account during compromise.

**Policy Owner and Effective Date**: CEO owns policy. Effective March 1, 2024.

---

### 3. Information Security Roles and Responsibilities Policy

**Objective**: Establish roles for protecting electronic systems and equipment.

**Policy Owner and Effective Date**: CEO owns policy. Effective March 1, 2024.

**Applicability**: All Document360 infrastructure, networks, systems, employees, contractors involved in security/IT.

**Audience**: All employees, contractors, partners, affiliates, temporary staff, trainees, guests, volunteers.

**Roles and Responsibilities**:

1. **Executive Leadership**:
   * Approve security program expenditures
   * Oversee risk management communication
   * Ensure compliance with GDPR, CCPA, SOC 2, ISO 27001
   * Review vendor contracts, oversee third-party risk

2. **VP of Engineering**:
   * Oversee development security
   * Implement security controls for development/IT
   * Conduct IT risk assessments, report to leadership

3. **VP of Customer Support**:
   * Manage security tools in customer environments
   * Ensure compliance with retention/deletion policies

4. **System Owners**:
   * Maintain system confidentiality, integrity, availability
   * Approve access and change requests

5. **Employees, Contractors, Temporary Workers**:
   * Protect health, safety, information resources
   * Identify risk management improvements
   * Report incidents, follow company policies

6. **Chief Human Resources Officer**:
   * Ensure qualified, competent staff
   * Oversee background checks, policy training, Code of Conduct
   * Evaluate performance, provide security training

**Policy Compliance**: Measured through reports, audits, feedback. Exceptions require CEO pre-approval. Non-compliance may lead to termination.

**Document Control**:
* **Version**: 1.0
* **Date**: February 3, 2024
* **Author**: Yasser ElSaid
* **Approved by**: Yasser ElSaid

---

### 4. Secure Development Policy

**Policy Owner and Effective Date**: CEO owns policy. Effective March 1, 2024.

**Purpose**: Design and implement information security within development lifecycle.

**Scope**: Applies to all business-critical Document360 applications and systems processing/storing/transmitting confidential data.

**Secure-by-Design Principles**:
* Minimize attack surface
* Establish secure defaults
* Apply least privilege
* Implement defense in depth
* Fail securely
* Avoid security by obscurity
* Keep security simple

**Privacy-by-Design Principles**:
* Proactive prevention
* Privacy as default
* Privacy embedded in design
* Full functionality without privacy compromise
* End-to-end security
* Full lifecycle protection

**Development Environment**: Segregate Production, Test/Staging, Development environments.

**System Acceptance Testing**: Establish testing programs and criteria. Complete Release Checklist before deployment.

**Protection of Test Data**: Carefully select, protect, control test data. Don't use confidential customer data without explicit permission.

**Change Control Procedures**: Changes require approval and oversight from multiple individuals.

**Software Version Control**: All software version controlled with role-based access restrictions.

**Policy Compliance**: Measured through reports, audits, feedback. Non-compliance may result in termination.

---

### 5. Code of Conduct Policy

**Policy Owner**: CEO

**Effective Date**: March 1, 2024

**Purpose**: Establish safe, inclusive environment for all staff.

**Scope**: Applies to all staff in all professional settings.

**Culture**: Promotes respect, collaboration, consideration.

**Expected Behavior**: Participate in respectful, collaborative workplace.

**Unacceptable Behavior**: Harassment, violence, discrimination, inappropriate conduct prohibited.

**Weapons Policy**: No weapons on company premises. Violations have strict consequences.

**Consequences**: Non-compliance results in immediate corrective actions and disciplinary measures.

**Responsibility**: CEO ensures staff adherence to policy principles.

---

### 6. Access Control Policy

**Policy Owner**: CEO

**Effective Date**: March 1, 2024

**Purpose**: Restrict access to authorized individuals per business objectives.

**Scope**: Applies to all Document360 systems handling confidential data for employees and external parties.

**Access Control Summary**:

**Identifying Users**: Access based on job roles and required competencies.

**Maintaining Authorization**: Document all privileged access allocations.

**Enforcing Security Measures**: MFA required for privileged access. No generic administrative IDs.

**Adopting Protocols**: Grant time-bound access permissions.

**Logging and Auditing**: Log and audit all privileged activities.

**User Access Reviews**: Regular reviews maintain appropriate identities.

**Access Control Policy**: Restrict access to authorized parties only.

**Password Management**: Implement secure log-on procedures.

**User Access Provisioning**: Grant access based on documented business requirements.

**Violations & Enforcement**: Report violations. Enforcement maintains compliance and security.

---

### 7. Data Management Policy

**Policy Owner**: CEO

**Effective Date**: March 1, 2024

**Purpose**: Classify, protect, retain, and dispose of information based on organizational importance.

**Scope**: Applies to all Document360 data, information, and systems.

**Data Classification**:

**Confidential**: Highest protection needed. Examples: customer data, PII, financials, strategic plans, technical reports.

**Restricted**: Thorough protection required. Default classification. Examples: internal policies, legal documents, contracts, emails.

**Public**: Intended for public consumption. Examples: marketing materials, product descriptions.

**Data Handling**:

**Confidential Data**:
* Restricted access to specific employees/departments
* Must encrypt at rest and in transit
* No storage on personal devices/removable media
* Requires secure storage and disposal

**Restricted Data**:
* Need-to-know access only
* Management approval for external transfer
* Secure storage and disposal mandatory

**Public Data**: No special protection required.

**Data Retention and Disposal**:
* Retain data per business, regulatory, contractual requirements
* Securely delete confidential/restricted data when unnecessary
* Delete or de-identify PII when no longer needed

**Annual Data Review**: Management reviews retention requirements annually.

**Legal Requirements**: Data under legal hold exempt from standard requirements. Retain per legal counsel instructions.

**Policy Compliance**: Measured through business tool reports and audits.

**Exceptions**: Require CEO approval.

**Violations & Enforcement**: Report violations to CEO. May result in termination.

---

### 8. Operations Security Policy

**Policy Owner**: CEO

**Effective Date**: March 1, 2024

**Purpose and Scope**:
* Ensure secure operation of information processing systems
* Applies to all critical Document360 systems and third-party entities with network access

**Documented Operating Procedures**: Technical and administrative procedures documented and accessible.

**Change Management**:
* Document, test, review, approve significant changes before deployment
* Emergency changes require retrospective review and authorization

**Capacity Management**:
* Monitor and adjust processing resources and storage
* Include human resource capacity in planning and risk assessments

**Data Leakage Prevention**:
* Classify information per Data Management Policy
* Train users on proper handling
* Use DLP tools based on risk assessment

**Web Filtering**:
* Implement DNS/IP blocking for risky websites
* Block malicious content/command servers unless business-necessary

**Separation of Environments**:
* Strictly segregate development, staging, production
* Don't use confidential production data in development/test without approval

**Systems and Network Configuration**:
* Follow configuration and hardening standards
* Review production access rules annually

**Protection from Malware**:
* Implement detection, prevention, recovery controls
* Use anti-malware software on all endpoints and emails

**Information Backup**: Design backup processes ensuring customer data recovery per SLAs.

**Logging and Monitoring**: Implement logging and monitoring for incident detection and response.

**Control of Operational Software**: Manage installation and use per established rules.

**Threat Intelligence**: Collect and analyze threats for actionable intelligence.

**Technical Vulnerability Management**: Identify, assess, address vulnerabilities timely.

**Restrictions on Software Installation**: Establish rules for secure software installation.

**Information Systems Audit Considerations**: Plan audits to minimize business disruptions.

**Systems Security Assessment**: Include security requirements in system acquisition/changes.

**Data Masking**: Implement data masking for PII and sensitive data based on risk assessment.

---

## Data Privacy

We maintain strict data handling practices:

* **Data Privacy Compliance**: Signed DPA with OpenAI outlining privacy commitments. [DPA details](https://ironcladapp.com/public-launch/63ffefa2bed6885f4536d0fe)
* **AI Models**: Use OpenAI's ChatGPT 3.5 and GPT-4 for Eddy AI performance
* **Privacy Adherence**: Feature follows OpenAI privacy policies through API integration
* **Data Transmission**: Send data via OpenAI APIs. OpenAI policy states: "OpenAI will not use customer API data to train models." Data retained maximum 30 days for analytics, then deleted

> **NOTE**
>
> Read complete [**OpenAI API data usage policies**](https://openai.com/enterprise-privacy/)
>
> For Document360 data policy queries, see [**Privacy policy**](https://document360.com/privacy/)

---

## AI Writer Suite

**Plans supporting AI writer suite**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Suite offers AI tools for content creation, SEO optimization, FAQ generation, and related content recommendations within the knowledge base portal.

---

## Features in the AI Writer Suite

1. [**AI writer**](/help/docs/ai-writer)
   1. **Outline creation**: Generate structured article outlines
   2. **Make longer/Make shorter**: Adjust content length
   3. **Change tone/Change voice**: Modify tone or switch active/passive voice
   4. **Split sentences**: Break complex sentences for readability
   5. **Convert speech**: Switch direct/indirect speech
   6. **Improve it**: Enhance clarity and impact
   7. **Convert into table**: Format lists/paragraphs as tables

2. [**AI FAQ generator**](/help/docs/ai-faq-generator): Create FAQs from article content

3. [**AI title recommender**](/help/docs/ai-title-recommender): Generate engaging title suggestions

4. [**AI SEO description generator**](/help/docs/seo-description-generator): Create search-friendly descriptions

5. [**AI tag recommender**](/help/docs/ai-tag-recommender): Suggest relevant content tags

6. [**AI related articles recommender**](/help/docs/ai-related-articles-recommender): Recommend connected articles

7. [**AI Chart generator**](/help/docs/ai-chart-generator): Generate pie charts, flow charts, tables

8. [**AI alt text generator**](/help/docs/ai-alt-text-generator): Create accessibility descriptions for media

---

## Multilingual Support for Eddy AI Writer Suite

Eddy AI supports 16 languages in the knowledge base:

* English variants: en, en-US, en-GB, en-AU
* French (fr)
* Spanish (es)
* German (de)
* Norwegian (no)
* Dutch (nl)
* Portuguese (pt)
* Swedish (sv)
* Italian (it)
* Korean (ko)
* Finnish (fi)
* Polish (pl)
* Arabic (ar)
* Hebrew (he)
* Danish (da)
* Brazilian Portuguese (pt-br)

Features unavailable for unsupported workspace languages like Chinese.

---

## Plan Availability and Usage Limits

Professional, Business, and Enterprise plans include full AI Writer Suite access. Freemium plan excludes these features.

Monthly credit limits apply:
* **Make longer/Make shorter/Outline creation/Change tone**: 5,000 credits
* **SEO description generator/Title recommender**: 1,000 credits
* **Other features**: Unlimited within paid plans

Platform notifies users approaching limits.

---

## AI Writer

**Plans supporting AI writer**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Eddy AI offers content enhancement tools. Launch with **Ctrl + Spacebar**.

> **NOTE**: Trial accounts enable all Eddy AI features by default.

---

## Prerequisites

Ensure project subscription supports AI writer (disabled by default):

1. Navigate to **Settings** > **AI features** > **Eddy AI**
2. Enable **AI writer** toggle

> **NOTE**:
> * [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)
> * Browser extensions may interfere. Disable ad blockers, password managers, pop-up blockers if experiencing issues

---

## Accessing AI Writer Actions

Available actions:
* Outline creation
* Improve it
* Change tone
* Convert speech
* Change voice
* Make longer
* Make shorter
* Convert into table
* Split sentence
* [AI chart generator](/help/docs/ai-chart-generator)

> **NOTE**: Available only in Advanced WYSIWYG editor

**Usage**:
1. Select text (minimum 10 words) in Advanced WYSIWYG editor
2. Click **Eddy AI** option and choose desired action

**Outline creation**: Generate structured outlines from content or prompts. Review and modify as needed.

**Improve it**: Refine grammar, semantics, clarity, phrasing.

*Original*: "The system is highly effective because it works well in most cases."

*Improved*: "The system is very efficient as it performs effectively in the majority of situations."

**Change tone**: Modify tone for different audiences. Options: Professional, Friendly, Casual, Straightforward, Confident.

*Original*: "The team will proceed with the update as soon as possible."

*Friendly*: "The team is excited to get started on the update and will do so as soon as possible!"

*Professional*: "The team will initiate the update at the earliest opportunity."

**Convert speech**: Switch direct/indirect speech.

*Direct*: "He said, 'I will definitely complete the task by tomorrow.'"

*Indirect*: "He said that he would definitely complete the task by the following day."

**Change voice**: Switch active/passive voice.

*Active*: "The team successfully completed the project within the specified date."

*Passive*: "The project was successfully completed by the team within the specified date."

**Make longer**: Expand text with elaborated details.

*Original*: "Document360 is a knowledge base platform with several advanced features."

*Expanded*: "Document360 is a comprehensive knowledge base platform equipped with a wide array of advanced features that cater to the diverse needs of users..."

**Make shorter**: Condense text without losing essence.

*Original*: "The Document360 platform provides a robust set of features, including version control, multi-language support, analytics, and a powerful AI-assisted search, which helps streamline the knowledge management process."

*Shortened*: "The Document360 platform offers version control, multi-language support, analytics, and a powerful AI-assisted search to streamline knowledge management."

**Convert into table**: Format content as tables.

**Split sentence**: Break complex sentences for readability.

*Original*: "Document360 is an advanced platform, and it offers numerous features, including analytics, version control, and AI assistance, making it ideal for managing knowledge bases efficiently."

*Split*: "Document360 is an advanced platform. It offers numerous features, including analytics, version control, and AI assistance. These features make it ideal for managing knowledge bases efficiently."

---

## FAQs

#### What subscription plans support the AI writer suite?

Professional, Business, and Enterprise plans.

#### How can I activate the Eddy AI feature?

Navigate to Settings > AI features > Eddy AI and enable the AI writer toggle.

#### What actions can I perform using the AI writer?

Make text longer/shorter, create outlines, change tone, convert speech, improve text, convert to tables, change voice, split sentences.

#### Is the AI writer available in all editors?

No, Advanced WYSIWYG editor only.

#### Will my data be secure when using Eddy AI?

* Follows OpenAI privacy policies through API integration
* OpenAI policy: "OpenAI will not use customer API data to train models"
* Data retained maximum 30 days for analytics, then deleted

> Read [**OpenAI API data usage policies**](https://openai.com/policies/api-data-usage-policies)
> See [**Document360 Privacy policy**](https://document360.com/privacy/) for queries

#### Can I use the AI writer features multiple times in a month?

Yes, content creation features have 5,000 monthly uses limit.

#### What should I do if I encounter issues with the AI writer?

Disable interfering browser extensions.

#### Are there any best practices for using the AI writer features?

Review generated content for relevance, use features to elaborate/simplify text, ensure tone matches audience.

#### How many AI credits do my plan support?

5,000 monthly credits in Professional, Business, and Enterprise plans. Contact support to increase limits.

**API**: Rules allowing software applications to communicate.

---

## AI FAQ Generator

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Automatically creates FAQs with answers from article content in Advanced WYSIWYG editor.

---

## Prerequisites

* Purchase Eddy AI content suite
* Enable AI writer suite (enabled by default)

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## AI FAQ Generator in Advanced WYSIWYG Editor

1. Navigate to article in Advanced WYSIWYG editor
2. Click **Eddy** icon in toolbar
3. Choose **Generate FAQs**

> **NOTE**:
> * Minimum 150 words required
> * Generated FAQs placed at article end

---

## Customizing Generated FAQs

Edit FAQ section title. Click FAQ section for options:

1. **Settings**: Adjust template settings for specific article
2. **Regenerate**: Create new FAQs from current content
3. **Expand/Collapse**: Show/hide answers
4. **Delete**: Remove entire FAQ section

---

## Adding Custom FAQs

1. Hover between FAQs where adding new one
2. Click **Add question** icon
3. Fill in custom question and answer

To delete specific FAQ:
4. Click FAQ to remove
5. Select **Delete** icon above it

---

## Locking FAQs

Protect FAQs from regeneration changes:

1. Click Lock icon next to FAQ
2. Locked FAQs marked with badge
3. Manual editing still possible

To generate additional FAQs while preserving current ones:
1. Lock existing questions
2. Click **Regenerate** for new relevant FAQs

> **NOTE**: FAQ templates differ from AI FAQ generator. See [Advanced WYSIWYG editor](/help/docs/advanced-wysiwyg-editor-basics) article.

---

## Setting up FAQ Generator

Customize settings at project level:

1. Navigate to Settings > Knowledge base site > Article settings & SEO
2. Expand **FAQ** accordion

---

## Customization Options

1. **Expand/Collapse**:
   * **Expand first**: First FAQ expanded by default
   * **Expand all**: All FAQs expanded
   * **Collapse all**: All FAQs collapsed

2. **Style**:
   * **With border**: Border around all FAQ sides (default)
   * **Without border**: Bottom border only (except last accordion)

3. **Expand arrow position**: Right or left (default: right)

4. **Expand/Collapse icons**: Arrow up/down or plus/minus options

---

## FAQs

#### What languages does the AI FAQ generator support?

English only.

#### How do I add a custom FAQ between generated FAQs?

Hover between FAQs, click icon, select from dropdown.

#### What is the minimum number of questions generated?

Typically 5-10 questions depending on content depth.

#### Can I edit AI-generated FAQs?

Yes, select and modify as needed.

#### Is there a usage limit?

5,000 monthly uses. Contact support to increase limit.

---

## AI Title Recommender

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Generates optimized titles using NLP to analyze content and suggest options capturing key information while maintaining context.

---

## Prerequisites

* Article content must exceed 50 words after preprocessing
* Sufficient Document360 credits (1 credit per recommendation)

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Using Article Title Recommender

**Suggest Title** available in article title section for new articles.

For published/draft articles:
1. Click article title to display **suggest title** feature
2. Click **Ask Eddy AI** button

Three AI-generated suggestions appear. Click **Generate more suggestions** for additional options.

Choose preferred title and click **Choose**, or **Cancel** to close.

**Key options**:
* **Suggested titles**: Three options per click. Select with radio button
* **Share feedback**: Upvote/downvote suggestions to improve feature
* **Save/Cancel**: Save selected title or cancel. 1 credit consumed per **Suggest title** click regardless of saving

---

## Credit Usage and Limits

* 1 credit per **Suggest title** click, even without saving
* Monthly limits per subscription plan

> **NOTE**: 1,000 monthly credits for title recommender across Professional, Business, Enterprise plans. Contact support for additional credits.

* Credits don't automatically renew monthly

---

## What are Preprocessed Words?

**Preprocessing** excludes elements from word count:

* HTML tags
* Images
* URLs/links
* Code blocks

Example: 220-word article may drop below 50 preprocessed words. Ensure content exceeds 50 preprocessed words for Title recommender.

---

## Data Privacy

Prioritize knowledge base data privacy. Title Recommender uses OpenAI integration, adheres to OpenAI privacy policies.

Policy extract: "OpenAI will not use customer API data to train models or improve services."

* [Full OpenAI API policy](https://openai.com/privacy)
* See Document360 Privacy Policy for company data practices

**API**: Rules allowing software applications to communicate.

---

## AI SEO Description Generator

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Streamlines meta description creation for articles and category pages. Generates concise, relevant descriptions optimizing search engine visibility and click-through rates.

---

## Prerequisites

1. **Sufficient credits**: Required per description generated
2. **Preprocessed content**: Exceed 200 words after excluding HTML tags, images, URLs, code blocks
3. **Access permissions**: **Ask Eddy AI** button available to authorized team members only

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Using SEO Description Generator

For individual articles/category pages:

1. Navigate to article/category in Knowledge base portal
2. Click **More** icon at top-right, select **SEO**
3. Expand **SEO** section, click **Ask Eddy AI**
4. Review generated description, click **Save**

> **PRO TIP**: Double-check generated descriptions for accuracy and audience alignment.

---

## Generating SEO Descriptions for Multiple Articles/Category Pages

1. Navigate to Documentation > Content tools > Documentation > SEO description
2. Select workspace from project dropdown
3. Ensure selected language is English
4. View all articles/category pages in workspace/language

> **NOTE**: Preprocessed word count shown next to names. Generate descriptions only for content exceeding 200 preprocessed words.

5. Filter articles by SEO availability, category, contributor, tags, last updated
6. Select eligible articles, click **Ask Eddy AI**
7. Review descriptions, click **Yes** to save

> **PRO TIP**: Prioritize high-traffic cornerstone content for maximum SEO impact.

---

## Best Practices for SEO Meta Descriptions & Titles

**Meta Descriptions**:
1. **Concise (155-160 characters)**: Brief yet informative
2. **Include relevant keywords**: Primary and secondary naturally
3. **Align with user intent**: Answer audience queries
4. **Make actionable**: Use calls like "Learn more," "Discover"
5. **Unique per page**: Avoid duplicate content issues
6. **Avoid keyword stuffing**: Maintain natural flow

> **PRO TIP**: Focus on clarity and relevance. Meta descriptions don't directly impact rankings but significantly improve click-through rates.

**SEO Titles**:
1. **Optimal length (50-60 characters)**: Prevent truncation
2. **Include primary keywords**: Preferably at beginning
3. **Reflect content accurately**: Avoid misleading users
4. **Make engaging**: Use compelling language
5. **Avoid redundancy**: Keep clear and straightforward
6. **Brand inclusion (optional)**: Add brand name if space allows

---

## FAQs

#### Why is SEO description generator essential?

Effortlessly generate optimized meta descriptions for articles and category pages based on content.

#### What is a meta/SEO description?

Summarizes article/category page content appearing in search results. Improves SEO, discoverability, organic traffic.

#### How are credits associated with SEO description generator?

1 credit per generated description. 50 articles require 50 credits.

#### Does Document360 offer free credits?

Yes, 10 free credits for paid projects. Trial plan excluded.

#### Why does article word count vary from preprocessed count?

Preprocessed count excludes HTML tags, images, URLs, code blocks. Editor count includes all elements.

#### What happens generating SEO description for article with existing description?

1 credit consumed. Generated description replaces current one.

#### Can I generate different meta descriptions with same content?

No, identical content produces same description. 1 credit consumed per generation.

#### Can I manually update SEO title and description?

Yes, through SEO description overview page or individual article settings.

#### Can I generate SEO descriptions for non-English articles?

Currently English-only. Manual additions possible for other languages.

#### Do search engines crawl SEO descriptions of private articles?

No, private articles remain uncrawled.

#### What is credit validity?

Credits valid for project lifetime.

#### Do credits affected by subscription plan changes?

No.

#### Does Document360 refund unused credits?

No.

#### Can I generate SEO titles with SEO description generator?

No, generates meta descriptions only. Use AI title recommender for SEO titles.

#### Can I switch languages in SEO description module?

Yes, but generator works English-only.

#### How many SEO descriptions can I generate?

**Soft limits**:
* Professional: 1,000 descriptions/month
* Business: 1,000 descriptions/month
* Enterprise: 1,000 descriptions/month

#### Is data security maintained?

Yes, follows OpenAI privacy policies. OpenAI doesn't use customer API data for training.

> Read [**OpenAI API data usage policies**](https://openai.com/policies/api-data-usage-policies)
> See [**Document360 Privacy policy**](https://document360.com/privacy/) for queries

**API**: Rules allowing software applications to communicate.

---

## AI Tag Recommender

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Suggests relevant tags using AI to analyze content and identify keywords/topics. Helps categorize content for easier discovery by team members and readers.

---

## Prerequisites

* **Preprocessed article content**: Must exceed 50 words
* **Access permissions**: Required for tag generation

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Accessing Recommended Tags for Articles

1. Navigate to article in Knowledge base portal
2. Click **More** at top right next to Publish button
3. Select **Tags** to open Article settings page
4. Click **Ask Eddy AI** button

AI-suggested tags appear in **Eddy AI recommends** section.

> **NOTE**: Minimum 200 words required for AI tag generation

5. Select suitable tags, click **Save**
6. Reopen article settings to regenerate tags

> **NOTE**: Tag recommendations also appear in Publish confirmation prompt. Expand **Configure article settings**, click **Ask Eddy AI** in Tags section before publishing.

---

## What Does Preprocessing Mean?

Preprocessing excludes specific elements when generating tags:

* HTML tags
* Images
* URLs/links
* Code blocks

Example: 80-word article may reduce below 50 preprocessed words. Ensure content exceeds 50 preprocessed words for tag generation.

---

## Why Tagging Matters

Essential for content management in large knowledge bases. Tags categorize articles by themes/topics, improving search precision and discoverability. Groups related content benefiting internal teams and external users.

---

## Best Practices for Content Management

1. **Create consistent tagging structure**: Establish guidelines for uniform tag usage across articles
2. **Use specific, relevant tags**: Avoid broad terms like "Update." Specify "Security Update" or "Feature Update"
3. **Limit tag count**: Use 3-5 key tags per article for focused searches
4. **Review and update tags regularly**: Modify outdated tags for efficient retrieval
5. **Group content using tags**: Cluster related articles (e.g., "Onboarding," "Troubleshooting," "Product Features")
6. **Leverage AI tag recommender**: Maintain consistent, relevant tagging across team-managed content

---

## FAQs

#### Who can generate tags?

Team accounts with combinations:
* Update article settings + Manage Tags
* Publish article + Manage Tags
* Update article settings + Publish article + Manage Tags

#### Can I generate tags for multiple articles simultaneously?

No, one article at a time currently.

#### Does AI tag recommender consume credits?

No, unlimited usage without credit limitations.

#### Can I add tags manually?

Yes.

#### Can I disable tag recommendations?

No.

---

## AI Related Articles Recommender

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Automatically associates relevant articles based on current content. Enhances user experience through quick access to connected information.

---

## Prerequisites

* Preprocessed content must exceed 200 words
* Required access permissions and credits

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Accessing AI Related Article Recommender

1. Navigate to Documentation in Knowledge base portal
2. Select published/unpublished article
3. Click **More** option, select **Related articles**

If existing related articles, view list below search bar.

4. Click **Ask Eddy AI** for recommendations

> **NOTE**: Minimum 50 words required

5. Click **Add** icon for desired articles
6. Enable **Auto relate this article to all related articles** toggle if needed

> **NOTE**: When enabled, bidirectional relationships created. Saves time adding related articles.

7. Click **Save** after changes

> **NOTE**: For bulk knowledge base additions, see [Dynamic related article recommendation](/help/docs/ai-dynamic-related-articles-recommendation)

---

## Accessing AI Related Article Recommender in Publish Checklist

1. Click **Publish** on desired article
2. Expand **Configure article settings** section
3. Scroll to **Related articles** section
4. Click **Ask Eddy AI** for recommendations
5. Click **Add** icon for desired articles
6. Click **Yes** when done

---

## Viewing Related Articles in Knowledge Base Site

Eddy AI-generated related articles appear in **Related articles** section at article bottom. Readers click to navigate directly to connected resources.

---

## FAQs

#### How many related articles can Eddy AI generate?

Maximum 3 related articles at once.

#### Can I manually add related articles alongside AI recommendations?

Yes, manual additions complement AI suggestions.

#### Will previously added related articles be overwritten?

No, AI suggests additional articles without affecting existing ones.

**Knowledge base portal**: Platform where project members manage and create content. Allows category/article/template creation, file/team/reader management, site configuration (branding, domain, security).

---

## AI Chart Generator

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Converts text into visual formats (pie charts, flow charts). Streamlines chart creation, eliminates third-party tools, saves time generating visual aids directly in articles.

---

## Prerequisites

* Active Eddy AI content suite subscription
* Enabled AI writer suite in Document360 account
* Text/table must be within article main body (not comments or captions)

> **NOTE**: [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Creating Charts from Text

1. In Advanced WYSIWYG editor, highlight content for chart conversion
2. Click Eddy AI option in floating bubble menu, select **Generate**
3. Choose chart type: Pie chart, Flow chart, Table
4. System creates chart from highlighted text. Regenerate up to 10 times if unsatisfactory
5. Replace selected text or insert chart below as image

> **NOTE**: Error message "No results found. Please revise content or add more context" appears if generation fails. Dismiss by clicking elsewhere or close button.

---

## Creating Charts from Tables

1. Highlight table for conversion
2. Click Eddy AI option in floating bubble menu, select **Generate**
3. Choose chart type: Pie chart, Flow chart, Table
4. System creates chart. Regenerate up to 10 times if needed
5. Replace table or insert chart below as image

---

## Customizing Charts

Edit appearance using Document360 image editing options:

* **Alignment and positioning**: Adjust via bubble menu
* **Edit chart**: Crop, resize, annotate through editor options

> **NOTE**: Charts cannot be directly edited once inserted. Undo action, update content, regenerate different result, or try different chart type.

* **Undo option**: Use Ctrl+Z to restore original content if replacing with unsatisfactory chart

---

## Supported Chart Types

* **Pie charts**
  * **Use case**: Show distribution of parts within whole. Visualize proportions, categories, percentages
  * **Example**: Display task completion percentages by team members

* **Flow charts**
  * **Use case**: Map processes, workflows, decision sequences. Illustrate step-by-step procedures
  * **Example**: Outline document approval process or user onboarding workflow

* **Tables**
  * **Use case**: Present structured data for comparison. Display datasets, comparisons, metrics
  * **Example**: Compare product features or user feedback across categories

---

## File Naming Convention

Generated charts follow standardized naming: AI-generated context plus chart type. Example: **sales_data_pie_chart.png**

---

## FAQs

#### Can I edit a generated chart?

No direct editing. Regenerate with updated content or different chart type.

#### What causes chart generation failure and how to fix?

Failures from:
1. Insufficient/incomplete data
2. Unsupported content (comments, captions)
3. Formatting issues or data limits

Fix by providing structured lists, numeric data, or logical groupings (region, product type). Revise content and retry.

#### Where are generated charts saved?

Final charts saved in Document360 Drive for reuse. Located in **Images** > **Documentation**

#### How many regeneration attempts allowed?

Up to 10 times including chart type switching.

#### Are all chart versions saved?

No, only final inserted chart saved in Drive. Regeneration versions discarded unless inserted.

#### Is undo available after replacing content with chart?

Yes, use Ctrl+Z to restore original content.

#### Does AI Chart generator consume Eddy AI credits?

Yes, each generation/regeneration deducts 1 credit from monthly allowance.

---

## AI Alt Text Generator

**Plans supporting feature**: Professional, Business, Enterprise

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

> **NOTE**: Legacy plan users require Eddy AI content suite add-on purchase.

---

## Alt Text Importance

Writing alt text improves accessibility and discoverability:

* Appears when images fail to load
* Assists visually impaired users with screen readers
* 20% of Google searches are image-based
* Optimized alt text enhances user experience, accessibility, search rankings

Document360's Eddy AI alt text generation suggests concise, accessible descriptions automatically. Example: **Document360's settings dashboard with configuration options**.

Combines accessibility with search optimization for impactful visual content delivery.

> **NOTE**:
> * Enabled by default if AI writer enabled
> * 5,000 alt texts monthly limit
> * Supports images <20MB in JPEG, JPG, PNG, WEBP formats
> * English language only
> * Accuracy limitations with panorama, fisheye, monochrome images
> * [Supported languages](/help/docs/ai-writer-suite#multilingual-support-for-eddy-ai-writer-suite)

---

## Generating AI Alt Text in Advanced WYSIWYG Editor

1. Navigate to article in Advanced WYSIWYG editor
2. Use `/image` slash command or **Insert > Image**

Methods:
* **Upload from device**: Eddy AI generates alt text automatically
* **Choose from Drive**: 
  * Existing Drive alt text persists
  * Update/regenerate by clicking image, selecting Alt text icon
* **Drag and drop**: Eddy AI generates alt text automatically
* **External URL**: Enter URL. Eddy AI generates alt text automatically

3. To regenerate: Remove existing text, click **Generate**
4. For multiple images: Eddy AI generates for all. Regenerate individually
5. Review/edit generated alt text
6. Click **Insert** to add image to article

> **NOTE**: See [Inserting images in Advanced WYSIWYG editor](https://docs.document360.com/docs/adding-images-to-articles#inserting-an-image-advanced-wysiwyg-editor)

---

## Generating AI Alt Text While Copy-Pasting Images

1. Drag/drop or paste image into Advanced WYSIWYG editor
2. Click pasted image for floating menu
3. Select **Alt text** icon
4. In **Image alt text** field:
   * Enter manually
   * Click **Generate** for Eddy AI suggestion
5. Click save icon

---

## Generating AI Alt Text While Uploading to Drive

1. During image upload:
   * Enter alt text manually
   * Click **Generate** for Eddy AI suggestion

2. For multiple images:
   * Click **Generate** next to each image individually
   * Click **Generate for all images** for bulk processing

---

## Generating AI Alt Text for Uploaded Drive Images

1. Navigate to **Drive** in Knowledge base portal
2. Click desired image for **File details** panel
3. In **Alt text** section:
   * Click **Generate** for Eddy AI alt text
   * To regenerate: Remove existing text, click **Generate** again
4. Click **Update** to save changes## Try This Feature

Explore this feature with an interactive demo below and see how it works in real time.

---

## Frequently Asked Questions

### How many AI alt texts can I generate per month?

You can generate up to 5,000 alt texts per month per project.

### Is the AI alt text generation feature enabled by default?

Yes, this feature is enabled by default if the AI writer is enabled.

### Can I review and edit the generated AI alt text?

Yes, you can review and edit the generated alt text before accepting it.

### How do I generate AI alt text when uploading an image to Drive?

When uploading an image to Drive, click the **Generate** button next to the alt text field to create AI-generated alt text.

### How do I regenerate AI alt text for an image?

To regenerate alt text, delete the existing alt text. The **Generate** button will reappear for Eddy AI regeneration.

### What happens if the Generate button is disabled?

If the **Generate** button is disabled, your monthly AI credit balance has been exhausted. Contact your admin or Document360 support.

### What happens if I try to upload multiple images but don't have enough credits?

If your available credit balance is insufficient for all images in a single upload, the **Generate all** button will be disabled.

For example, if you upload 10 images but only have 5 credits, the **Generate all** option will not be available. However, you can manually select up to 5 images (or as many as your credits allow) and click **Generate** to create alt text for the selected images.

### Can AI generate alt text for all image formats?

AI can only generate alt text for images smaller than 20 MB in JPEG, JPG, PNG, and WEBP formats.

### What if I copy-paste an image in an article? How can I add alt text?

If the article is in Advanced WYSIWYG editor, you can generate AI alt text for the image. Click the pasted image in the article to open a floating menu. Click the **Alt Text** icon, then **Generate** to create alt text. Click the save icon to confirm.

### Are KB customization images included in the alt text generation count in Drive?

No, only images from published articles with dependencies, as well as those from templates, snippets, and glossary, are counted.

---

## AI Search Suite

### Plans Supporting AI Search Suite

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

The AI search suite enhances user experience by integrating AI-powered tools that streamline search and content discovery. The suite includes three key features: Ask Eddy AI assistive search, Ask Eddy AI API, and an AI article summarizer, all designed to improve knowledge base navigation and content summarization.

---

## Features in the AI Search Suite

1. [**Ask Eddy AI assistive search**](/help/docs/ai-assistive-search-ask-eddy)

   This feature provides intelligent search, allowing users to ask questions directly and receive relevant, AI-curated answers. Machine learning enhances accuracy and speed of content retrieval, making knowledge base navigation more efficient.

2. [**Ask Eddy AI API**](/help/docs/ask-eddy-ai-api)

   This API provides a flexible, customizable solution, allowing seamless integration of GenAI search directly into your product's UI. Integration enables users to access Ask Eddy without navigating through product documentation, providing a streamlined experience.

3. [**AI article summarizer**](/help/docs/ai-article-summarizer)

   The AI article summarizer is integrated into the Knowledge base site to help users quickly get the gist of lengthy documents. This tool scans articles and condenses them into shorter summaries, providing key takeaways without reading the entire content.

4. [**Text to voice functionality**](/help/docs/text-to-voice-functionality)

   The text-to-voice feature allows users to listen to articles instead of reading them, saving time. This functionality is beneficial for multitasking, allowing users to absorb information while performing other activities.

---

## Multilingual Support for Eddy AI Search Suite

The Eddy AI search suite integrates with the Knowledge base site, offering support for multiple languages.

In addition to English (en, en-US, en-GB, en-AU), Eddy AI search suite supports 15 other languages: French (fr), Spanish (es), German (de), Norwegian (no), Dutch (nl), Portuguese (pt), Swedish (sv), Italian (it), Korean (ko), Finnish (fi), Polish (pl), Arabic (ar), Hebrew (he), Danish (da), and Brazilian Portuguese (pt-br).

If a workspace is configured with a language not supported by Eddy AI, such as Chinese, the search suite features will not be available for that workspace.

---

## Plan Availability and Usage Limits

1. **Ask Eddy search**: Included with 2,000 credits per month for the **Business** plan and 5,000 credits per month for the **Enterprise** plan. Each search query consumes 1 credit. Tailored for businesses with high AI-driven search needs. Contact support to purchase additional credits.

2. **Ask Eddy AI API**: Included with 2,000 credits per month for the **Business** plan and 5,000 credits per month for the **Enterprise** plan. Each API call consumes 1 credit. Enables enterprises to scale AI-powered search functionality seamlessly.

3. **AI article summarizer**: Included with 1,000 credits per month for **Business** and **Enterprise** plans. Each summarization task consumes 1 credit. Enhances content summarization efficiency for improved workflow management.

The AI search suite's flexible credit system ensures businesses can tailor usage to specific needs, providing scalable solutions for growing AI-enhanced search and content management demands. For more pricing information, click [here](https://document360.com/pricing/).

---

## AI Assistive Search (Ask Eddy AI)

### Plans Supporting AI Assistive Search

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

Ask Eddy AI is available on your home page and Knowledge base site's search bar. This AI assistant provides contextual answers to reader queries and prompts, helping users avoid searching through multiple articles.

> **NOTE**
> 
> * By default, Eddy AI assistive search retrieves answers from the main workspace. To access information from different workspaces, switch using the filter on your knowledge base site.
> * After updating published articles, Eddy AI assistive search takes approximately 15 minutes to fetch updated information.
> * For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

Ask Eddy AI extracts all information from your knowledge base, including textual content, code blocks, tables, content reuse elements, and LaTeX.

---

## Enable Ask Eddy AI for Your Knowledge Base Site

1. Navigate to **Settings** > **AI features** > **Eddy AI** in the Knowledge base portal.
2. Turn on the **AI assistive search** toggle.

Eddy AI begins indexing your Knowledge base content. Once complete, the Ask Eddy AI button appears on your Knowledge base site search bar and home page.

* The **KB site** checkbox enables Eddy AI for searches on the Knowledge base site (default selection).
* The **KB widgets & extensions** checkbox enables Eddy AI for widgets and third-party tool integrations.
* The **Public API** checkbox activates Eddy AI for all API endpoints using a single API token.

---

## Accessing Ask Eddy AI

> **For your information**
> 
> Conversational Eddy AI is available exclusively in **KB site 2.0**. To explore KB site 2.0 without impacting your existing Knowledge base, go to **Settings** > **Customize site**. For details, read the [KB site 2.0 migration](/help/docs/kb-site-20-migration) article.

1. Click the **Search bar** or press `Ctrl + K` on the Knowledge base site.
2. Start typing keywords. General search results appear.

> **NOTE**
> 
> If Ask Eddy AI is not enabled, only the standard search bar is available.

3. Press Enter. Ask Eddy AI generates results with source articles.
4. Click the **Copy** icon to copy generated content.
5. Provide feedback using the **Like** or **Dislike** icons.
6. Click **Source articles** to reference articles used by Eddy AI.

Source URLs are listed and numbered in the **Source articles** section. Numbers correspond to AI response citations for identification.

7. Hover over numbers to see additional information. For external sources, view webpage title and article description. Click the number or **Open in new tab** icon to view the source article.
8. Click desired source articles to open them in new tabs.

Eddy AI provides answers in the language of the question.

9. Choose workspace or all workspaces from filter dropdown to fetch results.

> **NOTE**
> 
> * Filtering workspaces during conversation resets generated results.
> * Eddy's response is contextual, based on the last five queries.

10. After first query and answer, click **Continue conversation with Eddy AI** text field to enter next query. Press Enter or click **Send** icon.

---

## Customize Eddy AI Localization Variables

1. Navigate to **Settings** > **Localization & Workspaces** in the Knowledge base portal.
2. Go to the **Localization variables** tab.
3. In the **Eddy AI** accordion, update variable values according to your desired language.

---

## Integrating Eddy AI in KB Widget with Multilingual Support

Access Eddy AI within your knowledge base as a widget in various languages: English (en-US, en-GB), French (fr), Spanish (es), German (de), Norwegian (no), Dutch (nl), Portuguese (pt), Swedish (sv), Italian (it), Korean (ko), Finnish (fi), Polish (pl), Arabic (ar), Hebrew (he), Danish (da). This ensures seamless user experience.

> For more information, read [Integrating Eddy AI in KB widget](/help/docs/knowledge-base-widget-getting-started).

---

## Enabling Eddy AI Credits Notification

Configure notifications for Ask Eddy AI credit balance:

1. Navigate to **Settings** > **Knowledge base portal** > **Notifications**.
2. Go to the **Notification mapping** tab.
3. In **Eddy AI notifications** accordion, turn on the **Credit usage alert** toggle.

Once enabled, Document360 sends reminders when credit balance drops to 20%, 10% of total allotted balance, and when balance expires.

---

## Data Privacy and Security

Document360's "Ask Eddy AI" utilizes OpenAI APIs in backend operations. Data transmits to OpenAI through their APIs. OpenAI's privacy policy prohibits using customer-submitted data via our API for training OpenAI models or enhancing OpenAI's service offerings. Both Document360 and OpenAI comply with GDPR regulations. Document360 is SOC 2 compliant.

OpenAI policy states: "OpenAI will not use data submitted by customers via our API to train OpenAI models or improve OpenAI's service offerings."

> Read complete [OpenAI API data usage policies](https://openai.com/policies/api-data-usage-policies).  
> For Document360 data policy queries, read our [Privacy policy](https://document360.com/privacy/).

---

## Frequently Asked Questions

### What data does Ask Eddy AI collect?

Ask Eddy AI does not collect Personal Identifiable Information (PII). We collect prompts (questions), Eddy AI's responses, citation articles, and feedback. This data is available in Eddy AI Search Analytics.

### What technology does Ask Eddy AI use?

Ask Eddy AI uses OpenAI APIs for functionality. Data sent via their APIs will not be used to train GPT models.

### Does Ask Eddy AI use external sources?

No, Ask Eddy AI relies solely on your knowledge base content. If insufficient information exists, Eddy AI responds with "I do not know."

### How do readers use AI-powered assistive search?

Knowledge base site users click the Ask Eddy AI button. A prompt input popup opens. They type queries to get tailored answers.

### How does Ask Eddy AI protect data?

We use industry-standard security practices, reputable subprocessors with SOC 2 compliance, and provide controls for organizations to meet data protection requirements.

### What does credit mean for Ask Eddy AI?

One credit equals one question (prompt). Standard offering includes 1,000 questions per month. Contact support or your customer success manager for additional credits.

### How does Ask Eddy AI work on private knowledge base?

Ask Eddy AI uses your access controls to generate appropriate responses based on user permissions. If users lack access to specific articles, Eddy AI responds with "I do not know."

### How quickly does Eddy AI reflect new content?

After updating articles, it takes around 15 minutes for Eddy AI responses to align with changes. Similarly, deleted articles take about 15 minutes to stop appearing in responses.

### Does Ask Eddy AI search within attachments?

Currently, Ask Eddy AI does not search within attachments. Content within PDF and Word documents is not indexed. This functionality will be supported in future releases.

### Does Eddy AI read Excel file data?

No, Eddy AI does not fetch or read information from files uploaded in articles.

### What happens if workspace language is French but questions are in English?

Eddy AI responds in English, matching the query language regardless of workspace language.

> **NOTE**
> 
> Eddy AI responds in the same language as the query.

### How do I check Eddy AI credit balance?

Admins/owners view remaining credits from **Settings** > **AI features** > **Eddy AI**.

Document360 sends reminders when credit balance drops to 20%, 10% of total allotted balance, and when balance expires.

### How do I purchase additional credits?

Navigate to **Settings** > **AI features** > **Eddy AI** and use the "Buy more" option. Trial version users cannot purchase add-ons.

### How do I configure email domain for Eddy AI notifications?

To receive Eddy AI credit notifications via email, configure your email domain: **Settings** > **Knowledge base portal** > **Notifications** > **Email domain**. Default sender is [support@document360.com](mailto:support@document360.com) if not configured.

### What notification channels support Eddy AI credits?

Receive Eddy AI credits notifications in English from webhook, Microsoft Teams, Slack, and email (if configured). For configuration details, read [Notifications](/help/docs/notifications).

### How do I configure email address for Eddy AI notifications?

After enabling Eddy AI credits notification toggle:

1. In **Notification channels** tab, click **New channel** and select SMTP.
2. Click **Next**.
3. Enter channel name and desired email address.
4. Add CC and BCC if required.

For more information, read [SMTP notification channel](/help/docs/smtp-email-notification-channel).

### Why is Eddy AI not available in API documentation?

Eddy AI is available only on Knowledge base site, not implemented for API documentation.

### Can Eddy AI answer questions requiring user login or involving restricted articles?

No, Eddy AI answers based on user's access control and permissions. If logged-in users lack access to specific articles, Eddy AI responds with *No results found*.

### Why is Ask Eddy AI button greyed out?

The Ask Eddy AI button becomes disabled when Eddy AI credit limit is reached. Renew credits to continue using this feature.

---

## AI Dynamic Related Articles Recommendation

### Plans Supporting AI Dynamic Related Articles Recommendation

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

This feature automatically links relevant articles across all content, ensuring readers find additional information related to their queries. Improves navigation and overall user experience. Apply related articles to your entire knowledge base in one instance.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

---

## Dynamic Related Articles Recommendation

> **For Your Information**
> 
> Available exclusively in **KB site 2.0**. To explore KB site 2.0 without impacting existing Knowledge base, go to **Settings** > **Customize site**. For details, read [KB site 2.0 migration](/help/docs/kb-site-20-migration).

Add related articles to all Knowledge base site articles:

1. Navigate to **Settings** > **AI features** > **Eddy AI**.
2. Turn on **Dynamic related article recommendation** toggle.

Eddy AI automatically adds related articles to all knowledge base site articles.

Additionally, manually add related articles:

1. Navigate to **Documentation** and select target article.
2. Click **More** option and select **Related articles**.
3. Click Ask Eddy AI. Eddy AI recommends related articles.
4. Click **Add** icon to include desired articles.
5. Turn on **Auto relate this article to all related articles** toggle if needed.
6. Click **Save**.

> **NOTE**
> 
> When **Auto relate this article to all related articles** is enabled, if Article-A is added as related to Article-B, then Article-B appears as related in Article-A. Save time using this toggle.

> **NOTE**
> 
> If **Dynamic related article recommendation** is not enabled:
> 
> * Users with permission see banner with **Enable recommendations** option, redirecting to Eddy AI settings.
> * Users without permission see **I'm Interested** button, emailing team account owner about feature interest.

---

## Knowledge Base Site View

After enabling Dynamic related article recommendation, all Eddy AI recommended articles display relevant related articles marked with an icon next to article names.

> **NOTE**
> 
> Eddy AI recommends up to three articles. If manually curated articles match Eddy's recommendations, number may vary.

---

## Frequently Asked Questions

### What is the Dynamic related articles recommendation feature?

Automatically links relevant articles across all knowledge base content, enhancing navigation and user experience.

### How do I enable Dynamic related articles recommendation?

Navigate to **Settings** > **AI features** > **Eddy AI** and turn on Dynamic related article recommendation toggle.

### Why are related articles not appearing for certain articles?

Feature uses algorithm to assess article relevance. Only articles meeting specific relevance threshold appear as related. If no similar articles found, recommendations cannot generate.

### How do I identify Eddy AI recommended articles?

Eddy AI recommended articles are marked with an icon next to article names. Manually added or Ask Eddy AI related articles do not show this icon.

---

## AI Chatbot

### Plans Supporting AI Chatbot

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

> **NOTE**
> 
> Legacy plan users need AI assistive search add-on for this feature.

Interact with Eddy AI Chatbot to get answers without searching Knowledge base articles. Helps find relevant information faster and easier.

> **NOTE**
> 
> * Available exclusively for KB site 2.0 projects.
> * For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

---

## Configuring Eddy AI Chatbot

Enable Eddy AI in Knowledge base widget:

1. Navigate to **Settings** > **AI features** > **Eddy AI**.
2. Turn on **AI assistive search** toggle.
3. Select **KB widgets & extensions** checkbox.

Configure Eddy AI Chatbot:

1. Navigate to **Widget** in Knowledge base portal.
2. Click **Add widget**.
3. Enter desired name (up to 30 characters) in **Widget name** field.

### Connection

4. In **Widget JavaScript** accordion, find **Widget key** and JavaScript code.
5. Click **Regenerate** icon to regenerate Widget key.
6. In **Connect domains** accordion, find domains where widget displays.
7. In **JWT** accordion, implement authentication configuration using JWT for secure private and mixed projects.

> **NOTE**
> 
> For more information, read [Securing Chatbot authentication using JWT](/help/docs/securing-chatbot-authentication-using-jwt).

### Customize Experience

8. Select **Chatbot** as widget type.

> **NOTE**
> 
> Widget type cannot be changed after selection and save.

9. In **Style widget** accordion, customize chatbot styles and themes.

> **NOTE**
> 
> For more information, read [Styling the Eddy AI Chatbot](/help/docs/styling-the-chatbot).

10. In **Content access** accordion, select content level access: **Project**, **Workspace**, or **Category**.

### Set Controls

11. In **Widget security** accordion, enter desired domain for exclusive widget display.

> **NOTE**
> 
> * Any project member installing chatbot on different domain must add domain to Widget security list.
> * Without domains in list, chatbot integrates into any SaaS application or public website.
> * www. not considered part of domain. Add only what follows www. in URL.
> 
> Example: [document360.com](http://document360.com)

12. Preview chatbot on right side of page.
13. Click **Save**.

Display created chatbot on Knowledge base site:

1. From widget page, hover over desired widget and click **Copy script** icon.
2. Go to **Settings** > **Knowledge base site** > **Integrations**.
3. Scroll to **Custom HTML** blade and click **Add**.

4. Enter desired description.
5. Select intended option in **Insert code** field.
6. Paste copied script and click **Add**.

Chatbot now appears on Knowledge base site.

> **NOTE**
> 
> To integrate into custom site, paste copied script into appropriate HTML file.

---

## Accessing Eddy AI Chatbot in Site

To access and interact:

1. Click chatbot icon to open.
2. Type question and click **Send** icon or press **Enter**.

Eddy AI retrieves information from Knowledge base to answer queries.

3. Hover over answers to **Copy**, **Like**, or **Dislike** responses.
4. Click **Clear** icon to clear conversation.

---

## Frequently Asked Questions

### How do I view Eddy AI Chatbot feedback?

To view feedback:

1. Navigate to **Analytics** > **Eddy AI**.
2. Filter desired chatbot using **Application** filter.

In **Feedback** section, see number of likes and dislikes received.

### What's the difference between Widget and Eddy AI Chatbot?

**Widget** allows manual navigation through articles or search functions. **Eddy AI Chatbot** engages users in conversation, offering immediate direct answers without manual navigation.

---

## Securing Chatbot Authentication Using JWT

### Plans Supporting AI Chatbot

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

JSON Web Token (JWT) is an open standard for securely transmitting information between parties as JSON objects. Enables authentication and information exchange with verified, trusted data. Implementing JWT for Eddy AI Chatbot creates secure environment for private and mixed projects, protecting sensitive information from unauthorized access.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

Implement authentication configuration using JWT for secure private and mixed projects:

1. Navigate to Knowledge base widget.
2. Click **Add widget** to create new widget.

Alternatively, hover over desired widget and click **Edit** icon to modify existing widget.

3. Select widget type as **Chatbot** to configure JWT.
4. In **Configure & connect** tab, go to **JWT** accordion and **enable** JWT toggle.

5. **Client ID:** Project's ID.
6. **Widget ID:** Unique ID for multiple widgets.
7. **Token endpoint:** HTTP endpoint for obtaining access token using authorization code.
8. **Client secret:** Click **Regenerate** to generate. Save for future use as applies to all future JWT-enabled widgets.

> **NOTE**
> 
> **Client Secret** required for all future JWT-enabled widgets. Not stored within Document360. Keep securely.

9. **Authorize URL:** Paste authorized URL from knowledge base widget webpage.

10. Click **Save**.

Embed authorized URL within code and paste into **Script section** of webpage to implement secure, authenticated Chatbot. Prevents unauthorized third-party access. Test thoroughly after configuration.

> **NOTE**
> 
> For more information on implementing auth endpoint, read [Managing the Knowledge base widget](/help/docs/managing-the-knowledge-base-widget).

---

## Frequently Asked Questions

### What should I check for authentication issues?

Ensure:
* Client secret and token endpoint correctly configured
* User authenticated before requesting endpoint

### What are common JWT pitfalls?

* **Failing to save client secret** after regeneration leads to authentication failures
* **Misconfiguring token endpoint** prevents successful token retrieval

### What if I lose my client secret?

Regenerate new client secret and update configuration accordingly.

### How do I verify JWT authentication works?

Test authentication flow by attempting to access Eddy AI Chatbot and checking for correct access token response.

---

## Styling the Chatbot

### Plans Supporting AI Chatbot

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

Customizing Eddy AI chatbot colors and icons to match brand creates seamless experience, making it easier for users to engage and get timely information.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

---

## Styling Eddy AI Chatbot

To style the chatbot:

1. Navigate to Knowledge base widget.
2. Hover over desired widget and click **Edit** icon.
3. In **Configure & connect** tab, expand **Style widget** accordion.

### Widget Color

4. Click **Change icon** to replace with image or select from available icons.

Choose any icon from **Icon set** tab.  
**OR**  
Click **Insert image** tab:
* Paste/type image URL and click **Insert**
* Upload image from Drive and select file

> **NOTE**
> 
> Click **Default** to revert to default icon and color.

5. Click **Change color** to update chatbot background color.

Select color using picker or enter hex, RGB, or HSL code for specific values.

### Widget Position

6. Select **Left** or **Right** to position widget icon.
7. Enter pixel values in **Side spacing** and **Bottom spacing** fields to adjust placement.

### Hide Widget

8. Turn on **Hide widget** toggle to hide on site.
9. Click **Save** after changes.

> **NOTE**
> 
> **Autosave** enabled when navigating between widget tabs, automatically saving changes.

---

## Adding External Sources for AI Assistive Search

### Plans Supporting External Sources in AI Assistive Search

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

> **NOTE**
> 
> Legacy plan users need AI assistive search add-on.

Configure AI assistive search to retrieve information from multiple external sources, simplifying process and delivering comprehensive answers.

Imagine a support agent for software company using Document360 to resolve customer issues. Previously, they could only search internal Knowledge base articles. With this feature, agent pulls information from external resources like company's public documentation site, blogs, and product release notes. Helps deliver accurate comprehensive answers quickly without leaving platform, improving response time and customer satisfaction.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

---

## Adding External Sources

To access and manage external sources:

1. Navigate to **Settings** > **AI features** > **Manage sources**.
2. Click **Add new** to add external source.

3. Choose source type: **Webpage** or **Sitemap**.

> **NOTE**
> 
> Add up to 50 **Webpages** and 1 **Sitemap**.

4. Enter source name.
5. Enter valid URL.

> **NOTE**
> 
> Webpages must be HTML5 format with `<article>` or `<main>` tags.

6. Click **Add source**.

---

## Manage Source Overview Page

**Manage source** page lists all indexed external sources.

Options available:

1. **Content access:** Restrict Eddy AI access to specific workspace and language. Options: **All** and **Allow selected**.
2. **Filter:** Filter sources by type: **All**, **Sitemap**, **Webpage**, or **Failed Sources**. Failed sources display sources with errors.
3. **Sync:** Sources sync every 24 hours. Click **Sync** to manually sync up to four times per day.
4. **Add new:** Click to add new source for indexing.
5. **Search:** Use search bar to locate sources by name.
6. **Type:** Displays source type: **Webpage** or **Sitemap**.
7. **Last sync:** Shows last sync date. Hover to view exact time.
8. **Status:** Toggle to enable/disable source. If disabled, Eddy AI stops fetching from that source.
9. **Error:** Denotes external source URLs with encountered errors.
10. **Delete:** Click **Delete** icon to remove source.
11. **Edit:** Click **Edit** to modify source name or URL.

---

## Enabling Eddy AI for Specific Workspaces, Languages, and Categories

Configure Eddy AI to selectively enable or restrict support for specific workspaces, languages, and categories.

1. Click **All** dropdown with two selections:
   * **All** - lists all workspaces
   * **Allow selected** - select workspace, languages, and categories

If **Allow selected**, **Manage workspace & category popup** appears.

2. Select workspace, languages, and categories for assistive search data access.

Manage button appears with Allow selected dropdown selection.

3. Click **Manage** to select/manage sources and click **Save**. Save button enabled only when changes made.

Modification confirmation popup shows 'AI search sources updated'.

4. Click **Cancel** or hit Esc to close popup.

> **NOTE**
> 
> Switching from **Allow selected** to **All** and back retains previous selections.

Feature applies across all AI Assistive Search enabled areas.

---

## Handling Errors in External Sources

If errors occur (unsupported HTML formats, languages, HTTPS issues), Eddy AI stops fetching from that page until resolved. For sitemap errors, Eddy AI continues fetching from remaining valid URLs.

1. Click **Error** icon next to status toggle.

Edit panel displays URLs and their errors.

2. Hover over URL and click **Open site** icon to view external source.
3. Click **Remove** to delete specific sitemap URL.
4. Click **Remove all** to delete all URLs with errors.

> **NOTE**
> 
> * If webpage has bot detection enabled, Eddy AI cannot crawl content. Source not added, forbidden error occurs.
> * Eddy AI supports only Server-Side Rendered (SSR) webpages. Client-side rendered pages may not index properly, leading to empty results. Use server-rendered content for accurate embedding.

---

## Knowledge Base Site View

When Eddy AI fetches from external sources:

1. Source URLs list and number in **Source articles** section. Same numbers used in AI response for identification.
2. Hover over numbers to find additional information. For external sources, view webpage title and article description. Click number or **Open in new tab** icon to view source article.
3. Click desired source articles to open in new tabs.

---

## Troubleshooting

### Unsupported Format While Adding Sitemap

**Error:** Unsupported format

Occurs when sitemap contains nested sitemaps with `<sitemapindex>` tag, exceeds 1 MB file size limit, or is unsupported format.

**Steps to resolve:**
* Use direct sitemap URL without `<sitemapindex>` tag (nested sitemaps not supported)
* Ensure sitemap file size is less than 1 MB
* Verify sitemap is supported format (XML)

### Forbidden Error While Adding Webpage

**Error:** Forbidden

Occurs when webpage source has bot detection or security mechanisms preventing Eddy AI crawling.

**Steps to resolve:**
* Check if source link has bot detection mechanisms. Contact website administrator for crawler access if needed
* Use different source without crawling restrictions

### Only HTML5 Documents with `<article>` or `<main>` Tags Supported

**Error:** Only HTML5 documents with `<article>` or `<main>` tags

Occurs when webpage doesn't meet HTML5 format or lacks required `<article>` or `<main>` tags.

**Steps to resolve:**
* **Verify HTML5 format:** Check doctype declaration. HTML5 pages should have `<!DOCTYPE html>`
* **Check required tags:** View page source and ensure contains `<article>` or `<main>` tags
* **Update webpage:** If not HTML5 format or lacks tags, update page to meet requirements

---

## Frequently Asked Questions

### How do I perform manual sync for external sources?

1. Navigate to **Settings** > **AI features** > **Manage sources**.
2. Click **Sync** at top of **Manage source** page.
3. Manually sync external sources up to four times per day.

> **NOTE**
> 
> System automatically syncs every 24 hours.

### How do I delete external sources?

1. Navigate to **Settings** > **AI features** > **Manage sources**.
2. Hover over desired source and click **Delete** icon.
3. To delete multiple, select checkboxes and click **Delete** at top.

### How do I view analytics for external sources?

1. Navigate to **Analytics** > **Eddy AI**.
2. In **Most referenced articles** section, external sources list alongside Knowledge base articles.

### Can I temporarily disable external sources?

Yes, turn off **Status** toggle next to external sources. Eddy AI stops fetching until re-enabled.

---

## AI Article Summarizer

### Plans Supporting AI Article Summarizer

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

**Article summarizer** is one of Document360's AI-powered features. Useful when readers want to save time by not reading lengthy articles. Instead, read condensed article information as **summary**.

Document360 uses natural language processing (NLP) to locate vital information in article content while maintaining original context for optimal summary.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

### Prerequisites

* **Preprocessed article content** must exceed **250 words**
* AI feature supported in subscription plan

> **NOTE**
> 
> Article summary available (depending on subscription plan) in new/existing articles published on or after May 27, 2023.

---

## Enabling Article Summarizer

1. Navigate to **Settings** > **AI Features** > **Eddy AI**.
2. Turn on **Article summarizer** toggle.

When enabled, **Summary** appears at article top in Knowledge base site. Click 'Summary' to expand and read.

---

## Frequently Asked Questions

### What is 'Preprocess' or 'Preprocessed words'?

**Preprocess** refers to filtering specific article/category elements. Elements not counted for meta description generation:

* HTML tags
* Images
* URLs/links
* Code blocks

If article word count shows 220 words at Document360 editor bottom, this includes HTML tags, links, code blocks. Preprocessed count is less. Ensure preprocessed content exceeds 250 words for AI summarizer.

### Data Privacy

Customer Knowledge base data is sensitive. As feature uses OpenAI integration, we adhere to OpenAI privacy policies. Policy states: "OpenAI will not use data submitted by customers via our API to train models or improve service offerings."

> Read complete [OpenAI API data usage policies](https://openai.com/policies/api-data-usage-policies)  
> For Document360 data policy queries, read our [Privacy policy](https://document360.com/privacy/)

---

## Ask Eddy AI API

### Plans Supporting Ask Eddy AI API

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

Eddy AI Public API enhances Eddy AI search functionality and flexibility. Particularly useful for businesses deeply integrating AI-driven search into their platforms. Embedding Eddy AI into products provides users powerful search without visiting documentation site.

API offers greater UI customization flexibility, allowing tailoring of color, naming, and placement to align with brand and user experience. With seamless integration, Eddy AI becomes natural product extension, enhancing user interactions and improving search efficiency. Exposing API endpoints incorporates them into platforms, effortlessly extracting answers and building customized search experience.

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

---

## Using the Public API

1. Navigate to Settings > **AI Features** > **Eddy AI**.
2. In **AI assistive search**, select **Public API** checkbox.

> **NOTE**
> 
> 1. Ensure at least one checkbox selected. Otherwise, AI assistive search toggle automatically disables.
> 2. Without Public API enabled, receive '500 response code error' or '400 API access disabled error' using Ask Eddy AI API.
> 3. Each API call reduces total credit count by one.

3. Create authorization API token.

> **NOTE**
> 
> 1. Navigate to Settings > **Knowledge Base Portal** > **API Tokens**.
> 2. Click **Create API Token**, enter token name, specify POST method.
> 3. Click **Create** and **copy** generated API token.

4. Find API structure at [API hub](https://apihub.document360.io/index.html).

---

## Try Eddy AI Public API in API Docs

1. Navigate to Document360 [API documentation](https://apidocs.document360.com/apidocs/perform-ai-assistive-search-ask-eddy-within-project-version).
2. On page right side, click **Try it** section.
3. In **Token** field, enter API token generated from Document360 project.
4. Enter desired values in **Body** section. Default request box:

   * **Prompt**: Enter question or query
   * **Version ID**: Obtain current version ID
   * **Language Code**: Specify desired language code

5. Click **Try it & see response** for generated response.

---

## Try Eddy AI Public API in Swagger

1. Navigate to Swagger [API hub](https://apihub.document360.io/index.html). Find Ask Eddy AI API under project versions.
2. In Swagger API hub top right, click **Authorize**.
3. **Available authorizations** panel appears, prompting API token entry.
4. Paste API token into **Available Authorizations** window and click **Authorize**.
5. Navigate to **Project versions** > `/v2/ProjectVersions/ask-Eddy AI` and click **Try it out**.
6. Default request box:

* **Prompt**: Enter question or query
* **Version ID**: Obtain current version ID from `/v2/ProjectVersions` endpoint
* **Language Code**: Specify desired language code

7. Click **Execute** for successful response with required information.

> **NOTE**
> 
> If receiving service unavailable message, ensure Public API enabled in settings.

---

## Frequently Asked Questions

### Why discrepancy in source articles between Ask Eddy public API and Eddy AI search?

Discrepancy occurs retrieving details using `articleID` for "Pagecategory" articles. Fields like `article_id`, `article_title`, and `article_slug` return null.

For "Pagecategory" articles, fetch details using `categoryID` instead of `articleID`. Example API response:

```
{
  "category_id": "_categoryid",
  "category_title": "Title",
  "category_slug": "slug",
  "version_name": "v1",
  "version_slug": "v1",
  "article_id": null,
  "article_title": null,
  "article_slug": null,
  "version_display_name": null
}
```

To resolve, use `categoryID` for "Pagecategory" articles when using Eddy API.

---

## Enhancing Accessibility with Read Out Loud Feature

### Plans Supporting Read Out Loud Feature

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

Read out loud feature allows users to listen to articles instead of reading, saving time. Beneficial for multitasking, absorbing information while performing other activities. Particularly useful for auditory learning preference or multitasking users.

Available exclusively on Knowledge Base site 2.0, enhancing engagement with flexible reading alternative.

> **NOTE**
> 
> Legacy plan customers need Enterprise plan with AI assistive search add-on.

---

## Using Read Out Loud Feature

Key highlights:
* Begins reading from article heading, continues with body content
* Does not cover article summary
* Reads alt text of images and videos. Without alt text, audio indicates presence in respective language
* **Listen** button in article header below heading. Playback updates button label to **Listening** and opens Player window

> **NOTE**
> 
> For supported languages, [click here](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite).

### Player Options

Player controls at screen bottom right:
* Play icon - start listening to content
* Pause icon - stop audio play
* Forward icon - skip ahead by ten seconds
* Backward icon - rewind by ten seconds
* Close (x) icon - close player window

### Enable or Disable Player

Enable/disable at project level:
1. Navigate to Settings > **Knowledge base site** > **Article settings**.
2. Under **Accessibility** section, turn on **Enable read out loud** toggle.

> **NOTE**
> 
> **Enable read out loud** disabled by default for trial plan customers.

---

## Frequently Asked Questions

### What content does read out loud feature cover?

Reads:
* Textual content
* Glossary
* Snippets
* Variables
* Headings (H2, H3, H4)
* Numbered lists
* Checklists
* Bullet lists
* Callouts
* Private notes
* Accordions
* FAQ
* Link text
* Emojis

Indicates presence without reading:
* Tables
* Inline code
* Code blocks
* Images
* Videos
* LaTeX
* Files attached using insert menu

### Can I choose to read article from middle?

Yes, navigate audio player using seek option.

---

## AI Premium Suite

### Plans Supporting AI Premium Suite

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

**AI premium suite** elevates user experience by automating key business processes and improving workflow efficiency through advanced AI-powered tools.

---

## Features in AI Premium Suite

1. [**AI-automated business glossary generation**](/help/docs/ai-glossary-generator)

Streamlines creation and management of industry-specific glossaries. Maintains consistent terminology across teams, enhances communication, ensures documentation accuracy.

> **NOTE**
> 
> Eddy AI premium suite available in English (en) only.

---

## AI Glossary Generator

### Plans Supporting AI Premium Suite

| Professional | Business | Enterprise |
|--------------|----------|-----------|
|              |          |           |

Different departments may use similar business terms with differing definitions and assumptions. This knowledge remains department-specific. Defining business terms is crucial for shared understanding, consistent data collection, and correct business logic application for reliable metrics.

Document360's AI Glossary generator helps organizations communicate and collaborate by clearing terminology ambiguity. Creates complete collection of business terms, providing clarity and shared understanding. Aids data collection, team collaboration, communication, and database design.

---

## Enabling AI Glossary Generator

1. Navigate to **Settings** > **AI Features** > **Eddy AI**.
2. Scroll to find **AI Glossary generator** option.
3. Toggle switch to enable feature.

---

## Accessing AI Glossary Generator

1. Navigate to **Documentation** > **Content tools** > **Content reuse** and select **Glossary**.
2. Click **Take action** on Eddy AI banner.

Default view shows **Open suggestion** section under **Eddy AI glossary suggestions**.

> **NOTE**
> 
> AI Glossary Generator shows suggestions only for published articles. Otherwise shows 0 suggestions.

3. Left navigation bar:
   * List of Eddy AI recommended glossary terms
   * Use **Search bar** for multiple terms
   * Use **Sort** option to organize terms

4. Top center shows term repetition count.

Example: Backup used 1 time(s) in 1 article(s).

5. **Definition** text box shows Eddy AI suggested definition. Edit using formatting tools.

> **NOTE**
> 
> Glossary definition up to 500 characters.

6. **Add to** dropdown defaults to **English**.
7. Enable **Update in articles (n)** checkbox to update glossary in articles.

> **NOTE**
> 
> Create glossary without implementing in articles by unchecking **Update in articles**.

8. Click **Show Articles** to view articles using glossary terms.

> **NOTE**
> 
> Only accessible articles display here.

9. Click **+ Add to glossary** after changes.
10. Added terms move to glossary list.
11. Click **Ignore term** to move to **Ignored suggestions** section.
12. From **Ignored suggestions**, click **Move to open list** anytime.
13. Click **Continue later** to close blade.

AI Glossary generator scan every 7 days.

---

## Using AI Glossary Generator in Advanced WYSIWYG Editor

1. Navigate to Advanced WYSIWYG editor and click **Insert**.
2. Select **Glossary**. Eddy AI provides glossary suggestions based on specific article.

> **NOTE**
> 
> In Editor, **AI Glossary generator** scan occurs every time opened. One instance scans up to first 50 terms.

3. Click **Take action** to open **Eddy AI glossary suggestions** window with Open suggestions section as default view.

---

## Shortcuts for AI Glossary Generator

Use shortcuts in **Edit glossary suggestions** window:
* ARROW keys to navigate suggestions
* ENTER to add current glossary term
* BACKSPACE to ignore current glossary term

---

## Frequently Asked Questions

### Does AI Glossary generator recognize singular and plural terms as one?

No, Document360's AI Glossary generator considers identical singular and plural terms as individual specific terms.

Example: **Team Accounts** and **Team Account** evaluated as distinguished terms.

### Does AI Glossary generator recognize synonymous terms as one?

Synonymous terms considered as individual separate terms.

Example: Routine and Daily are synonymous but considered different terms.

### How often can I rescan and why?

System recommends 7-day interval between scans, notified in UI. Quantifiable documentation content necessary for new suggestions.

### Is rescan manual or automated?

Rescan is manual process, not automated.

### What happens after rescan?

New suggestions update **open suggestions** list. Users receive email notification.

---

## How to Write GenAI Friendly Content

Structure information for improved clarity, readability, and searchability:

### 1. Use Clear and Concise Headings

* **Headings (H1, H2, H3)**: Organize content with clear descriptive headings. Helps AI understand hierarchy and structure.
* **Keyword-rich headings**: Reflect section content. Instead of "Introduction," use "Introduction to Cloud Storage Solutions."

### 2. Write Short and Focused Paragraphs

* **Keep sentences short**: Aim for 15-20 words. Avoid complex sentences confusing AI processing.
* **One idea per paragraph**: Each paragraph covers one idea for easy AI extraction.

### 3. Include Tables for Structured Data

* **Well-labeled tables**: Present structured data for easier AI scanning and interpretation. Clearly label rows and columns.
* **Consistent formatting**: Format consistently for better AI recognition (avoid merged cells or irregular formatting).

### 4. Incorporate Code Snippets Carefully

* **Clean, well-commented code**: Use standard formatting and comment key sections. AI uses comments for context understanding.
* **Appropriate syntax highlighting**: Helps AI differentiate code from regular text.

### 5. Use Bullet Points and Numbered Lists

* **Break up information**: Help organize content for easier AI breakdown and extraction.
* **Limit list length**: Keep concise (under 5-7 points) to avoid overwhelming AI and readers.

### 6. Include Descriptive Alt Text for Images

**Alt text and captions**: Always include descriptive alt text and captions for AI context processing.

### 7. Provide Clear, Contextual Links

* **Internal links**: Link to relevant internal articles using clear anchor text. Avoid "click here."
* **Anchor text**: Use descriptive anchor text informing AI of linked content ("Read more about cloud storage security best practices").

### 8. Ensure SEO Best Practices

* **Keyword optimization**: Use naturally within headings, subheadings, and content. Avoid keyword stuffing.
* **Meta descriptions**: Write clear, relevant meta descriptions with keywords for effective AI ranking.

### 9. Use Business Glossary Terms Consistently

* **Consistent terminology**: Use business glossary terms consistently throughout articles. Helps AI identify and relate key terms.
* **Define key terms**: Include brief definitions or link to business glossary for unfamiliar terms.
* **Standardize abbreviations**: Always use standardized abbreviations or acronyms from business glossary. Ensures correct AI identification.

### 10. Write for Humans First

* **Conversational tone**: AI performs better with human-friendly tone for engagement and contextual understanding.
* **Natural language**: Use natural everyday language. Avoid jargon or complex terms unless necessary. Provide definitions for technical terms.

### 11. Monitor AI-Generated Content

**Review and revise**: Always review AI tool output for quality standards and natural reading.

---

## Recommendations for Optimizing Experience as Contributor with Eddy AI

Create easily understood documentation by incorporating clear language, structured formatting, and adherence to specific guidelines:

1. **Use clear and focused language**

Express ideas straightforwardly, avoiding unnecessary complexity.

Break down complex concepts into simpler parts.

Define technical terms or provide links to detailed explanations.

2. **Structured formatting**

Use clear headings and subheadings to organize information.

Employ bullet points and numbered lists for step-by-step instructions.

Highlight key points using bold or italics for better bot parsing.

3. **Consistent terminology**

Maintain consistent terminology for understanding.

Use Document360 Glossary feature.

Avoid ambiguity with specific standardized terms.

4. **Avoid jargon overload**

Minimize industry-specific jargon unless essential.

If technical terms necessary, provide brief explanations or context.

5. **Elaborative text content**

Elaborate content and clearly specify intent.

With multimedia content, provide text explanation of conveyed message.

Break information into shorter paragraphs for better readability.

Provide explicit answers to questions in FAQ form to minimize inaccurate Eddy AI answers. AI bots hallucinate with insufficient or unclear content.

6. **Provide context and example**

Offer real-world examples illustrating technical concepts.

Provide context for reader understanding of purpose and application.

7. **Use descriptive headings**

Craft descriptive headings accurately representing content.

Headings should guide, summarizing content beneath.

Avoid repetitive heading text in same article.

8. **Test with Eddy AI**

Utilize Eddy AI to analyze content for clarity and coherence.

Make adjustments based on tool feedback.

Implementing these recommendations creates documentation comprehensible to humans and easily processed by AI and NLP bots like Eddy AI.

---

## Prompt Engineering Tips

Document360's Eddy AI provides various AI-driven functionalities streamlining content creation and enhancing knowledge base experience. Leveraging prompt engineering with Eddy AI improves accuracy, efficiency, and relevance in generating tailored content. This guide helps maximize Eddy AI capabilities when interacting with knowledge base.

---

## Best Practices for Prompt Engineering with Eddy AI

### 1. Be Clear and Specific in Prompts

More precise instructions yield better results. Instead of "brief summary," specify "Generate 100-word summary about Document360 knowledge base benefits."

For complex technical details, break into smaller manageable requests for focused relevant outputs.

### 2. Ask for Step-by-Step Instructions

Eddy AI is effective for procedural content with clear task specification. Instead of "Explain how to publish article," use "List steps to publish article in Document360, including where to click and how to configure settings."

### 3. Structure Prompts for Comparisons

Structure accordingly for content comparing features or options. "Compare key differences between Document360's private and public knowledge base setups" guides Eddy AI to generate detailed comparison.

### 4. Focus on Article Summaries

When summarizing longer articles, ask Eddy AI to create summaries based on specific sections or categories. "Summarize benefits and limitations section of article on Document360's multi-language support" generates more concise useful summaries.

### 5. Include Context for Recommendations

Context critical for generating recommendations or suggestions. Instead of "Recommend improvements," use "Recommend improvements to onboarding process in knowledge base article for new users."

---

## Recommendations for Optimizing Experience as Reader with Eddy AI

1. **Converse naturally**

Speak to Eddy AI as to human.

Example: Instead of "Search for articles on templates," try "Eddy AI, find me articles explaining Document360 templates."

2. **Provide detailed context**

Enhance understanding by setting stage and providing context.

Example: Instead of "Errors in documentation," try "Eddy AI, help me identify and resolve errors in Document360 user guide."

3. **Customize persona**

Instruct Eddy AI to adopt specific identity for personalized responses.

Example: Instead of "Search for software updates," try "Eddy AI, imagine you're our IT expert and update me on latest software changes."

4. **Embrace creativity**

Encourage experimentation and creativity in queries.

Example: Instead of standard search "Knowledge base structure," try "Eddy AI, let's play! Imagine you're content strategist and suggest ideal knowledge base structure."

Following these recommendations harnesses Eddy AI capabilities for more engaging tailored interactions. Experiment, instruct creatively, and watch queries yield more insightful personalized results.

---

## Tips for Enhancing Knowledge Base Articles with Eddy AI

### 1. Use Eddy AI for Content Categorization

When organizing content, ask Eddy AI to help categorize or label articles. "Suggest categories for article discussing API integration and customization in Document360" streamlines knowledge base structure.

### 2. Generate Error Message Documentation

For troubleshooting or technical content, ask Eddy AI to document common error messages. "Generate explanations for common error messages users encounter integrating third-party tools in Document360" ensures comprehensive error documentation.

### 3. Request Best Practices

Eddy AI assists in compiling best practices. "List best practices for writing comprehensive how-to articles for knowledge base aimed at developers" generates useful guidelines.

### 4. Create Troubleshooting Guides

For knowledge base troubleshooting sections, instruct Eddy AI to generate content like "Create troubleshooting guide for resolving common login issues in Document360" ensuring focus on step-by-step solutions.## Use Cases

Eddy AI streamlines content creation across industries—LMS platforms, customer support knowledge bases, compliance documentation, product development guides, and e-commerce systems. Tailor prompts to specific needs for better efficiency, accuracy, and engagement.

### 1. Building a Learning Management System (LMS)

**Course Creation and Structuring**

* **Outline generation:** Ask Eddy AI to create course outlines by specifying learning objectives. Example: "Create outline for beginner's cloud computing course."
* **Content segmentation:** Divide long-form content into digestible modules. Example: "Split cybersecurity fundamentals article into 5 lessons with titles and summaries."
* **Quiz and FAQ generation:** Generate interactive content. Examples: "Create quiz questions for each module in cloud computing course" or "Generate FAQs for cloud security module."

**Enhancing User Engagement**

* **Adaptive learning paths:** Recommend follow-up content based on learner performance. Example: "Suggest advanced articles for learners who completed beginner's cloud computing course."
* **Knowledge retention aids:** Create summaries and revision guides. Example: "Generate revision guide summarizing key points of data privacy module."

---

### 2. Streamlining Customer Support Knowledge Bases

**Creating Troubleshooting Guides**

* Generate step-by-step guides for specific support cases. Example: "Create troubleshooting guide for common login issues in e-commerce platform."
* Document error message explanations. Example: "Create documentation explaining causes and fixes for error code 403 in web hosting."

**Organizing FAQs for Support Agents**

* Generate FAQs based on customer interactions. Example: "Create list of FAQs for common billing issues on our platform."
* Update existing FAQs by analyzing new data. Example: "Update current FAQ section with recent questions about product integration."

---

### 3. Accelerating Compliance Documentation

For healthcare, finance, or manufacturing sectors requiring up-to-date compliance documentation.

**Generating Compliance Checklists**

* Create checklists based on industry standards. Example: "Generate checklist of mandatory compliance requirements for HIPAA."
* Update compliance content. Example: "Update checklist with latest GDPR regulation changes."

**Creating Standard Operating Procedures (SOPs)**

* Draft clear, detailed SOPs for regulated environments. Example: "Draft SOP for handling customer data in compliance with GDPR."

---

### 4. Supporting Product Development Documentation

**API Documentation**

* Generate API usage examples. Example: "Create step-by-step guide for integrating our API with third-party services."
* Update documentation. Example: "Update API documentation to reflect changes in latest version."

**Release Notes and Feature Documentation**

* Create concise release notes. Example: "Generate release notes for version 4.2 highlighting new features and bug fixes."
* Generate user guides for new features. Example: "Create user guide for new reporting dashboard feature in SaaS platform."

---

### 5. Automating Retail and E-commerce Content

**Product Documentation**

* Generate product guides automatically. Example: "Create product guide for smart home security system covering setup, troubleshooting, and usage tips."
* Generate comparison content. Example: "Compare features of three smart home security systems on our platform."

**Order and Return Procedures**

* Simplify customer processes. Example: "Generate step-by-step guide for returning product purchased on e-commerce site."

---

### FAQs

**How can I ensure Eddy AI gives specific content?**

Be detailed in prompts. Specify length, tone, and focus. Example: "Provide formal, 200-word explanation of creating custom categories in Document360."

**What if the output is too broad?**

Rephrase prompts to narrow focus. Break requests into smaller steps. Example: "Generate summary of Document360's version control feature" followed by "List key benefits of version control in knowledge base system."

**Can Eddy AI assist with writing FAQs?**

Yes. Request FAQs based on specific sections. Example: "Generate FAQs related to article categorization and tagging in Document360."

**How can I use Eddy AI for technical content?**

Include relevant technical details in prompts. Example: "Generate step-by-step guide for integrating Google Analytics with Document360's knowledge base."## Variables

**Plans supporting content reuse**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Variables help maintain consistency when using the same text across multiple documentation sections. Update information in one place, and it automatically reflects everywhere the variable is used.

For example, use a variable for contact information. When details change, update the variable once instead of editing every instance.

---

## Creating a variable

To create a variable:

1. Navigate to Documentation > **Content tools** > **Content reuse** > **Variables**.
2. Click **Create variable**.
3. Enter the **Name** for your variable.

> NOTE
>
> Variable names can include letters, numbers, hyphens, and underscores. Maximum length: 30 characters.

4. The **Merge code value** appears automatically. This is how the variable will be referenced in articles.

> Example: Variable name "Disclaimer" becomes merge code `{{variable.Disclaimer}}`

5. Select **Language**:
   * **Global** - Available across all languages
   * Specific language - For language-specific content

6. Enter the variable **Content**.

> NOTE
>
> Character limit: 100 characters including spaces. For longer content, use **Snippets**.

#### Formatting options

Style your variable content with these formatting tools:

• **Bold**
• **Italic**
• **Strikethrough**
• **Underline**
• **Font size** (8 to 36)

Additional formatting:
• **Font Family**
• **Text color** (HEX code or picker)
• **Background color** (HEX code or picker)
• **Subscript**
• **Superscript**
• **Clear Formatting**

**Insert Link**:
1. Click **Insert link** icon
2. Enter URL and link text
3. Optionally select **Open in new tab**
4. Click **Insert**

7. Click **Create variable**.

The new variable appears in the Variables list, ready for editing or deletion.

---

## Using variables in articles

Add variables to articles using two methods:

#### Method 1: Markdown syntax

Type the merge code between double curly brackets:

`{{variable.Disclaimer}}`

> NOTE
>
> Exact spelling required. Even one character difference breaks the variable.

#### Method 2: Editor toolbar

1. Click **Content reuse** icon in Markdown/WYSIWYG editors
   *Or* in Advanced WYSIWYG: **Insert > Variables** or use "/" command

2. Select variable from list or use **Search variables**

> In Advanced WYSIWYG, hover over variable names to preview content

3. Click to insert variable

> NOTE
>
> Markdown/WYSIWYG editors allow multiple variable selection

---

## Variables overview page

Manage variables from the overview page:

1. Navigate to Documentation > **Content tools** > **Content reuse** > **Variables**

Key features:
1. **Languages** - Filter by Global or specific language
2. **Search variable** - Find variables by name
3. **Used in** - View articles using each variable. Click **View** for details
4. **Language** - See each variable's language setting
5. **Last modified** - Track update timestamps
6. **Preview** - Click variable name to see content
7. **Progress** - View translation status across languages
8. **Edit** - Modify variable content
9. **Delete** - Remove variables

---

## View article dependencies

Find where variables are used:

1. In the **Used in** column, click **View**
2. **View references** panel shows all articles containing the variable
3. Click article names to expand details:
   * Article version
   * Workspace and language
   * Contributor information
   * Article status (Published, Draft, New)
   * Insert timestamp

---

## Editing variables

1. Navigate to Documentation > **Content tools** > **Content reuse** > **Variables**
2. Hover over variable and click **Edit**

> NOTE
>
> Variable names and merge codes cannot be changed after creation

**Editing links in variables**:
Click the link to access options:
• **Open link** - Test the URL
• **Style** - Choose green text or thick formatting
• **Edit** - Modify URL, text, or target settings
• **Unlink** - Remove hyperlink formatting

3. Click **Update** after editing

> NOTE
>
> Changes appear immediately in all articles using the variable

---

## Deleting variables

1. Navigate to Documentation > **Content tools** > **Content reuse** > **Variables**
2. Hover over variable and click **Delete**
3. Confirm deletion

#### Bulk deletion

Select multiple variables and click **Delete** at top of list

> NOTE
>
> Variables with dependencies cannot be deleted. Remove from articles first.

---

## Translating variables

Create multilingual variables for consistent localized content.

#### New variables

1. Navigate to Documentation > **Content tools** > **Content reuse** > **Variables**
2. Click **Create Variable**
3. Select specific language (not Global)
4. Enter variable name and content in default language
5. Click **Translate to other languages**
6. Select target languages and click **Translate**

> NOTE
>
> Default language marked as **Main**
> Translated languages show green checkmarks

7. Click **Create Variable**

#### Existing variables

1. Open variable for editing
2. Click **Translate to other languages**
3. Select target language and click **Translate**
4. Use **Translate again** to overwrite existing translations
5. Use **Remove language** to delete specific translations

> NOTE
>
> Global variables cannot be translated

---

## FAQ

**How do variables work?**

Define content once, use everywhere. Changes update automatically across all articles.

**What's the benefit?**

Maintain consistency while reducing manual updates. Saves time and prevents errors.

**Can I create custom variables?**

Yes, create variables for any reusable text, numbers, or links.

**How do I use variables in articles?**

Insert via editor toolbar or merge code syntax.

**Do variables update multiple articles?**

Yes, one edit updates all instances.

**What content types work with variables?**

Text, numbers, and links. Ideal for product names, versions, URLs, and contact info.

**How do variables help collaboration?**

Everyone uses the same accurate information. Updates propagate instantly.

**Should I use variables in technical docs?**

Absolutely. Essential for dynamic information requiring frequent updates.

**Can I translate variables?**

Yes, into any project language.

**Are variables searchable?**

Yes, both site search and Google index variable content.## Eddy AI Search Analytics

**Plans supporting Eddy AI analytics**

| Professional | Business | Enterprise |
| --- | --- | --- |
| ✓ | ✓ | ✓ |

Eddy AI assistive search analytics helps you understand and optimize AI search performance in your knowledge base. The analytics page shows overall Eddy AI performance and search metrics, including unanswered searches. Visualize search data through charts and graphs.

> NOTE
>
> See [Eddy AI multilingual support](/help/docs/ai-search-suite#multilingual-support-for-eddy-ai-search-suite) for supported languages.
>
> Conversational Eddy AI metrics are only available in KB site 2.0 projects.

### Accessing Eddy AI analytics

Navigate to **Analytics** > **Eddy AI - Assistive Search** in the knowledge base portal.

### Key metrics

| Metric | Description |
| --- | --- |
| **Total searches** | Number of searches performed during the selected period |
| **Answered searches** | Searches where Eddy AI provided relevant results |
| **Unanswered searches** | Searches where Eddy AI couldn't find relevant content |
| **Click-through rate** | Percentage of users who clicked on AI-suggested articles |
| **Feedback rating** | Average user rating of AI search results (1-5 stars) |

### Filter options

Customize data display using filters:

1. **Date range**: Select predefined periods or custom dates
2. **Search type**: Filter by search intent (Informational, Navigation, Transactional)
3. **Language**: View analytics for specific knowledge base languages
4. **User type**: Filter by team accounts or readers

> NOTE
>
> Analytics data may take up to 15 minutes to appear in the portal.

### Search performance visualization

View search data through interactive charts:

* **Search volume trend**: Track searches over time
* **Answer rate distribution**: See answered vs unanswered searches
* **Top search queries**: Identify most common user searches
* **Zero-result searches**: Find queries that returned no results

Click chart legends to toggle data series visibility. Export charts as PNG images using the **Export image** icon.

### Improving search performance

Use analytics to optimize your knowledge base:

1. **Add content for unanswered searches**: Create articles addressing common zero-result queries
2. **Refine existing articles**: Improve articles with low click-through rates
3. **Monitor trending topics**: Stay ahead of emerging user interests
4. **Track multilingual performance**: Ensure consistent search quality across languages

### FAQ

**How often is Eddy AI search data updated?**

Data updates every 15 minutes. Real-time metrics aren't available.

**Can I export Eddy AI analytics data?**

Yes, export search metrics and query data as CSV files from the analytics page.

**What causes unanswered searches?**

Unanswered searches typically result from:
* Content gaps in your knowledge base
* Poorly phrased user queries
* Insufficient article tagging or categorization
* Low-quality article content that doesn't match search intent### Accessing Eddy AI search analytics

1. Navigate to **Analytics** > **Eddy AI** in the Knowledge base portal
2. The **Eddy AI - Assistive Search** page appears
3. View article performance metrics for the past week by default
4. Use filters to select different date ranges

### Using filters to customize data

Adjust the default **last week** date range using filters:

1. Click the **Date** filter dropdown
2. Select a predefined range (**This month**, **Last month**) or **Custom** for specific dates

---

### Eddy AI search analytics page overview

You can view the following article performance metrics as tiles:

| Field | Description |
| --- | --- |
| **Total conversations** | Total number of conversations in Eddy AI. Available only for KB site 2.0 projects where Eddy AI is conversational. A single message counts as a conversation. |
| **Total queries** | Total number of queries performed in Eddy AI. Queries are individual questions within conversations. |
| **Answered queries** | Total number of queries that returned a result |
| **Unanswered queries** | Total number of queries that produced no results |

> NOTE
> 
> If multiple chatbots or knowledge base widgets are deployed, data from all instances is merged in the results.

---

### Query analysis

Interact with the graph to analyze query data:

1. **Date-wise metrics**: Hover over the graph to see metrics for specific dates
2. **Date filter**: Click **This month** dropdown to view different months
3. **All**: Shows answered queries, unanswered queries, and conversations together
4. **Answered** (green line): Click to view only answered query data
5. **Unanswered** (red line): Click to view only unanswered query data
6. **Conversations** (violet line): Click to view conversation data. Available only for KB site 2.0 projects
7. **Export image**: Save Query analysis as PNG using the export icon

> NOTE
> 
> Keep unanswered searches low compared to answered searches. Unanswered searches typically occur when documentation lacks relevant information. Regular updates help minimize these.

---

### Conversation depth metrics

Shows conversation length distribution. Available only for KB site 2.0 projects.

1. Hover over bars to see exact conversation counts
2. Tracks conversations from 1 to 5 queries
3. Conversations with more than 5 queries grouped under 6+
4. Click **Export image** to save as PNG

---

### Feedback chart

Displays Like/Dislike data with percentages. Total feedback percentage shown inside the color chart.

Click **Export image** to save the Feedback chart as PNG.

---

### Popular queries

Shows top five search themes with frequency counts for the selected month. Queries grouped by keywords to highlight most popular topics.

> NOTE
> 
> Popular queries require at least one month of data.

---

### Unanswered queries

Shows top five unresolved search themes with frequency counts. Each keyword represents a topic with unanswered searches.

> NOTE
> 
> Monthly post-processing analyzes 30 days of data. OpenAI identifies common keywords and groups them into 10 primary topics. Remaining data grouped under "Others." Applied to all answered and unanswered queries.

---

### Most referenced articles

Lists five most-referenced articles for the selected month, showing how often each appeared in Eddy AI search results.

---

### Conversations

Detailed view of user interactions in tabular format showing queries, response status, and feedback.

1. **Search field**: Search for specific conversations or queries
2. **Conversations**: Displayed with first question visible by default. Other questions collapsed. Click queries to view full conversation in popup

   > NOTE
   > 
   > Conversations spanning multiple months appear in the analytics of their starting month
3. **Query topic**: Derived from popular queries list. Requires 30 days of data
4. **Response**: Shows answered or unanswered status
5. **Feedback**: Displays likes or dislikes
6. **Filter**: Filter by query topic, response status, feedback type, or application

   * **Response Status**: All, Answered, or Unanswered
   * **Feedback**: All, None, Liked, or Disliked
   * **Query type**: Filters previous month queries. Unavailable for current month
7. **Export**: Save filtered data as CSV

---

### FAQs

**Why can't I filter data weekly?**

Popular queries and unanswered search keywords require sufficient data for algorithmic grouping based on response frequency.

**How do I resolve unanswered queries?**

Identify relevant articles based on keywords from unanswered searches and update content accordingly.

**How does Eddy AI handle multilingual conversations?**

Each language in a conversation updates separately in the conversation table. Metrics like searches, answered queries, unanswered queries, and feedback update only for the language where they occurred.

**How does Eddy AI handle multi-workspace conversations?**

Each workspace in a conversation updates separately in the conversation table. Metrics update only for the languages used within respective workspaces.

**How are queries different from conversations?**

Queries are individual questions. One or more queries make up a conversation.## Adding custom links

Need to add a download link to an eBook or Google Sheets?  
You can direct users by adding custom links to the Knowledge base Widget.

![2_addingcusotmlinks.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_addingcusotmlinks.png)

Links are added as a "section" to your Widget. They appear in the order added, underneath the **Top search articles** section.

To add a custom link:

1. Navigate to **Knowledge base Widget** in the Knowledge base portal
2. Hover on the desired Knowledge base Widget and click **Edit**
3. In the **Installation & Setup** tab, expand the **Add custom links** section
4. In the **Add Custom Links** section:

   * Type the title for your section
   * Type the display text for the link

     > **For example:** **Contact Us**
   * Type the URL link

     > **For example:** https://support.document360.com
5. Click the adjacent icon and choose the desired icon from available options
6. Click **Add** > **Save**

![1_addlinks.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_addlinks.gif)

**NOTE**

You can use a `mailto:` in the link field. For example: `mailto:<youremail@somedomain.com>`

### Edit a custom link

1. Navigate to **Knowledge base Widget** in the Knowledge base portal
2. Hover on the desired Knowledge base Widget and click **Edit**
3. In the **Configuration & connect** tab, expand the **Add links** section
4. In the **Add Links** section, locate the custom link you wish to edit
5. Click **Edit** and update desired fields
6. Click **Save**

### Deleting a custom link

1. Navigate to **Knowledge base Widget** in the Knowledge base portal
2. Hover on the desired Knowledge base Widget and click **Edit**
3. In the **Configuration & connect** tab, expand the **Add links** section
4. In the **Add Links** section, locate the custom link you wish to delete
5. Click **Delete**
6. Click **Save**

---

## Securing Knowledge base widget authentication using JWT

Implement authentication configuration for the widget using JWT to ensure secure access for private and mixed projects.

1. Navigate to Knowledge base widget in the Knowledge base portal

   The list of widgets will appear
2. Hover on the desired Knowledge base Widget and click **Edit**
3. In the **Configure & connect** tab, navigate to the **JWT** section and **enable** the JWT toggle

1. **Client ID:** Your project's ID
2. **Widget ID:** Unique identifier for each widget
3. **Token endpoint:** HTTP endpoint to obtain access token given authorization code
4. **Client secret:** Click **Regenerate** to generate. Save this for future use - same secret applies to all widgets

> NOTE
>
> Client secret required for JWT widgets. This information will not be stored in Document360

5. **Authorize URL:** Paste the authorized URL from your knowledge base widget webpage
6. Click **Save**

![Securing the Knowledge base widget](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Securing_Knowledge_base_widget_authentication_using_JWT.png)

Embed the authorized URL within your code and paste it into the **script section** on your webpage. This creates a secure, authenticated widget that prevents unauthorized third-party access.

---

### Implementing the auth endpoint

```
[HttpGet]
[Route("authenticate")]
public async Task<IActionResult> WidgetAuthentication(string id)
{
    if (HttpContext.User.Identity.IsAuthenticated)
    {
        var clientData = new ClientDetails()
        {
            ClientId = "{Client ID}",
            Secret = "{Client secret}",
            TokenEndpoint = "{Token endpoint}",
            WidgetId = "{Widget ID}",
            SecurityGroupIds = "{Comma separated reader group IDs}", // mandatory for KB widget configuration
            TokenValidity = 15, // token validity in minutes
        };

        if (clientData == null)
            return NotFound();

        List<string> readerGroupids = null;
        if (!string.IsNullOrEmpty(clientData.SecurityGroupIds))
            readerGroupids = clientData.SecurityGroupIds.Split(',').Select(c => c.Trim()).ToList();

        var payload = new
        {
            username = "{Username}",
            firstName = "{First name}",
            lastName = "{Last name}",
            emailId = "{Email address}",
            readerGroupIds = readerGroupids,
            tokenValidity = clientData.TokenValidity,
            widgetId = clientData.WidgetId,
            projectId = clientData.ClientId
        };

        var payloadString = JsonConvert.SerializeObject(payload);

        var result = await client.RequestTokenAsync(new TokenRequest
        {
            Address = clientData.TokenEndpoint,
            ClientId = clientData.ClientId,
            ClientSecret = clientData.Secret,
            GrantType = "Widget",
            Parameters =
            {
                {
                    "payload",  payloadString
                },
                {
                    "id", clientData.ClientId
                },
            }
        });

        return Ok(new
        {
            accessToken = result.AccessToken,
            expiresIn = result.ExpiresIn
        });
    }
    else
    {
        return Unauthorized(new { success = false });
    }
}
```

C#

Copy

> NOTE
>
> Include comma-separated reader group IDs as security group IDs to configure and render the KB widget

---

### FAQs

#### Why are certain categories appearing on the Knowledge base site but not in the widget?

This occurs when category-level access isn't properly configured for the widget. To ensure categories are visible:

1. Verify team accounts or readers have permission to view specific categories/articles in the widget
2. Check if category-level access is configured. If so, manually add desired categories in the content access section during widget configuration

**To add categories to the widget:**

1. Navigate to **Knowledge base widget** in the Knowledge base portal
2. Hover over the desired widget and click **Edit**
3. In the **Configuration & connect** tab, expand the **Content access** section
4. Select **Category** and choose desired categories
5. Click **Save**

#### The Knowledge base widget is not loading on the Knowledge base site. How can I fix this?

Most likely caused by an outdated API key. Update the API key to restore widget functionality.

---

## URL Mapping

The **URL Mapping** feature allows you to control which articles and categories appear based on the pages your users visit. This improves user experience by directing them to relevant content and lets you hide the widget on certain URLs or customize search placeholders.

---

## Using URL mapping

Configure URL mapping by performing specific actions within the knowledge base widget for designated URLs.

### Actions

Four actions available with URL mapping:

1. **Show article:** Displays a single article on specified URL
2. **Show list of articles:** Lists selected articles under **Recommended** section on specified URL
3. **Show search results:** Sets specific search term to query knowledge base, returning relevant results on specified URL
4. **Hide widget:** Prevents Knowledge Base widget icon from appearing on specified URL

Find these actions under the **URL Mapping** tab or when editing existing mappings.

> NOTE
>
> Knowledge base widget must be installed on your site or app for URL Mapping to work. See [Installing the Knowledge base widget](/help/docs/installing-the-knowledge-base-widget)

### URL Parameters

Three types of parameters when configuring Knowledge Base widget URL:

1. **Include Path**: `/thisis/a/path`
2. **Include Query**: `?animal=bear`
3. **Include Hash**: `#inbox`

Enable **Is Regex** toggle to incorporate regular expressions into URL configurations.

---

## Adding URL Mapping to your Widget

To integrate desired widget into knowledge base site:

1. Navigate to **URL Mapping** tab in **Widget** in Knowledge base portal
2. Click **New URL mapping** and specify:

   * **Name** - Only shown on URL mapping record within Document360
   * **URL structure** - Select URL parameter type (**Include path**/**Include query**/**Include hash**). Enable at least one parameter
   * Type URL where you want article/category to show or action to occur

     > NOTE
     >
     > Domain name not included in URL path. For `https://document360.com/ebook/rapid-guide-to-launch-your-knowledge-base/`, URL Path is `/ebook/rapid-guide-to-launch-your-knowledge-base/`
   * **Action** - Select desired action
   * **Select workspace** - Choose version (if multiple versions exist)
   * **Language to** - Select language (if multiple languages exist)
   * **Article to show** - In search bar, select articles/categories to show from knowledge base documentation

   NOTE

   Folder categories not available for selection. Only **page** and **index** category types available.

3. Click **Create**

![1_URLmapping.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_URLmapping.gif)

When users access specified URL path and open Knowledge Base widget, they see mapped article/category. This remains consistent as they navigate between widget tabs within same version and language.

---

## Editing URL mapping

To modify existing URL mapping:

1. Navigate to **Widget** in Knowledge base portal
2. Hover on desired Knowledge base widget and click **Edit**

   In **URL mapping** tab, find list of available URL mappings
3. Hover over desired URL mapping and click **Edit**

   **Update URL mapping** blade appears
4. Update information and click **Update**

![2_urlmapping_edit.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_urlmapping_edit.gif)

---

## Deleting URL mapping

To delete URL mapping:

![3_urlmapping_delete.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_urlmapping_delete.png)

1. Navigate to **Widget** in Knowledge base portal
2. Hover on desired Knowledge base widget and click **Edit**
3. In **URL mapping** tab, find list of available URL mappings
4. Hover over desired URL mapping and click **Delete**
5. Click **Yes** in **Delete confirmation** prompt

---

## URL mapping settings

Define Knowledge base widget behavior for URLs without configured mapping to improve user experience.

![4_urlmapping_settings.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_urlmapping_settings.png)

1. Navigate to **Widget** in Knowledge base portal > **Configure & connect**
2. Under **Set controls** section, expand **URL mapping settings** section
3. Select desired option:

   * **Navigate to the page help/knowledge base**: Display article/category in Page help or Knowledge base tab
   * **Do not make any changes to the existing setup**: Display last opened article/category
4. Click **Save**

---

## Basic URL matching

Understanding URL matching is crucial for effective URL mapping. General-purpose regex for typical URLs:

```
^https?://?[a-zA-Z0-9.-]+/[a-zA-Z0-9/._-]*??[a-zA-Z0-9=&._-]*?#[a-zA-Z0-9_-]*?$
```

Regex

Copy

**Component explanation:**

* `^https?://?`: Matches protocol (`http://` or `https://`). The `?` makes protocol optional

  > NOTE
  >
  > Add backward slash (\) before every forward slash (/) when testing on https://regex101.com
* `[a-zA-Z0-9.-]+`: Matches domain name including letters, numbers, dots (`.`), and hyphens (`-`)
* `/[a-zA-Z0-9/._-]*?`: Matches path after domain, allowing slashes, alphanumeric characters, dots, underscores, and hyphens
* `?[a-zA-Z0-9=&._-]*?`: Matches optional query parameters (`?key=value`)
* `#[a-zA-Z0-9_-]*?`: Matches fragment (`#section`)

---

### Examples of URL mapping using Regex

#### **Mapping URLs with specific paths**

For URL pattern like `/users/{id}`:

```
^/users/[0-9]+$
```

Plain text

Copy

Captures user ID dynamically.

**Example Matches:**

* `/users/123`
* `/users/456`

#### **Mapping URLs with query parameters**

For URLs like `/search?q={query}`:

```
^/search?q=[a-zA-Z0-9]+$
```

Regex

Copy

**Example Matches:**

* `/search?q=apple`
* `/search?q=123abc`

#### **Mapping URLs with optional parameters**

For URL pattern like `/products/{category}/{id}` where category is optional:

```
^/products/[a-zA-Z]+?/[0-9]+$
```

Regex

Copy

**Example Matches:**

* `/products/123`
* `/products/electronics/123`

#### **Mapping URLs with wildcard or multiple paths**

For `/blog/*`:

```
^/blog/.*?$
```

Regex

Copy

**Example Matches:**

* `/blog`
* `/blog/how-to-code`
* `/blog/2021/10`

**Mapping URLs with subdomains**

For subdomain URLs:

```
^https?://?[a-zA-Z0-9-]+.example.com$
```

Regex

Copy

**Example Matches:**

* `http://blog.example.com`
* `https://shop.example.com`

#### Combining multiple components

Comprehensive regex matching URL with optional protocol, domain, path, query parameters, and fragment:

```
^https?://?[a-zA-Z0-9.-]+/[a-zA-Z0-9/._-]*??[a-zA-Z0-9=&._-]*?#[a-zA-Z0-9_-]*?$
```

Regex

Copy

---

## FAQs

**How can I remove the Page help and Search bar from the widget when URL mapping for a single article is configured?**

To hide Page help tab and Search bar:

1. Navigate to **Widget** in Knowledge base portal
2. Hover over desired widget and click **Edit**
3. Paste provided code in **Custom CSS** tab:

   ```
   li#page-help-tab {
       display: none;
   }

   .article-header .article-back-icon {
       display: none;
   }

   .search-container {
       display: none !Important;
   }
   ```

   CSS

   Copy
4. Paste provided code in **Custom JavaScript** tab:

   ```
   setTimeout(function() { $('.search-container').hide();}, 2000);
   setTimeout(function() { $("#knowledge-base-tab").click();}, 2000);
   ```

   JavaScript

   Copy
5. Click **Save**

**How can I see the updates immediately in the KB Widget after adding or updating a URL Map?**

Updates cached on server for performance and refresh automatically every 15 minutes. Clear application cache for immediate changes.

---

## Customizing the Knowledge base widget using Custom CSS/JavaScript

Customizing the Knowledge Base (KB) widget allows personalization of appearance and behavior to match branding or specific functionality needs. This includes customizing the widget icon, setting up buttons for interaction, managing callbacks for show/hide functionality, and applying styling and localization adjustments.

---

## How to change the default widget icon?

Replace default Knowledge Base widget icon with custom one that fits brand design.

### **Creating a custom button**

To add custom button interacting with Knowledge Base widget:

1. Add new HTML element, button for example, anywhere on page:

   ```
    <button id="doc360_help_btn" class="btn hide"><span>Help!</span></button>
   ```

   XML

   Copy
2. Assign element CSS class including `display: none`:

   ```
   .hide
   {
       display:none;
   }
   ```

   CSS

   Copy

### **Setting up callback functions**

Control visibility of custom button based on Knowledge Base widget state using JavaScript callback functions.

Add following [callback functions](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) to JavaScript files or inside `<script>` tag.

**Show button when widget loads:**

```
function doc360_callback()
{	
    document.getElementById('doc360_help_btn').classList.remove('hide');
}
```

JavaScript

Copy

**Show button after being hidden by URL mapping:**

`doc360_callback` removes `display: none` from button. Executed when Knowledge Base widget completes loading.

```
function doc360_show_callback()
{
    document.getElementById('doc360_help_btn').classList.remove('hide');
}
```

JavaScript

Copy

**Hide button based on URL mapping:**

`doc360_show_callback()` removes `display: none` from button. Executed if button was previously hidden by URL mapping.

```
function doc360_hide_callback()
{
    document.getElementById('doc360_help_btn').classList.add('hide');
}
```

JavaScript

Copy

`doc360_hide_callback()` adds `display: none` to button. Executed by [URL mapping](/help/docs/url-mapping) if valid map found to hide Knowledge Base widget.

> NOTE
>
> Show and hide callbacks only necessary if hiding widget on specific pages using URL mapping

### Integrating the callback functions

Make widget recognize custom callbacks by modifying Knowledge Base widget's JavaScript snippet:

```
<!-- Document360 Knowledge Base assistant Start -->
<script>
    (function (w,d,s,o,f,js,fjs) {
        w['JS-assistant']=o;w[o] = w[o] || function () { (w[o].q = w[o].q || []).push(arguments) };
        js = d.createElement(s), fjs = d.getElementsByTagName(s)[0];
        js.id = o; js.src = f; js.async = 1; fjs.parentNode.insertBefore(js, fjs);
    }(window, document, 'script', 'mw', 'https://cdn.document360.io/static/js/assistant.js'));
    mw('init', { apiKey: 'YOUR KEY', 
                   callback:  doc360_callback, 
                   show_callback: doc360_show_callback,  
                   hide_callback: doc360_hide_callback });
</script>
<!-- Document360 Knowledge Base assistant End -->
```

JavaScript

Copy

### **Making the button open the widget**

Make button open Knowledge Base widget when clicked using pure JavaScript or jQuery.

**Using Pure JavaScript:**

```
document.getElementById('doc360_help_btn').addEventListener('click', function () { 
    document.getElementById('document360-assistant-iframe').contentDocument.getElementById('doc360-button').click();
});
```

JavaScript

Copy

**Using jQuery:**

```
$('#doc360_help_btn').click(function() {
    $('#document360-assistant-iframe').contents().find('#doc360-button').click();
}); 
```

JavaScript

Copy

### **Customizing the button's appearance**

Apply custom CSS to button to match website branding. Change colors, font styles, or add effects.

---

## How to change dark theme in Knowledge base widget?

Use Custom JavaScript for this customization.

1. Navigate to **Knowledge base Widget** in Knowledge base portal and click **Edit**

![kbwidget_darktheme.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1730066025105.png)

2. Open **Custom CSS** tab, paste snippet below, and click **Save**

```
.doc360-widget-modal {
    background-color: black;
    color: white;
}
 
.doc360-widget-modal div,
.doc360-widget-modal li,
.doc360-widget-modal p,
.doc360-widget-modal ul,
.doc360-widget-modal span,
.doc360-widget-modal input,
.doc360-widget-modal textarea {
color: white !important;
  background-color: black !important;
}
 
.doc360-widget-modal button {
  color: white !important;
}

.eddy-feedback-btn:hover {
    color: black !important;
    background-color: #e4e4e7 !important;
}

.eddy-feedback-btn {
    background-color: black !important;
}
```

CSS

Copy

---

## How to change the fields displayed in the Knowledge base Widget?

Use Custom JavaScript for this customization.

1. Navigate to **Knowledge base Widget** in Knowledge base portal and click **Edit**

![kbwidget_changefields.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1730066068782.png)

2. Open Custom JavaScript tab to paste snippet below

```
$(document).ready(function() {
    if ($('.tab-link.current').length > 0) {
        $('.tab-link.current').html($('.tab-link.current').html().replace("Page help", "Destek"));
        $('.tabs li:last-child').html($('.tabs li:last-child').html().replace("Knowledge base", "DokÃ¼matasyon"));
    }

    setTimeout(function() {
        $('#top-search-title').html($('#top-search-title').html().replace("Top search articles", "En Ã‡ok Aranan DokÃ¼manlar"));
    }, 3000);
});
$(document).ready(function() {
    $('#search-input').each(function(ev) {
        if (!$(this).val()) {
            $(this).attr("placeholder", "Arama");
        }
    });
    $('#category-filter').each(function(ev) {
        if (!$(this).val()) {
            $(this).attr("placeholder", "Filtrele");
        }
    });
});
```

JavaScript

Copy

3. Replace text as needed
4. Click **Save**

---

## How to set the Knowledge base Widget to open automatically in the knowledge base site?

Use Custom JavaScript for this customization.

1. Navigate to **Knowledge base Widget** in Knowledge base portal and click **Edit**

![kbwidget_autoopen.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1730066097873.png)

2. Open Custom JavaScript tab, paste snippet below, and click **Save**

```
$(function() {
setTimeout(function(){
let iframe = $('#document360-widget-iframe');
let button = iframe.contents().find('#doc360-button');
button.trigger("click");}, 2000);
});
```

JavaScript

Copy

---

## FAQ - Knowledge base widget

#### 1. What is a Knowledge base widget?

Knowledge base widget helps users find answers without leaving your site or application. Assists users in finding solutions to common questions, troubleshooting issues, and learning about new features - all within the application.

---

#### 2. How is the Knowledge base widget useful for the users?

Here are some scenarios where Knowledge base widget proves helpful:

* **User onboarding**: New app users access widget to learn basics - account setup, UI navigation, common tasks - without leaving application
* **Technical support**: When users encounter problems or error messages, they search Knowledge base for solutions instead of contacting customer support or searching externally
* **Learning about new features**: As apps update with new features, users access widget to learn changes, usage, and benefits - improving overall experience and adoption

---

#### 3. Is it possible to configure multiple Knowledge base widgets?

Yes, configure up to 10 Knowledge base widgets per project.

---

#### 4. How to change the position of the Knowledge base widget icon on your website?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. In **Style your widget** section, find **widget position**
3. Select **Left** or **Right** button to change icon position
4. Enter desired spacing values in **Side spacing** and **Bottom spacing** fields
5. Click **Save**

---

#### 6. How to turn off the top search in the Knowledge base widget?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. In **Style your widget** section, enable **Hide top search** toggle
3. Click **Save**

---

#### 7. Why does a configured URL mapping appear broken?

URL mapping breaks due to changes in 'Filter widget content' configuration in 'Installation & setup' tab. Check URL mapping and update configuration.

---

#### 8. How do I set my desired logo as a widget icon?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. In **Style your widget** section, find **widget icon**
3. Click **Change icon** button
4. Choose/upload desired icon
5. Click **Save**

---

#### 9. How to hide the Knowledge base widget?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. In **Style your widget** section, enable **Hide widget** toggle
3. Click **Save**

---

#### 10. Can I add custom links in the Knowledge base widget?

Yes.

---

#### 11. What is URL mapping?

URL mapping makes specific articles/categories appear in knowledge base widget based on user's current page. Also hide widget on specific URLs or provide search bar with custom placeholders.

---

#### 12. How to enable Ticket deflector in the Knowledge base widget?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. Enable **Show ticket deflector** toggle
3. Click **Save**

---

#### 13. Can I add regular expressions (regex) in URL mapping?

Enable **Is Regex** toggle to include regular expressions.

---

#### 14. What is regex?

Regex ("regular expression") defines search pattern to match and manipulate text strings.

> For example, configure single URL mapping for 20 articles with similar URLs:
>
> * `https://example.com/drive-General`
> * `https://example.com/drive-settings`
> * `https://example.com/drive-functionA`
>
> Without regex, add individual URL mappings for each. With regex, single mapping suffices: Select "Include path" and add `docs/drive` in URL field.

---

#### 15. Can I add URL mapping for categories?

Yes. Applies only to page and index categories.

---

#### 16. How to remove the Knowledge base widget icon from an article?

1. Go to **URL mapping** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. Create new URL mapping with **Hide** action for desired article

---

#### 17. What is the default language behavior of the Knowledge base widget?

Widget opens in default browser language. If unavailable, default Knowledge base language appears.

#### 18. How do I restrict the Knowledge base widget to a specific domain?

1. Go to **Installation & Setup** tab of desired Knowledge base widget (**Knowledge base widget** > **Edit**)
2. In **Style your widget** section, find **Keep your widget secure**
3. Enter domains where Knowledge base widget should display
4. Click **Add** > **Save**

---

## Knowledge base site 2.0

Knowledge Base Site 2.0 improves article access and information browsing. Enhanced UI, better AI-powered search, and streamlined content organization help users find relevant articles and troubleshoot efficiently. Real-time updates and interactive elements simplify navigation and engagement.

> For migration from KB site 1.0 to KB site 2.0, see [**KB site 2.0 migration**](/help/docs/kb-site-20-migration)

---

## Overview of Knowledge base site 2.0

![Image showing sections of Knowledge base site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-Knowledge_base_site_2.0.png)

### 1. Header section

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-New_Header_section_of_Knowledge_base_site_2.0(1).png)

1. **Logo image:** Organization branding/logo. Click navigates to documentation home page
2. **Workspace:** Dropdown to navigate different Knowledge base workspaces. Click API documentation workspace to go to API home page
3. **Primary navigation:** Customize to navigate different pages from home or Knowledge base site
4. **Announcement icon:** "What's New" page shows recently published articles (new and forked) in selected workspace
5. **Acknowledgment required:** Page displays acknowledgment required/acknowledged articles
6. **Theme:** Switch between System theme, light, and dark themes. Light theme set as system theme by default
7. **Language:** Select desired language to read articles
8. **Secondary navigations:** Customize to navigate different pages from home or Knowledge base site

---

### 2. Left navigation pane

![Overview of the Knowledge base site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Screenshot-left_side%20pane_KBsite2.0.png)

1. **Search bar:** Access search function or use shortcut Ctrl + K (Command + K on Mac). Search Knowledge base articles or use Eddy AI search. See [Search](/help/docs/document360-search)
2. **Hide navigation menu:** Click to hide left pane for wider article view
3. **Tree view:** View category/article hierarchy in clear tree structure
4. **Article status:** Color badge represents article status (new, updated, custom). See [Article status](/help/docs/article-status)
5. **Context menu:** Private/mixed project users hover for options:

   * **Follow category/article:** Click to receive notifications for new/updated articles. Available only in private/mixed projects. See [Follow articles and categories](/help/docs/follow-articles-and-categories)
   * **Export PDF:** Export article/category as PDF

---

### 3. Article section

![Knowledge base site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-New_Article_section_of_Knowledgemnt_base_Site_2.0.png)

1. **Breadcrumbs:** Navigate back to article category/sub-category
2. **Article title:** Displays article title
3. **Copy link:** Click to copy article URL to clipboard
4. **Status badge:** Displays article status (new, updated, custom)
5. **Article date:** View published/updated date
6. **Read time:** View estimated reading time based on word count
7. **Contributors:** View list of article contributors
8. **Share icon:** Share article via Twitter, LinkedIn, Facebook, or Email
9. **More sharing options:** Download article as PDF or print
10. **Follow:** Click to follow articles. Available for reader accounts
11. **Article summary:** Click to view Eddy AI-generated article summary
12. **Acknowledgement required:** Scroll to article end and acknowledge

---

### 4. Image

When clicking images on Knowledge base site, they open in image viewer.

* **Title text:** Displays image caption, if any
* **Open link:** Open image URL, if available
* **Zoom out:** Minimize image
* **Zoom in:** Enlarge image
* **Download:** Download image to local storage
* **Close:** Close image
* **Next:** Move to next image
* **Previous:** Move to previous image

Hold and drag image to move anywhere on screen. Click anywhere outside image to close.

![Knowledge base site view of an image](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_ScreenShot-Knowledge_base_site_2.0.png)

---

### 5. Right side pane

![Overview of the Knowledge base site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Screenshot-Right%20side%20pane_KBsite2.0.png)

1. **Hide navigation menu:** Click to hide right pane for wider article view
2. **Files:** View article attachments
3. **Tags:** View article tags
4. **In this article:** View article headings (formerly "Table of Contents")

---

### 6. Article footer

![Article footer of the Knowledge base site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Footer_section_of_Knowledge_base_site_2_0.png)

1. **Article feedback:** Click **Yes** or **No** and enter feedback
2. **Previous and Next Article:** Navigate to previous/next articles in category
3. **Related articles:** View list of related articles

---

## Troubleshooting

Step-by-step guidance for common Knowledge base site management/access challenges.

### Website fails to load after entering the URL

Possible causes: incorrect URL entry, browser cache issues, VPN interference, network problems, server downtime, outdated browsers, or incorrect system date/time settings.

**Steps to resolve:**

1. Ensure website URL entered correctly
2. Reload page
3. Clear browser cache:

   * Right-click page and select **Inspect** to open developer tools
   * Right-click browser reload button and choose **Hard reload** or **Empty cache and Hard reload**
4. Check if VPN active on device. Disable and attempt site access again
5. Ensure system date, time, and time zone set correctly

Contact support if issue persists.

### 504 gateway timeout while accessing the site

**Error:** 504 gateway timeout

Possible cause: sub-folder configuration issues.

**Steps to resolve:**

1. Check recent web server configuration changes:

   * Review location blocks/configuration files for recent changes
   * If changes identified, revert to previous state
2. Verify sub-folder configuration:

   * Change in sub-folder slug within Sub-folder Configuration may cause issue
   * Revert recent sub-folder configuration changes

See [Hosting Document360 on a sub-directory](https://docs.document360.com/docs/document360-on-a-sub-folder)

### Page unresponsive while editing an article

**Error:** Page isn't working. example.com redirected too many times. ERR_TOO_MANY_REDIRECTS.

Possible causes: outdated browser cache, overly large articles, missing/improperly closed HTML tags, or excessive redirects from incorrect configurations.

**Steps to resolve:**

1. **Clear browser cache:** Outdated/corrupted cache interferes with page functionality. Clear, reload, and check if issue persists
2. **Reduce article length:** Large articles cause performance issues. Split into smaller sections under relevant categories
3. **Check for missing closed tags:** Ensure all HTML tags have closing tags, especially in Markdown. Elements like `<table>`, `<div>`, and `<p>` must be properly closed

### Page isn't working due to too many redirects

**Error:** Page redirected too many times

Possible causes: incorrect JWT Login URL configuration, domain URL as Login URL causing redirect loops, or outdated JWT settings.

**Steps to resolve:**

1. **Check recent changes:** Review JWT Login URL updates in configuration
2. **Correct Login URL:** Ensure domain URL not set as Login URL to prevent multiple redirects
3. **Update JWT configuration:** Remove incorrect Login URL and replace with correct one

See [JWT article](https://docs.document360.com/docs/configuring-the-jwt-sso)

### Sorry! Project not found during custom domain configuration

**Error:** Sorry! This project does not exist.

Possible causes: incorrect/missing CNAME record configuration, expired CNAME records, or incomplete domain verification.

**Steps to resolve:**

1. **Verify CNAME Record:** Ensure CNAME record added correctly. Click 'Verify' button on custom domain page. Custom domain activates immediately after verification
2. **Check for CNAME expiry:** If CNAME updated in DNS after delay, it may have expired, preventing verification
3. **Reconfigure domain:** Reconfigure custom domain, update CNAME record, and verify in Document360

See [custom domain mapping article](https://docs.document360.com/docs/custom-domain-mapping)

### Encountering "/home/error/" message while accessing the site

**Error:** /home/error/

Possible causes: incorrect site configuration, server-side issues, or unresolved backend errors.

**Steps to resolve:**

1. **Contact support:** Email [**support@document360.com**](mailto:support@document360.com) with:

   * Screen share video demonstrating issue
   * Steps to reproduce error, if possible
2. **Provide HAR file:** Follow steps in [guide](https://docs.document360.com/docs/document360-support-generating-a-har-file) to download HAR file
3. **Share console errors:**

   * After downloading HAR file, click 'console' tab in browser developer tools
   * Screenshot console errors and include in email

### Icons not rendering correctly on user site

Broken icons typically result from unintended modification of Document360's FontAwesome family. Changes to other classes/HTML tags may alter icon font settings.

To avoid this issue:

* Ensure site styling/class definitions don't impact FontAwesome classes or font family settings
* When targeting specific elements, double-check icon-related styles remain intact

**Steps to resolve:**

1. **Inspect broken icon:**

   * Use browser developer tools to inspect user site
   * Click broken icon with selector tool to identify issue
2. **Check custom CSS:**

   * Navigate to **Settings** > **Knowledge base site** > **Customize site** > **Custom CSS & JavaScript**
   * Review font rules applied to various classes. Font changes may unintentionally apply to broader classes, affecting icons
   * Apply font changes only to specific classes requiring them

Contact [Document360 support](https://document360.com/support/) if issue persists.

### Knowledge base site loading without CSS styling

Typically occurs when site accessed from network blocking/whitelisting Document360 domains.

**Steps to resolve:**

1. Verify site works correctly from different network. If so, issue relates to network restrictions
2. Whitelist following domains in network settings for proper access

![Image showing domains to whitelist](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-troubleshooting.png)

### Secure connection issues on knowledge base site

**Error:**

* Site can't provide secure connection
* Connection isn't private
* Connection not secure

**Steps to resolve:**

1. **Check CAA Record in DNS:**

   * Verify CAA (Certification Authority Authorization) record added for Knowledge base site
   * If no CAA record found, inspect SSL certificate. Refer to steps in provided video
2. **Update CAA Record:**

   * Based on SSL certificate provider, add corresponding CAA record to DNS
   * For Let's Encrypt, add specified CAA record. Ensure correct record for certificate type
3. **Reference for CAA Records:**

   Learn more about CAA records: [CAA Record and Why It Is Needed](https://www.namecheap.com/support/knowledgebase/article.aspx/9991/38/caa-record-and-why-it-is-needed-ssl-related/#caa_how)
4. **Contact DNS Provider:**

   If issue persists during custom domain setup, contact DNS provider to confirm additional issues

Contact [Document360 support](https://document360.com/support/) if issue persists.

### Encountering "ResourceNotFound" error accessing images/files/attachments

**Error:** ResourceNotFound

Occurs when SaaS token not appended to file URL in **private** and **mixed projects**. Document360 appends SaaS token to ensure authorized access.

**Steps to resolve:**

* Ensure SaaS token appended to file URL before accessing/sharing
* Try downloading file again directly from Document360

![Error message indicating resource not found](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1739344746842.png)

### Encountering "AuthenticationFailed" error accessing images/files/attachments

**Error:** AuthenticationFailed

Occurs when **SaaS token** expired in **private** and **mixed projects**. SaaS token valid for **15 minutes** before automatic update. If shared with expired token, users can't access file.

**Steps to resolve:**

* **Refresh source webpage** and generate new file link
* Share file within valid token period (15 minutes for standard files, 1 hour for video files)

![Error message indicating authentication failure](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Screenshot-Troubleshooting-Authentication%20failed.png)

---

## Customize site

In Document360 projects, manage Knowledge base site design/customization from unified **Customize site** feature. Tailor site to align with brand identity and user preferences - select themes, adjust colors, personalize layouts.

> Available in KB Site 2.0. See [KB site 2.0 migration](/help/docs/kb-site-20-migration)

> **Customize site** is project-level setting. Changes reflect across entire project.

---

## Basic site customization

To perform basic customization:

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal

   Page holds all basic site design configurations
2. Choose theme from **Site theme** field:

   * Both Light & Dark
   * Light only
   * Dark only
3. In **Branding** section, choose **Logo** and **Favicon**. Set custom redirection link for logo - users redirect to specified link when clicking logo

   > Customers with existing customized logo/favicon unaffected until navigating to **Customize site** settings and saving changes
4. In **Colors** section, select **Auto set color contrast to meet** [**WCAG**](https://www.w3.org/TR/WCAG21/) **standards** checkbox to automatically apply brand colors

   > See [Web Content Accessibility Guidelines (WCAG)](/help/docs/web-content-accessibility-guidelines-wcag)

   * In **Brand color** section, choose primary color for CTAs, selection states, etc.
   * In **Hyperlink color** section, customize hyperlink color to enhance user experience:

     + **Use industry standard:** Applies commonly used hyperlink color
     + **Use brand color:** Applies chosen brand color
     + **Use a different color:** Select default, hover, and visited colors for hyperlinks
5. In **Fonts** section, change Knowledge base content fonts anytime:

   * **Article font pairing:** Applied to all article titles and contents. Click **Have a specific font combination in mind?** for more options
   * **Site font:** Select font from dropdown. Applied throughout Knowledge base site - left navigation pane, header/footer navigations, controls
6. In **Styling** section, choose button/form element style:

   * Rounded
   * Sharp
   * Bubble
7. In **Site layout** section, choose:

   * **Full width:** Content extends to browser window edges
   * **Center:** Content fits more centrally in browser window
8. Click **Save**

![Configuring basic customization](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Basic_site_customization.gif)

---

## Advanced site customization

Personalize website by incorporating branding elements, header/footer sections, homepage, login page, and error pages in one central location.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal

   Page holds all basic site design configurations
2. Click **Customize site**
3. Configure site elements:

   * [Site header & footer](/help/docs/site-header-and-footer): Customize [Header](/help/docs/header-primary-navigation), [footer](/help/docs/footer-navigation), etc.
   * [Main pages](/help/docs/main-pages): Customize Home, Documentation, and Login pages
   * [Error pages](/help/docs/error-pages): Customize [404 page](/help/docs/404-page), [Access denied](/help/docs/access-denied-page), [Unauthorized](/help/docs/unauthorized-page), and [IP restrictions](/help/docs/ip-restriction-page) pages
   * [Custom CSS / JavaScript](/help/docs/custom-css-javascript): Add advanced styling or interactivity

   Changes applied on left section previewed on right window. Click desired item in Preview window to edit specific element
4. Use dropdown to choose different pages

   New Home page builder interface provides easier navigation and customization
5. Click **Save** to save changes
6. Click **Preview** to see site appearance
7. Click **Publish** to commit changes

![Configuring advanced customization](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Advanced_site_customization.gif)

---

### FAQs

#### How do I change the site theme?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Site theme** section, choose from:

   * Both Light & Dark
   * Light only
   * Dark only

#### How do I change the Favicons?

Favicon (16x16 pixels) identifies website in browser tabs, bookmarks, and history.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Branding** section, hover over default favicon and click **Click to change**
3. Add Favicon via:

   * **Using a URL:** Paste image URL and click **Insert**
   * **Upload an image:** Choose file from Drive or upload from local storage and click **Insert**
4. Click **Save**

> **PRO TIP**
>
> * Use minimalistic, square images
> * Ensure favicon sized at 48 x 48 pixels for optimal rendering

#### Why is the favicon added not rendering on the Knowledge base site?

Favicon doesn't meet specified criteria (size/format). Make necessary changes or re-upload.

#### How do I change the site logo?

Replace default **Logo** by uploading desired logo.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Branding** section, hover over default **Logo** and click **Click to change**
3. Add Logo via:

   * **Using a URL:** Paste image URL and click **Insert**
   * **Upload an image:** Choose file from Drive or upload from local storage and click **Insert**
4. Click **Save**

#### How do I add text as the logo?

Replace default logo with text.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Branding** section, click **Don't have a logo? Use name instead**
3. Enter desired text (company name/tagline)

   > Up to 30 characters allowed
   > Maximum logo size: Height - 40 px, Width - 270 px
   > Larger logos scaled down to fit maximum size
4. Click **Save**

#### How do I add custom logo URL?

Add clickthrough URL to logo. Users redirect to provided link when clicking logo.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. Add desired URL in Logo URL field
3. Click **Save**

> If no logo URL added, clicking logo redirects to Knowledge base home page
> Custom logo URL optional field

#### How do I set a different logo for different themes?

KB site 2.0 projects can add custom code for different logos per theme.

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** > **Custom CSS & JavaScript** in Knowledge base portal
2. From left navigation pane, click **CSS** tab and paste CSS snippet:

```
.brand-logo img {
    content: url('Paste the Light mode logo URL here');
}

/* Override logo image when theme is set to "dark" */
html[data-bs-theme="dark"] .brand-logo img {
    content: url('Paste the Dark mode logo URL here');
}
```

CSS

Copy

#### How to choose the brand color?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. Under **Colors**, choose **Brand** color for CTAs, selection states, etc.

> If **Auto set color contrast to meet WCAG standards** chosen, light/dark theme colors set automatically. Otherwise, manually set colors for each theme

3. Click **Save**

#### How do I choose font family in customize site?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. Under **Fonts** section:

* **Article font pairing:** Applied to article Titles and Contents

> Click **Have a specific font combination in mind?** for more options

* **Site font:** Select from dropdown. Applied throughout Knowledge base site - left navigation pane, header/footer navigations, controls

3. Select desired font and click **Save**

> See [How to configure a custom font](/help/docs/how-to-configure-a-custom-font-in-the-knowledge-base)

#### How do I change the default paragraph style?

No direct option exists. Change default article font in Document360 editor.

To set default font for articles:

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Fonts** section, choose desired font pair in **Article font pairing** tile

   > For instance, if drafting in `Verdana` but selecting `Ubuntu + Open Sans` for **Article font pairing**, Knowledge base site shows article title in `Ubuntu` and content in `Open Sans`

> Can select custom fonts. See [How to configure a custom font](/help/docs/how-to-configure-a-custom-font-in-the-knowledge-base)

To change paragraph style for individual articles:

1. Open desired article in **Advanced WYSIWYG editor** and select text
2. Click **Format**, then choose font style in **Typography** section

#### How do I change the button styles?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Styling** section, select button style:

   * Rounded
   * Sharp
   * Bubble

#### How do I change the site layout in customize site?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. Under Layout, find:

* **Full width:** Content extends to browser window edges
* **Center:** Content fits more centrally in browser window

3. Click **Save**

#### How do I set the default font for my articles on the Knowledge base site?

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal
2. In **Fonts** section, choose desired font pair in **Article font pairing** tile

   > If drafting in `Verdana` but selecting `Ubuntu + Open Sans`, Knowledge base site shows article title in `Ubuntu` and content in `Open Sans`

> Can select custom fonts. See [How to configure a custom font](/help/docs/how-to-configure-a-custom-font-in-the-knowledge-base)

---

## KB site 2.0 migration

Document360 introduces Knowledge Base Site 2.0 with advanced customization capabilities and new functionalities like following articles/categories, sharing via private links, enhancing user experience and engagement.

> KB Site 2.0 accessible by default for projects created after June 10th, 2024

---

## Customizing your knowledge base site 2.0

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in Knowledge base portal

   **Customize site** page appears
2. New banner displays to upgrade to Knowledge base site 2.0

> Banner displayed exclusively for Document360 1.0 Standard plan projects

3. Click **Experience 2.0** in banner to explore KB site 2.0 preview
4. Two tabs appear: Site 1.0 (Active) and Site 2.0 (Preview). Site 2.0 tab selected by default
5. In **Site 2.0** tab, view **Knowledge Base Site 2.0 preview** banner with options:

   * Go live with Site 2.0
   * Customize site
   * Preview site 2.0
   * How to configure

![1_Screenshot-Customize_site_page_Kb Site 2.0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Customize_site_page_Kb%20Site%202.0.png)

### **a. Go live with Site 2.0**

1. Click **Go live with Site 2.0** to publish KB Site 2.0 with same functionalities as KB Site 1.0, without customization

   **Publish confirmation** panel appears

> Cannot deselect configurations first time editing

2. Click **Continue**

   **Switch from Knowledge base site 1.0 to 2.0** panel appears
3. Enter project subdomain and click **Switch to 2.0**

   Migrated to KB site 2.0

> From KB Site 1.0, logo, favicon, primary color, link colors, title & body font, and site layout retained

4. Within 30 days, can revert to KB Site 1.0 by clicking **Rollback to Site 1.0**. Team reviews request and reverts site to version 1.0

> After rollback, system stores last saved KB site preview

![2_ScreenGIF-Go_Live_Site_2_0_Migration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Go_Live_Site_2_0_Migration.gif)

### **b. Customize site**

1. Click **Customize site**

   Overview of customize site page appears
2. Customize various pages: Site header & footer, Main pages, Error pages, Custom CSS & JavaScript
3. Click **Save** to save changes as draft
4. Click **Preview** to view changes in Knowledge base site
5. Click **Go live with Site 2.0** to publish changes
6. Select desired configurations and click **Continue**

   **Switch from Knowledge base site 1.0 to 2.0** panel appears
7. Enter project subdomain and click **Switch to 2.0**

![3_ScreenGIF-Customize_site_2.0_option_Migration_2_0](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGIF-Customize_site_2.0_option_Migration_2_0.gif)

### **c. Preview site 2.0**

Click **Preview site 2.0** to view KB site 2.0 with default branding elements retained from KB site 1.0

### **d. How to configure**

Click **How to Configure** for instructional video

---

### FAQ

**Will I lose any integrations or extensions when switching from KB site 1.0 to KB site 2.0?**

No. All integrations and extensions configured in KB site 2.0 continue working seamlessly.

---

## Web Content Accessibility Guidelines (WCAG)

In digital age, accessibility is necessity, not feature. Ensuring all users can access and use products is cornerstone of inclusive design. Document360 complies with WCAG 2.1 A and AA standards.

> WCAG available exclusively in KB Site 2.0 for projects created after June 10th, 2024

---

## Implementing WCAG 2.1 A and AA in Document360

Document360 aligned with WCAG 2.1 A and AA guidelines:

1. **Text alternatives:** Provide text alternatives for non-text content like images/icons for screen readers
2. **Keyboard navigation:** Full keyboard navigation enables access without mouse
3. **Readable text:** Clear fonts, appropriate contrast ratios, simple language enhance readability

![WCAG 2.1](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-WCAG.gif)

---

## Key Principles of WCAG 2.1

WCAG 2.1 organized around four core principles:

1. **Perceivable:** Information/interface components presented in perceivable ways. Includes text alternatives for non-text content
2. **Operable:** Interface components/navigation easy to use. All functionality available from keyboard, sufficient time to read/use content, easy navigation/find content
3. **Understandable:** Information/interface operation understandable. Text readable/comprehensible, web pages operate predictably
4. **Robust:** Content robust enough for reliable interpretation by wide range of user agents, including assistive technologies. Ensures compatibility with current/future technologies

> See [**WCAG 2.0 Guidelines**](https://www.w3.org/TR/WCAG21/)

---

## Header - Primary navigation

Primary navigation header is bar next to logo at top of site. Add menus helping readers navigate different pages from Home page or Knowledge base site.## 404 Page

A 404 page appears when readers try to access nonexistent pages in the Knowledge base site. For example, attempting to access a deleted URL triggers the 404 page.

Customize this error page by adding a custom message and illustration. This improves user experience by guiding readers to relevant content instead of leaving them on a generic error page. Add links, titles, descriptions, and images that reflect your brand. Choose between basic or custom styling options.

> Once configured, you cannot revert to the default 404 page. Custom pages are recommended for better reader experience.

---

### Accessing the 404 page design settings

To access the 404 page:

1. Navigate to **Settings** () > **Knowledge base site** > **Customize site** in the Knowledge base portal.
2. Click **Customize site**.
3. From the left dropdown menu, select **404** under **Error pages**.
4. Choose from two options:
   * **Basic style**: Customize the default image only
   * **Custom style**: Add custom HTML and CSS. Use the **Preview** toggle to switch between code view and rendered view
5. Click **Save** to save changes.
6. Click **Preview** to see changes on the site.
7. Click **Publish** to activate changes on the Knowledge base site.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Accessing_404_pages_Design_settings.png)

---

### Customizing the 404 page

#### Basic style

1. Navigate to **Settings** () > **Knowledge base site** > **Customize site** in the Knowledge base portal.
2. Click **Customize site**.
3. From the left dropdown menu, select **404** under **Error pages**.
4. Select **Basic style**.
5. Click **Choose image** to select an image from Drive.
6. Click **Save** and then **Publish**.

#### Custom style

1. Navigate to **Settings** () > **Knowledge base site** > **Customize site** in the Knowledge base portal.
2. Click **Customize site**.
3. From the left dropdown menu, select **404** under **Error pages**.
4. Select **Custom style**.
5. Choose one of three options:
   * **Theme A**: Predefined theme with editable code
   * **Theme B**: Predefined theme with editable code  
   * **Blank**: Add custom HTML
6. Click **Preview** to view output without saving.
7. Click **Save** to apply changes.
8. Click **Publish** to activate changes on your Knowledge base site.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Customizing_the_404_page.gif)

---

### FAQ

#### Can I upload images from local storage for 404 page design?

Yes, you can import images from Drive or local storage.

#### Is it possible to switch back to the default static 404 page after configuring a custom one?

No. Once you configure a custom 404 page, you cannot revert to the default static page.## Customizing the 404 page

To customize the 404 page:

1. Navigate to **Settings** > **Knowledge base site** > **Customize site** in the Knowledge base portal.
2. Click **Customize site**.
3. From the left dropdown menu, select **404 page**.
4. Choose one of two customization options:
   * **Basic style**: Modify the default image, heading, paragraph, and buttons
   * **Custom style**: Add custom HTML and CSS
5. Click **Preview** to test changes.
6. Click **Save** to save changes.
7. Click **Publish** to activate changes on your Knowledge base site.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Accessing_custom_pages_Design_settings.gif)

---

### Basic style

#### Image

1. Click **Image**.
2. Click **Change** and choose:
   * **Default images**: Select from predefined images
   * **Image**: Provide URL or upload from drive
3. Set image alignment (left, center, or right).

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Upload_Image_Basic_style.png)

#### Heading

1. Click **Heading**.
2. Enter heading text.
3. Select text color.

Default: "404"

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Header_Basic_style_.png)

#### Paragraph

1. Click **Paragraph**.
2. Enter description.
3. Select text color.

Default: "Oops! Page not found"

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Paragraph_Basic_style_.png)

#### Buttons

Add up to three navigation buttons:

1. Click **Buttons**.
2. Click **Add button**.
3. Enter button text and destination URL.
4. Use **Delete** () to remove buttons or **Hide** () to temporarily hide them.
5. Click **Delete** at bottom to remove all buttons.
6. Click **Save** when finished.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Buttons_Basic_style_.png)

Suggested links:
* Home page
* Contact page/form
* Knowledge base sitemap
* Popular blog pages
* Key product/category pages

---

### Custom style

1. Select **Custom style**.
2. Switch between **HTML** and **CSS** sections.
3. Update code as needed.
4. Toggle **Preview** to view changes.
5. Click **Save** and **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Custom_style_preview.png)

> **Page not found** analytics show URLs generating 404 errors. Use redirect rules to fix broken links and improve user experience. See [Page not found analytics](/help/docs/page-not-found-analytics).

> **Links status** checks for broken links across your Knowledge base site. See [Link status](/help/docs/links-status).

---

### FAQ

#### What causes 404 errors?

* **Deleted URL**: Article removed without redirect
* **Changed URL**: URL modified without redirect rule
* **Subfolder path**: Changing subfolder from default "docs" causes errors (applies only when subfolder host is disabled)
* **Misconfigured redirect**: Redirect rule points incorrectly or causes loop
* **Incorrect URL**: Mistyped or improperly formatted URL (slugs must be lowercase)
* **Server issues**: Infrastructure problems preventing page load

#### Best practices for 404 pages

1. **Maintain design consistency**: Match site branding, colors, and fonts
2. **Use clear language**: Avoid technical jargon; acknowledge error humanely
3. **Provide navigation**: Include links to homepage, search, popular pages
4. **Add search bar**: Help users find what they're looking for
5. **Explain the issue**: Briefly mention broken links or moved content
6. **Include CTAs**: Link to support or broken link reporting
7. **Add personality**: Use humor or visuals to reduce frustration
8. **Ensure functionality**: Test all buttons and links
9. **Enable feedback**: Provide way to report issues
10. **Consider SEO**: Include proper meta tags and internal links
11. **Use engaging visuals**: Custom illustrations or animations
12. **Test mobile**: Ensure responsive design works on all devices

<a id="access-denied-page"></a>

## Access denied page

**Plans supporting error page**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Appears when users with limited permissions try to access restricted content. For example, readers accessing content outside their authorized categories in mixed knowledge bases.

Customize with clear messaging like: "You don't have permission to access this page. Contact your admin to request access."

> Only available for Private and Mixed projects. Cannot revert to default once customized.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Example_Access_denied_custom_page.png)

---

## Customizing the Access denied page

1. Navigate to **Settings** > **Knowledge base site** > **Customize site**.
2. Click **Customize site**.
3. Select **Access denied** page from left dropdown.
4. Choose customization option:
   * **Basic style**: Modify default image, heading, paragraph
   * **Custom style**: Add custom HTML and CSS
5. Click **Save** to save changes.
6. Click **Preview** to test changes.
7. Click **Publish** to activate.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Customizing_the_Access_Denied_page.gif)

---

### Basic style

#### Image

1. Click **Image**.
2. Click **Change** and choose:
   * **Default images**: Select from predefined options
   * **Image**: Provide URL or upload from drive
3. Set alignment (left, center, right).

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Image_basic_style_access_denied_page.png)

#### Heading

1. Click **Heading**.
2. Enter text.
3. Select color.

Default: "Sorry!"

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-heading_basic_style_access_denied_page.png)

#### Paragraph

1. Click **Paragraph**.
2. Enter description.
3. Select color.

Default: "You are not authorized to access this article or page."

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Paragraph_basic_style_access_denied_page.png)

---

### Custom style

1. Select **Custom style**.
2. Switch between **HTML** and **CSS** sections.
3. Update code.
4. Toggle **Preview** to view changes.
5. Click **Save** and **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Custom_style_access_denied_page.png)

---

### FAQ

**Is the Access denied page available for all project types?**

No. Only for Private and Mixed projects.

**Can I revert to default Access denied page?**

No. Once customized, default cannot be restored.

**How do I hide heading and paragraph elements?**

1. Navigate to **Settings** > **Knowledge base site** > **Customize site**.
2. Click **Customize site**.
3. Select **Access denied** page.
4. Hover over element and click **Hide** ().
5. Click **Unhide** () to restore.

> Image element cannot be hidden or deleted.

**Can I upload custom images?**

Yes. Use default images or upload your own.

**Best practices for Access denied pages**

* Use clear, instructive language: "Contact admin for access"
* Link to help resources or support
* Test responsive design on all devices

<a id="unauthorized-page"></a>

## Unauthorized page

**Plans supporting error page**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Appears when users without proper permissions access restricted content.

Customize with descriptive message explaining access restrictions and solution.

> Cannot revert to default once configured. Recommended for better user experience.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Example_Unauthorized_denied_custom_page.png)

---

## Customizing the Unauthorized page

1. Navigate to **Settings** > **Knowledge base site** > **Customize site**.
2. Click **Customize site**.
3. Select **Unauthorized** page from dropdown.
4. Choose option:
   * **Basic style**: Modify default elements
   * **Custom style**: Add custom HTML/CSS
5. Click **Save**.
6. Click **Preview**.
7. Click **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF_Accessing_Unauthorized_page.gif)

---

### Basic style

#### Image

1. Click **Image**.
2. Click **Change** and choose:
   * **Default images**: Predefined options
   * **Image**: URL or file upload
3. Set alignment.

#### Heading

1. Click **Heading**.
2. Enter text.
3. Select color.

Default: "Sorry!"

#### Paragraph

1. Click **Paragraph**.
2. Enter description.
3. Select color.

Default: "You are not authorized to access this article or page."

---

### Custom style

1. Select **Custom style**.
2. Switch between **HTML** and **CSS** sections.
3. Update code.
4. Toggle **Preview**.
5. Click **Save** and **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Custom_Style_in_Unauthorized.png)

<a id="ip-restriction-page"></a>

## IP restriction page

**Plans supporting error page**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Appears when users access the Knowledge base from restricted IP addresses.

Customize with clear instructions like: "Your IP address is not authorized. Contact admin for access."

> Only available for Enterprise plan projects. Cannot revert to default once customized.

---

## Customizing the IP restriction page

1. Navigate to **Settings** > **Knowledge base site** > **Customize site**.
2. Click **Customize site**.
3. Select **IP restriction** page from dropdown.
4. Choose option:
   * **Basic style**: Modify default elements
   * **Custom style**: Add custom HTML/CSS
5. Click **Save**.
6. Click **Preview**.
7. Click **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Accessing_IP_restriction_page_in_the_Knowledge_base_portal.gif)

---

### Basic style

#### Image

1. Click **Image**.
2. Click **Change** and choose:
   * **Default images**: Predefined options
   * **Image**: URL or file upload
3. Set alignment.

#### Heading

1. Click **Heading**.
2. Enter text.
3. Select color.

Default: "Sorry!"

#### Paragraph

1. Click **Paragraph**.
2. Enter description.
3. Select color.

Default: "Your IP address {{template:IPAddress}} is restricted from accessing this article or page."

---

### Custom style

1. Select **Custom style**.
2. Switch between **HTML** and **CSS** sections.
3. Update code.
4. Toggle **Preview**.
5. Click **Save** and **Publish**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Adding_Custom_CSS&JS_in_the_IP_restriction_page.png)## Follow articles and categories

**Plans supporting readers to follow articles and categories**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

The **Follow articles and categories** feature in Document360 allows users to receive notifications about new content and updates. Followers get email alerts when articles are published or modified.

> **NOTE**
>
> This feature works only for **Private** and **Mixed** projects in **KB site 2.0** (projects created after June 10th).

---

## Enabling the 'Show Follow button' in KB Portal

1. Go to **Settings** () > **Knowledge base site** > **Article settings & SEO**.
2. In the **Article header** section, toggle **Show Follow button** on.

![Reader notification](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Enabling_Reader_Notification.png)

> **NOTE**
>
> The **Show Follow button** toggle is enabled by default for new Private and Mixed projects.

---

## Using Follow articles and categories in KB Site

1. Go to the desired category and click **More (•••)**.
2. Click **Follow category**.

   A "Notification turned on" message appears.
3. To follow an article, navigate to it and click **Follow**.

![Reader notification](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-follow_and_Follow_category.png)

You'll receive email notifications when:

* A new version of an article or page category is published
* Any newly published article, page category, or replicated article is published
* An article or page category is republished
* A published article is unhidden or recovered from the recycle bin
* The next version of an article is published via Zapier and Crowdin integration
* The next version of an article is published via API endpoint

> **NOTE**
>
> * When following a category, you'll get email notifications within **30 minutes** for updates to that category, including all sub-categories (up to level six) and associated articles.
* In mixed projects, clicking **Follow category** redirects you to the login page if you're not logged in.

Email notifications are NOT sent when:

* Articles or categories are deleted
* Articles or categories are hidden
* The next version of an article is hidden
* An article is reordered or moved to another category
* The reader doesn't have view access to the article/category

> **NOTE**
>
> Readers are redirected to the respective article or login page from email notifications.

---

### FAQs

#### How do readers configure their email domain for notifications?

Notifications come from the domain set in **Settings** () > **Knowledge base portal** > **Notifications** > **Email domain**. If not configured, emails default to **support@document360.com**.

#### How do I customize the 'Follow' button?

Change the **Follow** variable name in **Settings** () > **Localization & Workspace** > **Localization variables** > **Article Header**. Enter the desired name in the **Follow** field and click **Save**.

#### How do I unfollow a category?

1. Go to the desired category and click **More (•••)**.
2. Click **Unfollow**. A **Notification turned off** message appears.

#### How do I unsubscribe from Follow notifications?

Click **Unsubscribe** in the email. If not logged in, you'll be redirected to the login page. The article or category will be automatically unfollowed.

#### Is the 'Follow Article' feature available for JWT users?

No. The "Follow Article" feature doesn't work with JWT authentication.

<a id="search-in-knowledge-base-site"></a>

## Search in Knowledge base site

**Plans supporting Search in Knowledge base site**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Your Document360 knowledge base includes a fast search bar above articles. Results are filtered by relevance and show article/category names, content previews, and breadcrumbs. **Advanced search** lets you filter results. You can search across all workspaces and languages simultaneously. **Search attachments** finds content inside PDF files.

---

## Search attributes

Search results are based on:

* Article and category titles
* Tags
* Article and category slugs
* Breadcrumbs
* Article content

> **NOTE**
>
> **Search priority:** Article title > Tags > Slugs > Breadcrumbs > Content

---

## Advanced search

Advanced search filters results with options for combined searches across workspaces and languages.

**Example:** Searching for `login` across multiple workspaces:

1. Enter `login` in the search bar.
2. Click **More article filters**.
3. Apply filters: Workspace, Language, Tags, Contributors, Date, Categories.

### Enabling advanced search

1. Go to **Settings** () > **Knowledge base site** > **Article settings & SEO**.
2. In the Search settings section, toggle **Enable advanced search** on.
3. Select **Include all workspaces in site searches** to make "All workspaces" the default search filter.

> **NOTE**
>
> If **Enable advanced search** is off, filter options won't appear.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_New_Screenshot-Enabling_Advanced_Search_in_the_knowledge_base_portal.png)

### Accessing advanced search

1. Enter a keyword in the search bar.
2. Click **More article filters**.
3. Use available filters:

| Filter | Description |
| --- | --- |
| **Workspace** | * **Current workspace**: Search within current workspace * **All workspaces**: Search across all workspaces * **Specific**: Limit search to selected workspaces |
| **Language** | * **Current language**: Search in active language * **All languages**: Search across all languages * **Specific**: Focus search on selected languages |
| **Tags** | Narrow results to articles with selected tags |
| **Contributor** | Filter by contributors from dropdown |
| **Date** | Filter by date range: Last 7/30/90 days or Custom range |
| **Categories** | Refine results to articles in selected categories |

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Accessing_advanced_search_in_KB_site.gif)

---

## Search attachments

Search attachments finds content within PDF files. When searching, four filter tabs appear:

* **Categories**: Results within categories
* **Articles**: Results within articles
* **API Docs**: Results within API documentation
* **Files**: Results within PDF attachments

**Example**: If "SharePoint" yields no article results, switch to the Files tab to find relevant PDF content.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_new_Screenshot-Search_attacment_.png)

### Enabling attachment tab in search

1. Go to **Settings** () > **Knowledge base site** > **Article settings & SEO** > **Article settings**.
2. Expand **Search settings** and toggle **Show attachments tab in search** on.

> **NOTE**
>
> * If **Show article files** is off, **Show attachments tab in search** becomes inaccessible. Enable **Show article files** first.
* When disabled, search only covers article/page elements: title, slug, tags, content.

---

## No search result feedback

When a search returns no results, either a blank page appears or a feedback form shows up if enabled. This form lets readers describe what they were looking for. Feedback can be reviewed in [Search analytics](/help/docs/analytics-search) to improve content.

### Enabling no search result feedback

1. Go to **Settings** () > **Knowledge base site** > **Article settings & SEO** > **Article settings**.
2. Expand **Search settings** and toggle **No search result feedback** on.

> **NOTE**
>
> The feedback form appears on both the Knowledge base site and widget.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Enabling_no_search_result_feedback.png)

**Knowledge base site view**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-No_search_feedback_KB_site.png)

---

## Search filters

The **Filter** option left of the search bar narrows results:

* **Search category titles**: Shows categories and articles containing the keyword
* **Search attachments**: Shows files containing the keyword
* **Workspace**: 
  + Current Workspace: Searches active workspace
  + All Workspaces: Includes all workspaces and API documentation
  + Specific: Select particular workspaces
* **Language**:
  + Current Language: Searches active language
  + All Languages: Includes all supported languages
  + Specific: Select particular languages

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Search.png)

---

## Search operator support

Search operators improve query precision:

* **Double Quotes (`""`)**: Search exact phrases. Words inside quotes must appear in that order.
* **Minus Sign (`-`)**: Exclude words. Place minus directly before word (no space) to exclude it.

Examples:

* `search -recipe` finds records with `search` but not `recipe`
* `search-recipe` finds records with both words (no exclusion)
* `-recipe pasta` finds records with `pasta` but not `recipe`
* `"-recipe"` finds records literally containing `"-recipe"`

---

## FAQs

#### What is Advanced search?

Advanced search lets you search across all workspaces and languages simultaneously using filters.

#### How do I hide the search bar on the Home page?

1. Go to **Settings** () > **Knowledge base site** > **Customize site**
2. Select **Customize site**
3. Choose **Header & Footer** > **Home**
4. Click **Hero section** > **Search**
5. Click the eye icon to hide the search bar

#### How do I exclude an article from search?

Read [Excluding articles from search engines](https://docs.document360.com/docs/excluding-articles-from-searches).

Hidden articles don't appear in the knowledge base site but can be found in the Knowledge base portal.

> **NOTE**
>
> Categories and page categories can also be hidden.

#### Will search include API documentation?

By default, search uses **Current workspace** filter. Select **All workspaces** to include API documentation.

For Document360 1.0:
1. Go to **Settings** () > **Knowledge base site** > **Article settings & SEO** > **Article settings**
2. Expand **Search settings**
3. Select **Include all workspaces in site searches**

#### How does search bar behave with RTL languages?

When RTL language (Hebrew, Arabic) is selected:
* Text aligns right
* Input direction is right-to-left

Multiple languages:
* **All RTL**: Maintains right-to-left input and alignment
* **Mixed RTL/LTR**: Behavior depends on default language

<a id="liking-or-disliking-an-article"></a>

## Liking or disliking an article

**Plans supporting article like or dislike feature**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Users can like or dislike articles in the Document360 Knowledge base site. This feedback helps improve content quality. Users can change their feedback by clicking the opposite button.

> **NOTE**
>
> Undo feature works only in KB Site 2.0 projects. Read about [KB site 2.0 Migration](/help/docs/kb-site-20-migration).

---

## Liking or Disliking an article

To like an article:
1. Navigate to the article
2. Click the **like** icon at the end
3. Optionally enter feedback
4. Select **Notify me about updates** and enter email if desired
5. Click **Submit**

To dislike an article:
1. Click the **dislike** icon
2. Select feedback option or click **Others** for custom feedback
3. Select **Notify me about updates** and enter email if desired
4. Click **Submit**

To undo:
1. Click the **like** or **dislike** icon again

> **NOTE**
>
> * Dislike feedback requires a comment
* Works in both Knowledge base site and widget
* In Public sites, undo works within 30 days unless browser cache is cleared

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-liking_and_disliking_an_Article.gif)

---

### FAQs

**What happens when I undo a dislike after submitting feedback?**

In Feedback manager:
* Open feedback gets deleted
* Assigned feedback gets marked as **Removed**

**Will undoing a dislike appear in Analytics?**

No. Undo cancels the action entirely.

**What happens if I select "Notify me about updates"?**

Team members can respond to your feedback in the portal, and you'll receive email notifications.

**Can I provide multiple likes or dislikes?**

No, but you can change your feedback by clicking the opposite button. Previous comments remain associated with the new feedback type.

<a id="smart-bar"></a>

## Smart bars

**Plans supporting Smart bars in knowledge base site**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Smart bars display customizable banners across your Knowledge base site. They can show information, announcements, or messages based on conditions like user location, browser type, or language settings.

---

## Smart bar overview

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_New_Screenshot-Overview_of_Smart_bars.png)

1. **Select language**: Shows global language and project languages with Smart bar counts
2. **Status**: Indicates if Smart bar is active
3. **Details**: Shows name, position, and preview option
4. **Show rules**: Lists conditions for display
5. **Hide rules**: Lists conditions for hiding
6. **Edit**: Modify Smart bar
7. **Delete**: Remove Smart bar
8. **Filters**: Sort by name, location, rules
9. **New smart bar**: Create new Smart bar

---

## Creating a new Smart bar

1. Go to **Settings** () > **Knowledge base site** > **Smart bars**
2. Click **New smart bar**
3. Enter name
4. Set status (on by default)

#### Configuring content

5. Expand **Content** section
6. Use **Global** toggle for all languages or specific ones
   * **Global On**: Appears across all pages and languages
   * **Global Off**: Select specific languages
7. Add content using formatting tools

#### Customizing Design and location

8. Expand **Design and location**
9. Select position:
   * **Site top**
   * **Site bottom**
   * **Article top**
   * **Article bottom**

10. Choose color theme:
    * **Light theme**: Grey background, black text
    * **Dark theme**: Black background, white text
    * **Custom theme**: Set custom colors

**Advanced display conditions**

11. Configure visibility rules:

| **Condition** | **Description** | **Example** |
| --- | --- | --- |
| **URL** | Specific URLs to include/exclude | Promotional banner on product pages |
| **Query strings** | Use parameters with operators | Discount code when campaign string present |
| **IP address** | Target specific IPs or ranges | Internal updates for office network |
| **Browser** | Based on user's browser | Compatibility warnings for old browsers |
| **Device** | Desktop, mobile, or tablet | Mobile app download banner |
| **Project** | Specific projects, categories, tags | New feature announcements |
| **Language** | Only if Global is on | Localized welcome messages |

12. Select **AND**/**OR** logic for multiple rules
13. Click **Add**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Adding_Smart_bar.gif)

---

### FAQs

#### How do I edit a Smart bar?

1. Go to **Settings** () > **Knowledge base site** > **Smart bars**
2. Hover over Smart bar and click **Edit**
3. Modify content
4. Click **Update**

#### How do I delete a Smart bar?

1. Go to **Settings** () > **Knowledge base site** > **Smart bars**
2. Hover over Smart bar and click **Delete**

<a id="cookie-consent"></a>

## Cookie consent

**Plans supporting cookie consent in knowledge base site**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Document360 lets you add cookie consent bars or popups for readers.

---

## Adding cookie consent

1. Go to **Settings** () > **Knowledge base site** > **Cookie consent**

> **NOTE**
>
> Toggle **Enable cookie consent** on and click **Save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Cookie_consent_Overview_page.png)

### Select language

2. Set message for **All languages** or specific language

> **NOTE**
>
> * Message can be localized and styled
* **All languages** shows across all languages
* Unspecified languages show the **All languages** message

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot_Selecting_languages_for_Cookie_Consent.png)

### Content

3. Add custom message using formatting tools
4. Click **Restore default message** to reset

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screnshot-Content_part_in_the_cookie_consent.png)

### Theme and position

5. Select **Bar** or **Popup**
6. Set position:
   * **Bar**: Top or Bottom
   * **Popup**: Various positions
7. Choose CTA type: Text, Button, or Icon
8. Enter CTA text
9. Select color theme:
   * **Light**: White background, black text
   * **Dark**: Black background, white text
   * **Custom**: Set custom colors
10. Click **Preview**
11. Toggle **Enable cookie consent** on
12. Click **Save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Them_and_position.png)

---

### FAQs

**What is cookie consent?**

Users agreeing to website cookie usage for analytics, personalization, or advertising.

**Can I customize the message?**

Yes, using text formatting and hyperlinks.

**Can I set multiple languages?**

Yes, specific languages or all languages.

**How do I control cookie settings?**

Document360 cookies are essential and cannot be disabled. For optional cookies, use a dedicated cookie management platform.

<a id="accessing-the-ticket-deflectors"></a>

## Accessing ticket deflectors in portal

**Plans supporting ticket deflector**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Ticket deflectors reduce support tickets by helping users resolve queries independently.

---

## Ticket deflectors overview

Go to **Settings** () > **Knowledge base site** > **Ticket deflectors**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Overview_of_ticket_deflector.png)

1. **Title**: Ticket deflector title
2. **Status**: Online/offline toggle
3. **Last updated by**: Team member who last modified
4. **Last updated**: Modification date
5. **New ticket deflector**: Create new deflector
6. **Integrate your Helpdesk**: Configure Freshdesk/Zendesk

Hover options:
7. **Copy**: Generate link (active deflectors only)
8. **Clone**: Duplicate deflector
9. **Preview**: View in knowledge base
10. **Edit**: Modify settings
11. **Delete**: Remove deflector

> **NOTE**
>
> * Set to offline before deleting
* Only configurable for main workspace and its languages

---

## Helpdesk configuration

Integrate with **Freshdesk** or **Zendesk** for direct ticket creation.

1. Go to **Settings** () > **Knowledge base site** > **Ticket deflectors**
2. Click **Integrate your Helpdesk**
3. Choose platform

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Helpdesk_configuration_panel.png)

**Freshdesk Integration**
1. Enter API key and domain URL
2. Click **Validate & save**

> **NOTE**
>
> See [Freshdesk help article](https://support.freshdesk.com/en/support/solutions/articles/215517-how-to-find-your-api-key) for API key details

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Freshdesk_configuration_panel.png)

**Zendesk Integration**
1. Enter API key, domain URL, and agent email
2. Click **Validate & save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Zendesk_configuration_panel.png)

---

## Adding Ticket deflectors to Header/Footer

#### Header navigation

1. Go to **Settings** () > **Knowledge base site** > **Customize site**
2. Click **Customize site**
3. Select **Site header & footer**
4. Expand **Header** > **Header navigation**
5. Click **Add new item**
6. Select **Ticket deflector** type
7. Enter title and select deflector
8. Check **Open link in new tab**
9. Click **Add**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Adding_Ticket_deflector_in_Header_navigation.gif)

#### Header secondary navigation

1. Go to **Settings** () > **Knowledge base site** > **Customize site**
2. Click **Customize site**
3. Select **Site header & footer**
4. Expand **Header** > **Secondary navigation**
5. Click **Add new item**
6. Select **Ticket deflector** type
7. Enter title
8. Paste deflector link
9. Check **Open link in new tab**
10. Click **Add**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Adding_Ticket_deflector_in_Header_secondary_navigation.gif)

#### Footer navigation

1. Go to **Settings** () > **Knowledge base site** > **Customize site**
2. Click **Customize site**
3. Select **Site header & footer**
4. Click **Footer**
5. Choose design: **Basic footer** or **Custom footer**

**Basic footer**
1. Click **Add new link**
2. Enter title and paste deflector link
3. Check **Open link in new tab**
4. Click **Add**

**Custom footer**
1. Paste deflector link in code
2. Click **Save** > **Preview**
3. Click **Publish**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Adding_Ticket_deflector_in_footer_navigation.gif)

### Using form link

Add ticket deflectors to:
* Articles or category pages
* Deprecation messages
* Smart bars
* Cookie consent notifications
* Snippets and variables
* Knowledge base home page
* Knowledge base assistant

---

### FAQs

#### How do I copy the ticket deflector link?

1. Go to **Settings** () > **Knowledge base site** > **Ticket deflectors**
2. Click **Copy** next to deflector

#### What does Clone do?

Duplicates existing deflector with all settings and content.

#### Can I preview before publishing?

Click **Preview in Knowledge base**.

#### How do I delete a ticket deflector?

1. Go to **Settings** () > **Knowledge base site** > **Ticket deflectors**
2. Set status to offline
3. Click **Delete**

<a id="adding-a-new-ticket-deflector"></a>

## Adding a new ticket deflector

**Plans supporting ticket deflector**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Ticket deflectors help users resolve queries independently before contacting support.

> **NOTE**
>
> Business and Enterprise plans support up to 10 ticket deflectors.

---

## Creating a new Ticket deflector

1. Go to **Settings** () > **Knowledge base site** > **Ticket deflectors**
2. Click **New ticket deflector**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Creating_a_new_ticket_deflector.png)

### Step 1: Title, Slug, and Description

Default title: "**How can we help you?**"

1. Edit title (150 character limit)
2. Edit slug (150 character limit, auto-generated)

> **NOTE**
>
> Changing URL breaks existing references

3. Add description
4. Toggle **Online** for visibility

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Adding_Ticket_deflector_step1.png)

### Step 2: Context questions

Context questions understand user issues and guide resolution.

> **NOTE**
>
> No character limit for context questions

1. Click **Questions** (two default questions)
2. For each question:
   a. Enter text
   b. Toggle **Enable search** to require knowledge base search
   c. Check **Make search optional** to allow skipping
   d. Choose next action from dropdown
   e. Delete unwanted questions
   f. Click **Add questions**
   g. Reorder questions

> **NOTE**
>
> * At least one qualifying question required
* No limit on question count

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Context_question_step2.png)

### Step 3: Suggestions

Suggestions provide navigation based on user responses.

> **NOTE**
>
> Suggestions are optional

#### Creating block steps

1. In **Suggestions**, click **Add**
2. Choose type:
   * **Additional question**
   * **Answer**
   * **Answer from your knowledge base**

**a. Additional question**
1. Enter title
2. Enter question
3. Choose next action
4. Delete unwanted questions
5. Add more questions
6. Reorder questions

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Creating_block_steps_Additional_question.png)

**b. Answer**
Enter title and provide text answer with formatting options.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Creating_block_steps_Answer.png)

**c. Answer from your knowledge base**
1. Enter title
2. Select workspace
3. Search and add article

> **NOTE**
>
> Only one article can be linked per step

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_ScreenGIF-Answer_from_your_Knowledge_base.gif)

---

### Step 4: Help request

**Contact form**

Configure form fields:
* **Email**: Mandatory
* **First Name**: Mandatory
* **Last Name**: Optional mandatory
* **Telephone**: Optional mandatory
* **Description**: Mandatory
* **Form submission text**: Customizable
* **Allow attachments**: Up to 5 files, 2 MB each
* **Enable captcha**: Protects against spam
* **After submission message**: Mandatory, 250 character limit

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Help_Request_Contact_form.png)

### Step 5: Ticket submission settings

**Ticket submission email notification**

1. **Email subject**: Up to 100 characters
2. **Send notification email to**: Select team accounts
3. **These emails**: Add additional recipients (no limit)

> **NOTE**
>
> Map forms to specific emails:
* Sales form → sales@yourcompany.com
* Operations form → tech@yourcompany.com

**Connect a helpdesk**

1. Expand **Create helpdesk ticket**
2. Toggle **Create helpdesk ticket on form submission** on
3. Click **Connect a helpdesk**
4. Select platform (Freshdesk/Zendesk)
5. Enter credentials
6. Click **Validate & save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-connecting_a_helpdesk.png)

---

### Localizing ticket deflector text

1. Go to **Settings** () > **Localization & Workspaces** > **Localization variables**
2. Select language
3. Expand **Ticket deflector** section
4. Update text
5. Click **Save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Localizing_the_ticket_deflector.png)

<a id="integrations-getting-started"></a>

## Integrations in Document360

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Document360 supports over 25 third-party integrations in categories:
* **Analytics**
* **Chat**
* **Comments**
* **Marketing automation**

## Adding a new integration

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. View existing integrations in **Installed integrations**
3. Scroll to see more apps
4. Find desired app and click **Add**
5. Choose **Basic** or **Custom configuration**
6. Enter required information
7. Click **Add**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Integrations%20-%20Overview%20page.png)

> **NOTE**
>
> Required information varies by integration

Click **Learn more** for detailed setup instructions.

---

## Integration controls

Manage integrations from **Settings** () > **Knowledge base site** > **Integrations**:

* **Status** – Green (active) or Gray (inactive)
* **Type** – Integration name and icon
* **Description** – User-defined description
* **Updated on** – Last modification date
* **Users** – Team members who modified integration

### Available integrations

| Analytics | Chat | Commenting | Marketing automation |
| --- | --- | --- | --- |
| * [Amplitude](/help/docs/amplitude) * [FullStory](/help/docs/fullstory) * [GoSquared](/help/docs/gosquared) * [Google Analytics](/help/docs/google-analytics-integration) * [Google Tag Manager](/help/docs/google-tag-manager) * [Heap](/help/docs/heap) * [Hotjar](/help/docs/hotjar) * [Mixpanel](/help/docs/mixpanel) * [Segment](/help/docs/segment-integration) | * [Belco](/help/docs/belco) * [Chatra](/help/docs/chatra) * [Crisp](/help/docs/crisp) * [Doorbell](/help/docs/door-bell) * [Freshchat](/help/docs/freshchat) * [Gorgias](/help/docs/gorgias) * Intercom * [Kommunicate](/help/docs/kommunicate) * [LiveChat](/help/docs/livechat) * [Olark](/help/docs/olark) * [Sunshine Conversations](/help/docs/sunshine) | * [Comment](/help/docs/commento) * [Disqus](/help/docs/disqus) | * [Freshmarketer](/help/docs/freshmarketer) * [VWO](/help/docs/vwo) * [Zoho PageSense](/help/docs/zoho-page-sense) |

---

## Custom HTML

Embed third-party widgets using Custom HTML integration.

### Adding Custom HTML code

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Under **Custom HTML**, click **Add**
3. Choose insertion point:
   * **Header**
   * **Begin Body**
   * **End Body**
4. Paste code snippet
5. Click **Add**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Custom%20HTML%20-%20Integrations.png)

---

## Editing or deleting an integration

#### Editing:

1. Hover over integration and click **Edit**
2. Update Status, Description, or App ID/URL
3. Click **Update**

#### Deleting:

1. Hover over integration and click **Delete**
2. Confirm deletion

---

### FAQs

#### What if my integration isn't working?

Verify App ID and URL. Check internet connection. Click **Learn more** for app-specific instructions.

#### Best practices for managing integrations?

Review active integrations periodically. Keep integrations updated.

#### Best practice for analytics scripts?

Use **Custom HTML** option in Integrations section. Add script and save changes.

<a id="advanced-insertion-rules-in-integration"></a>

## Code inclusion and exclusion conditions

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure **Code inclusion/exclusion conditions** to control where integrated code runs.

For Google Analytics, set conditions based on:
* **IP Address** – Specific IPs or ranges
* **Workspace** – Selected workspaces
* **Language** – Specific languages

Use **AND/OR** logic for multiple conditions.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Code%20inclusion%20in%20Integrations%20-%201.png)

### IP address condition

1. In **Upgrade Integration**, select **IP Address**
2. Choose **Show** or **Hide**
3. Select **Exact** or **Range**
4. Specify IP address(es)

### Workspace condition

1. Select **Workspace** condition type
2. Choose **Show** or **Hide**
3. Specify workspaces

### Language condition

1. Select **Language** condition type
2. Choose **Show** or **Hide**
3. Specify language(s)

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Code%20inclusion%20in%20Integrations%20-%202.png)

<a id="livechat"></a>

## LiveChat

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

LiveChat provides instant customer service using AI. It enables real-time communication and handles multiple chats simultaneously.

---

## Integrating Document360 and LiveChat

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Select **LiveChat** and click **Add**
3. Add Description and enter LiveChat ID

> **NOTE**
>
> LiveChat ID comes from LiveChat application

4. Use **Code inclusion/exclusion conditions** if needed
5. Click **Add**

![2_ScreenGIF-Document360_and_Livechat](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Document360_and_Livechat.gif)

---

## Obtaining the LiveChat ID

#### For existing LiveChat customers

1. Access LiveChat dashboard and click **Install**
2. In **Install chat widget manually**, find ID after "*window.lc.license=*"

![3_Screenshot-getting_Live_chat_ID_Existing_customers](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-getting_Live_chat_ID_Existing_customers.png)

#### For new LiveChat users

1. Copy LiveChat ID during account setup
2. Complete integration in Document360
3. Open LiveChat interface to view chats

> **NOTE**
>
> Deploy bots to handle regular queries in chat box

<a id="olark"></a>

## Olark

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Olark combines live chat with customer data collection.

**Key Features:**
* **Visitor Cobrowsing**: Navigate user screens in real-time
* **Visitor Geolocation**: Location insights
* **Visitor Insights**: Browsing behavior and history
* **Transcripts**: Complete chat records

---

## Integrating Document360 and Olark

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Select **Olark** and click **Add**
3. Add Description and enter Olark ID

> **NOTE**
>
> Olark ID comes from Olark application

4. Use **Code inclusion/exclusion conditions** if needed
5. Click **Add**

![2_ScreenGIF-Integrating_Document360_Olark](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Integrating_Document360_Olark.gif)

---

## Obtaining the Olark ID

1. Sign in to Olark account
2. Go to **Settings** > **Channels**
3. In **Installation Code**, click **Copy to Clipboard**
4. Find `olark.identify()` function
5. Copy thirteen-digit ID (including dashes)

![3_Screenshot-Getting_Olark_ID](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Getting_Olark_ID.png)

> **NOTE**
>
> Use Olark for lightweight, customizable chat with automation rules

<a id="freshchat"></a>

## Freshchat

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Freshchat is messaging software for sales and customer engagement teams. It supports AI-powered chatbots and integrates with WhatsApp, Apple Business Chat, Facebook Messenger, and LINE.

**Key Features:**
* **One inbox**: Consolidate messages from different platforms
* **Self-Service with AI Bots**: Reduce response times

![002_Screenshot_Freshchat_Integration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/002_Screenshot_Freshchat_Integration.png)

---

## Integrating Document360 and Freshchat

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Select **Freshchat** and click **Add**
3. Add Description and enter Freshchat Token

> **NOTE**
>
> Freshchat Token comes from Freshchat application

4. Use **Code inclusion/exclusion conditions** if needed
5. Click **Add**

![1_ScreenGIF-Integrating_Document360_and_Freshchat](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Integrating_Document360_and_Freshchat.gif)

---

### Obtaining the Freshchat Token

1. Log in to Freshchat dashboard
2. Go to **Settings** > **Admin settings**
3. Select **Configuration and Workflows**
4. Scroll to **Workflows** > **Web Chat Settings** > **Integration Settings**
5. Under **Web messenger**, copy token

![2_ScreenGIF-Getting_token_from_freshdesk_for_Document360](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Getting_token_from_freshdesk_for_Document360.gif)

<a id="crisp"></a>

## Crisp

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Crisp centralizes customer conversations for instant online communication.

**Key features:**
* **Cost Efficiency**: One agent handles multiple conversations
* **Predefined Answers**: Automated responses to common queries
* **Enhanced Communication Tools**: Images, buttons, GIFs in messages

---

## Integrating Document360 and Crisp

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Select **Crisp** and click **Add**
3. Add Description and enter Crisp website ID

> **NOTE**
>
> Crisp website ID comes from Crisp application

4. Use **Code inclusion/exclusion conditions** if needed
5. Click **Add**

![2_ScreenGIF-Integrate_Document360_and_crisp](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Integrate_Document360_and_crisp.gif)

---

### Getting the Crisp Website ID

#### For existing Crisp customers:

1. Open Crisp dashboard
2. Go to **Settings** > **Website Settings**
3. Copy Website ID from **Setup Instructions**

![02_Screenshot_Crisp_Integration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/02_Screenshot_Crisp_Integration.png)

#### For new Crisp customers:

1. Get Website ID during account installation
2. Complete integration in Document360
3. Open Crisp interface to respond to chats

> **NOTE**
>
> Use Crisp for chatbots with email campaigns and mobile apps

<a id="chatra"></a>

## Chatra

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Chatra enables real-time interaction between customers and representatives. One agent handles multiple conversations simultaneously.

![2_Screenshot_Chatra_Integrations](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot_Chatra_Integrations.png)

---

## Integrating Document360 and Chatra

1. Go to **Settings** () > **Knowledge base site** > **Integrations**
2. Select **Chatra** and click **Add**
3. Add Description and enter Chatra ID

> **NOTE**
>
> Chatra ID comes from Chatra application

4. Use **Code inclusion/exclusion conditions** if needed
5. Click **Add**

![2_Screenshot-integrating_Document360_and_Chatra](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-integrating_Document360_and_Chatra.gif)

---

### Getting the Chatra ID

#### For existing Chatra customers:

1. Log in to Chatra account
2. Go to **Settings** > **Chat widget**
3. Find `w.Chatra.ID` in Chat Widget window

![3_Screenshot-Chatra_ID_chat_widget_existing_user](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Chatra_ID_chat_widget_existing_user.png)

#### For new Chatra users:

1. Sign up and verify email
2. Receive Chatra ID in confirmation email

![4_Screenshot-Chatra_ID_chat_widget_new_user_customer](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Chatra_ID_chat_widget_new_user_customer.png)

> **NOTE**
>
> Chatra enables real-time conversations, targeted chats, and visitor tracking. See [Chatra help](https://chatra.com/help/) for more features.

<a id="door-bell"></a>

## Doorbell

**Plans supporting third party tool integrations**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Doorbell collects, manages, and analyzes customer feedback. Users can attach screenshots for context.

![003_Screenshot_Doorbell_Integration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/003_Screenshot_Doorbell_Integration.png)

---## Document360 Extensions - Getting started

**Plans supporting Extensions**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Document360 extensions integrate your knowledge base with third-party platforms for more efficient workflows. These extensions allow you to access, manage, and share knowledge base content directly from other platforms.

## Accessing the Extensions page

1. Navigate to **Settings** () > **Knowledge base portal** > **Extensions**.
2. Filter extensions by category:
   * All extensions
   * Helpdesk
   * Team collaboration
   * Code repositories
   * Translation & browser
3. Click **Connect** on the intended extension tile.

**Available extensions:**

**Helpdesk**
* [Freshdesk](/help/docs/freshdesk)
* [Zendesk](/help/docs/zendesk-1)
* [Intercom](/help/docs/intercom-integration)
* [Salesforce](https://docs.document360.com/docs/salesforce-integration)

**Team collaboration**
* [Slack](/help/docs/slack)
* [Microsoft Teams](/help/docs/microsoft-teams)
* [Drift](/help/docs/drift)
* [Zapier](https://docs.document360.com/docs/zapier-integration)
* [Make](/help/docs/make-1)

**Code repositories**
* [GitHub](https://portal.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/document/help/view/7678f7e8-9fd8-48a1-ba64-c0d7ed5ffb45)

**Translation and browser**
* [Chrome](/help/docs/chrome-extension)
* [Crowdin](/help/docs/crowdin)
* [Phrase](/help/docs/phrase)

<a id="freshdesk"></a>

## Freshdesk

**Plans supporting Freshdesk extensions**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Integrate Document360 knowledge base with Freshdesk. Support agents can access knowledge base articles and create new articles directly from Freshdesk without switching tabs.

---

## Setup

1. In Document360, go to **Settings** () > **Knowledge base portal** > **Extensions**.
2. Click **Connect** on the Freshdesk extension.
3. Copy the generated API token.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Freshdesk_api_token.png)

4. In Freshdesk, go to **Admin** > **Support Operations** > **Apps**.
5. Search for Document360 in the App Marketplace.
6. Paste the API token and click **Install**.

You can add multiple API keys for different Document360 knowledge bases.

---

### Multi-product support

For companies with multiple products and separate knowledge bases, Freshdesk offers Multi-Product Support to handle all products from one portal.

Refer to [Freshdesk's Multi-product setup guide](https://support.freshdesk.com/support/solutions/articles/37638-supporting-multiple-products-with-freshdesk) for integrating multiple Document360 knowledge bases.

---

## Features

### Search and share articles

Once connected, access Document360 articles directly from Freshdesk:

1. Click the Document360 icon in the ticket response window
2. Select workspace and language
3. Search for articles
4. Use **+Link** to insert article hyperlinks or **+Content** to insert full article content

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Freshdesk_link_connect_buttons.png)

**Automated article search:** Freshdesk automatically searches knowledge base articles using ticket titles and displays matches under "Recommended articles."

### Create articles from Freshdesk

Create new knowledge base articles without leaving Freshdesk:

1. Click the Document360 icon
2. Select workspace and language
3. Click **+Create New Article**
4. Use the Markdown editor to write content
5. Add title and select existing category
6. Click **Create**

> NOTE: You cannot create new categories from Freshdesk. Only existing categories are available.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Freshdesk_create_new_article.png)

<a id="freshservice"></a>

## Freshservice

**Plans supporting Freshservice extensions**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Integrate Document360 knowledge base with Freshservice for better IT service management. Support agents can access and share articles during ticket resolution, plus create new articles directly from Freshservice.

---

## Setup

1. In Document360, navigate to **Settings** () > **Knowledge base portal** > **Extensions**.
2. Click **Connect** on the Freshservice extension.
3. Copy the generated API token.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Freshservice_api_token_details.png)

4. In Freshservice, go to **Admin** > **Automated & Productivity** > **Apps**.
5. Search for Document360 in the Apps marketplace.
6. Paste the API token and click **Install**.

You can integrate multiple Document360 knowledge bases by repeating this process with different API keys.## Integrating Confluence Server with Document360

**Plans supporting integration of Zapier extensions with Document360**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Using Document360 as your knowledge base platform, you can connect it with Confluence Server to synchronize content between the two platforms. This eliminates the need to manually transfer articles from Confluence to Document360.

By connecting Document360 and Confluence Server via Zapier, you can automate content flow. To set up the connection, follow these steps:

1. Log into your [Zapier account](https://zapier.com/app/dashboard).
2. From the left navigation menu, click **Create** > **Zaps**.
3. A new Zap will be created with **Trigger** and **Action** fields.

### Connecting Confluence Server and Document360 in Zapier

#### Step 1: Set up the trigger – Confluence Server

1. In the **Trigger** field, select **Confluence Server**.
2. Choose the required **Trigger event** (e.g., New Page, Updated Page).
3. Click the **Account** field. A sign-in window will appear.
4. Enter your Confluence Server credentials and click **Continue**.
5. Select the space, page, or blog you want to monitor.
6. Click **Continue**.

Zapier will test the trigger to confirm it's configured correctly.

#### Step 2: Set up the action – Document360

1. In the **Action** field, select **Document360**.
2. Choose the desired event (e.g., Create Article).
3. Click the **Account** field. A sign-in window will appear.
4. Enter your Document360 credentials and click **Allow**.

To generate an API token in Document360:

5. Navigate to **Settings** () > **Knowledge base portal** > **Extensions** > **Team collaboration**.
6. Click **Connect** on the Zapier extension tile.
7. Click the **Copy** () icon to copy the token.

8. Return to Zapier and paste the API token.
9. Click **Yes, Continue to Document360**.
10. Select the Document360 project you want to connect.
11. Click **Continue**.

#### Step 3: Customize the Zap

Map fields from Confluence Server to Document360:

* **Title** – Choose from available Confluence fields (e.g., Page Title).
* **Content** – Usually mapped to Page Content, but can be adjusted.
* **Version** – Select the workspace in your Document360 project.
* **Language** – Choose the article language.
* **Category** – Select the category for the new article.
* **Publish** – Set to **True** to publish immediately, **False** to save as draft.

Click **Continue** once all fields are mapped.

#### Step 4: Test and publish the Zap

1. Click **Test step**.
2. If successful, you’ll see the message: *Test Article sent! Check your Document360 account to view it.*
3. Click **Publish**.
4. You’ll get a confirmation: **Your Zap is on**. Click **Manage your Zap** to view it in the Zap overview page.

---

## Zap overview

### Create Document360 articles from new or updated Confluence pages

You can view and edit Zap information from the Zap overview page.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenShot-Confluence.png)

### Deleting a Zap

To delete a Zap:

1. Go to the **Zapier dashboard**. The overview page lists all existing Zaps.
2. Click the arrow (**>**) next to the Zap you want to delete.
3. Click **Turn off and delete Zap**.

The selected Zap will be deleted.## Integrating Jira with Document360

Using Document360 as your knowledge base platform and Jira for issue tracking, you may need to automatically create knowledge base articles from new Jira issues. This ensures that relevant information about issues is documented and easily accessible.

To establish a connection between Jira and Document360:

1. Ensure that you have logged into your [Make account](https://www.make.com/).
2. Click **Sign in** at the top to access the Make dashboard.

![1_Screenshot-Make_signin_page](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733464343369.png)

### Step 1: Create a new scenario

1. Click **Create a new scenario** at the top right.
2. Click the add (**+**) icon to view available applications.
3. In the Search field, type **Jira**.
4. Select **Jira** and choose the desired trigger event.

   For example, select **Watch Issues** to monitor new issues.
5. Click **Create a connection** and enter a connection name.
6. Click **Save**.
7. Allow Jira to access your Make account by clicking **Allow**.
8. Click **OK**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Jira_Make.gif)

### Step 2: Configure Jira trigger

Set up your Jira account connection for the new scenario:

![2_Screenshot-Jira_issue_details](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733466870362.png)

1. Select an existing Jira connection or create a new one.
2. From the **Project Key** dropdown, select the project to monitor.
3. Configure optional filters:
   * **Issue Type**: Filter by specific issue types
   * **Status**: Filter by issue status
   * **Priority**: Filter by priority level
4. In the **Limit** field, specify maximum issues returned per execution cycle.
5. Click **OK**.
6. In the **Choose where to start** popup, select when to begin monitoring issues.
7. Click **OK**.

Your Jira account is now connected to Make.

### Step 3: Connect Document360

After connecting Jira, link your Document360 account:

![3_Screenshot-Jira_add_new_module](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733468868456.png)

1. On the integration page, click **Add another module** (+).
2. In the Search field, enter **Document360**.
3. Select **Document360** and choose the action to perform.

   For example, select **Create an article** to generate draft articles.
4. Select an existing Document360 connection or create a new one:
   1. Click **Create a connection** and enter a connection name.
   2. Enter your API key and click **Save**.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGif-Jira_Make.gif)

To generate the API token from Document360:
1. Navigate to **Settings** () > **Knowledge base portal** > **Extensions** > **Team collaboration**.
2. On the Make extension tile, click **Connect**.
3. Click the **Copy** () icon to copy the token.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Jira_Make.gif)

Back in the Make window:
1. Paste the API token.
2. Click the **Article Title** field and select parameters for your article title.

   For example, select the Issue Summary parameter.
3. Click the **Article Content** field and select parameters for article content.

   For example, select Description, Reporter, and Assignee parameters.
4. From the **Project Category ID** dropdown, select where to create new articles.
5. Click **OK**.

![4_Screenshot-Document360_jira_module](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733472905161.png)

### Step 4: Test the scenario

Before activating, test your scenario:

1. Click **Run once** at the bottom left.
   
   Test details appear at the bottom of the page.
2. Create a new issue in your Jira project.
3. Verify that a new article was created in your Document360 category.

   Check test details or navigate to your Document360 project to confirm.

### Step 5: Schedule the scenario

1. Enable the toggle at the bottom left to schedule executions.

   This runs the scenario every 15 minutes.
2. Click **OK** to save.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenShot-Jira_Make.png)

### Step 6: Activate the scenario

1. Click the **Exit editing** () icon at the top.

   The integration dashboard appears.
2. Turn on the **ON/OFF** toggle near the **Edit** option to activate the scenario.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_ScreenShot-Jira_Make.png)

Once activated, your scenario runs according to the set schedule.

---

Application Programming Interface - A set of rules that allows one software application to communicate with another.## Integrating Jira with Document360

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Jira service desk delivers service experiences for employees and customers. It provides functionalities for service desk management, analytics, request queues, and integration with team collaboration platforms.

---

To integrate Jira with Document360:

1. Log into your [Make account](https://www.make.com/).
2. Click **Sign in** at the top.

   The Make dashboard appears.

![1_Screenshot-Make_signin_page](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733814317319.png)

### Step 1: Create a new scenario

1. Click **Create a new scenario** at the top right.
2. Click the add (**+**) icon. A list of applications appears.
3. In the Search field, type "Jira Cloud Platform".
4. Select **Jira Cloud Platform** and choose your task.

   For example, select **Watch Issues** to trigger on new responses.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Jira_Make.gif)

### Step 2: Connecting Jira

Connect your Jira account to the scenario:

1. Click **Create a webhook** and enter a **Webhook name**.
2. Click **Create a connection** and enter a **Connection name**.
3. Enter the **Service URL**.
4. Enter the **Username** and **API Token**.
5. Click **Save**.
6. From the **Watch Issues** dropdown, select what you want to track.
7. From the **Select a Method** dropdown, choose how to search issues.
8. If needed, select filters in **Filter**, **Expand**, and **Fields**.
9. In the **Limit** field, enter the maximum number of tasks Make returns per execution.
10. Click **OK**.
11. In the **Choose where to start** popup, select when to start watching issues.
12. Click **OK**.

    ![2_Screenshot-Jira_make_popup_window](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1733815745423.png)

    Your Jira project is now connected to Make.

### Step 3: Connecting Document360

After connecting Jira, link your Document360 account:

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenShot-Jira_Make.png)

1. On the Integration Jira page, click **Add another module** (+).
2. In the Search field, enter **Document360**.
3. Select **Document360** and choose your action.

   For example, select **Create an article** to create drafts.
4. In the Document360 window, select your existing connection.

   To create a new connection:
   
   1. Click **Create a connection** and enter a **Connection name**.
   2. Enter your API key and click **Save**.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Jira_Make.gif)

5. Navigate to **Settings** > **Knowledge base portal** > **Extensions** > **Team collaboration**.
6. On the Make extension tile, click **Connect**.
7. Click the **Copy** icon to copy the token.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Asana_Make.gif)
8. Return to Make and paste the API token.
9. Click the **Article Title** field and select parameters for your article title.

   For example, select the Task name parameter.
10. Click the **Article Content** field and select parameters for article content.

    For example, select Assignee Name, Resource Type, and Due On.
11. From the **Project Category ID** dropdown, select where to create the article.
12. Click **OK**.

### Step 4: Test the scenario

Before activating, test your scenario:

1. Click **Run once** at the bottom left.

   Test details appear at the bottom.
2. Create a new task in your Jira project.
3. A new article will appear in your Document360 category.

   Verify with test details or check your Document360 project directly.

### Step 5: Schedule the scenario

1. Enable the toggle at the bottom left to schedule scenarios.

   This runs the scenario immediately when data arrives.
2. Click **OK** to save.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenShot-Jira_Make.png)

### Step 6: Activate the scenario

1. Click **Exit editing** at the top.

   The integration dashboard appears.
2. Turn on the **ON/OFF** toggle near the **Edit** option to activate the scenario.

   ![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_ScreenShot-Jira_Make.png)

Once activated, your scenario runs according to schedule.

---

Application Programming Interface - A set of rules that allows one software application to communicate with another.

<a id="chrome-extension"></a>

## Chrome

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Chrome is a widely used, free cross-platform web browser. The Chrome Web Store offers various extensions.

> Extensions are small software programs that customize browser functionality.

The [Document360 extension](https://chromewebstore.google.com/detail/document360/lifhmbmenhhiolpbbahnjicckcnnophl) is available in the Chrome Web Store.

With the Document360 Chrome Extension and API key, you can access articles and categories from your knowledge base within Chrome anytime.

## Chrome extension: setup

### Adding the Document360 extension in Chrome

1. Open Chrome and navigate to the [Chrome Web Store](https://chromewebstore.google.com/).
2. Search for Document360 extension and click on it.
3. Click **Add to Chrome**.
4. In the popup, click **Add extension**.

![1_Screenvideo-Chrome_Extension_Adding.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenvideo-Chrome_Extension_Adding.gif)

Manage your extension settings:

5. Click More > **Extensions** > **Manage Extensions** to see all extensions.

> NOTE
>
> * You need a Google account to add/remove Chrome extensions.
> * Guest users cannot add Chrome extensions.
> * To use extensions in Incognito, go to **Manage extensions** and enable **Allow in Incognito**.

### API key configuration

1. Click the Document360 icon in the toolbar. A side window appears for the API key.

![5_Screenshot-API_Key.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-API_Key.png)

2. Navigate to your Document360 portal.
3. Go to Settings > **Knowledge base portal** > **Extensions**.
4. In **Chrome extension**, click **Details**.
5. The Chrome details popup shows the **Internal integration token**.
6. Copy the key using the clipboard icon.
7. Paste the key into the Document360 launcher in Chrome and click **Save**.

   Your knowledge base is now integrated and available in Chrome.

## Feature highlights

**Easy launch and customization**

* After integrating with the API key, launch the Document360 assistant in Chrome.
* Click the Document360 icon in the extension toolbar to launch.
* Toggle the assistant to the left or right side. Default is right.

![2_ScreenVideo-Document360_Extension.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenVideo-Document360_Extension%282%29.gif)

**Quick launch label**

* When you close the assistant, find the quick launch label on the right side.
* Click the label to launch the assistant on the same tab.
* Drag the label vertically to position it.
* Remove the label by hovering and clicking the **X** button.

**Page Help**

* This is the default tab when launching the extension.
* See top-searched articles based on previous searches.
* Search articles using keywords. Results update as you type.
* Select an article to view it in reader mode.

Reader view options:

1. **Copy**: Copy entire article content to clipboard.
2. **Open in new tab**: Open article in a new browser tab.
3. **Expand**: Expand reader view (not full screen).

![3_Screenshot-PageHelp.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-PageHelp.png)

**Knowledge base view**

* Click the Document360 launcher and select the **Knowledge base** tab.
* Browse the entire knowledge base structure within the assistant.
* This mirrors your knowledge base's tree-view structure.
* Click articles to view content in reader mode.

## Removing the Document360 extension in Chrome

To remove the extension:

* Visit the Document360 page in Chrome Web Store, click **Remove from Chrome**, then confirm.
* Or right-click the launcher icon, select **Remove from Chrome**, then confirm.

![4_Scrrenvideo-Removing_Doc360.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Scrrenvideo-Removing_Doc360.gif)

---

## FAQ

**What can be accessed through the Document360 Chrome extension?**

Access articles and categories from your Document360 knowledge base directly in Chrome. The extension provides search functionality and quick navigation through your knowledge base structure.

Application Programming Interface - A set of rules that allows one software application to communicate with another.## Restoring from a backup

To restore from a backup:

1. Go to **Settings** > **Knowledge base portal** > **Backup and Restore**.
2. Click the **Restore options** dropdown on the desired backup and select elements to restore:
   * For **Documentation**, **API documentation**, and **Homepage builder**: select checkboxes, then click **Restore**.
   * For **Custom CSS** and **Custom JavaScript**: compare versions, then click **Restore** to use the backup version.
3. Confirm by clicking **Yes**.

The restore runs in the background. A "Backup restored" message appears when complete.

![2_Screenshot-Restoring_a_Backup.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Restoring_a_Backup.png)

---

## Restore options

### 1. Documentation

Restores project documentation to the backup's state.

1. Select specific workspaces, languages, categories, or articles.
2. Enable **Select all** to restore everything.
3. Hover over any item in the **Restore documentation** panel and click **View** to preview content before restoring.

**Example:** To recover a deleted language:

1. Go to **Settings** > **Knowledge base portal** > **Backup and Restore**.
2. Click **Restore** and select **Documentation**.
3. Choose workspace and language, then click **Restore**.

> NOTE
> 
> * Restoring existing items updates them with backup content.
> * Restoring deleted items recreates them.

![3_ScreenGIF-Restore_Documentation.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGIF-Restore_Documentation.gif)

---

### 2. API documentation

Restores API documentation to the backup's state.

1. Select specific workspaces, languages, categories, or articles.
2. Enable **Select all** to restore everything.
3. Hover over items in the **Restore API documentation** panel and click **View** to preview content.
4. Click **Restore**.

![4_Screenshot-Restore_API_Documentation.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Restore_API_Documentation.png)

---

### 3. Homepage builder

Restores all Homepage builder features:
* **Navigations**: Header & Footer
* **Main Pages**: Home, Documentation, Login
* **Error Pages**: 404, Access denied, Unauthorized, IP restrictions

1. Select desired workspaces and languages.
2. Enable **Select all** to restore everything.

**Example:** To recover a deleted language's Home page:

1. Go to **Settings** > **Knowledge base portal** > **Backup and Restore**.
2. Click **Restore** and select **Homepage builder**.
3. Choose workspace and language, then click **Restore**.

![5_Screenshot-Restore_Homepage_Builder.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Restore_Homepage_Builder.png)

---

### 4. Custom CSS

Restores custom CSS to the backup's state.

* Compare backup and current versions (changes highlighted).
* Click **Copy code snippet** next to either version to copy the CSS.

**Example:** To recover overwritten CSS:

1. Go to **Settings** > **Knowledge base portal** > **Backup and Restore**.
2. Click **Restore** and select **Custom CSS**.
3. Compare versions.
4. Click **Restore** to recover the backup version.

![6_Screenshot-Restore_Custom_CSS.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Restore_Custom_CSS.png)

---

### 5. Custom JavaScript

Restores custom JavaScript to the backup's state.

* Compare backup and current versions (changes highlighted).
* Click **Copy code snippet** next to either version to copy the JavaScript.

**Example:** To recover overwritten JavaScript:

1. Go to **Settings** > **Knowledge base portal** > **Backup and Restore**.
2. Click **Restore** and select **Custom JavaScript**.
3. Compare versions.
4. Click **Restore** to recover the backup version.

![7_Screenshot-Custom JavaScript.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Custom%20JavaScript.png)

---

## FAQ

**Are backups created after every project update, or do I need to trigger them manually?**

Backups run automatically daily at 00:00 UTC, not after each update. Create manual backups for important changes.

**Can I perform manual backups at any time?**

Yes.

**How long are backups stored, and can I delete older backups?**

Backups last 90 days before automatic deletion. Manual deletion isn't possible.

**What elements can be restored from a backup?**

Documentation, API documentation, Homepage builder, Custom CSS, and Custom JavaScript.

**Can I restore specific elements from a backup?**

Yes, you can select specific elements to restore.

<a id="notifications"></a>

## Notifications

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Document360 sends project change notifications via email (SMTP), Slack, Microsoft Teams, and webhooks. These are **Notification channels**.

Example: A project manager configures Slack notifications to track team content updates in real-time.

---

## Accessing notification channels

To configure notification channels, go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification channels**.

View active channels, edit or delete as needed. Click **New channel** to add one.

> NOTE
> 
> An email channel (SMTP) is automatically configured and can't be deleted, but you can customize it.

![1_Screenshot-Notification_channel_overview_page.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Notification_channel_overview_page.png)

### Adding notification channels

Supported channels:
* [Webhook notification channel](/help/docs/webhook-notification-channel)
* [Slack notification channel](/help/docs/slack-notification-channel)
* [Microsoft Teams notification channel](/help/docs/microsoft-teams-notification-channel)
* [SMTP notification channel](/help/docs/smtp-email-notification-channel)

<a id="webhook-notification-channel"></a>

## Webhook notification channel

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Webhooks send real-time data from Document360 to other applications when specific events occur.

Example: Notify your Slack workspace instantly when articles update.

---

## Setting up Webhook notification channel

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Click **New channel**.
3. Select **Webhook** and click **Next**.
4. Enter a **Friendly name**.
5. Select **POST** or **PUT** request method.
6. Enter the destination **Webhook URL**.
7. Choose message format from **Request content**.
8. Add headers if needed under **Default headers**.
9. Enter **Authorization key** if required.
10. Click **Save**.

> NOTE
> 
> Read about [Request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header).

![1_ScrenGIF-Setting_up_the_Webhook_notification_Channel.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScrenGIF-Setting_up_the_Webhook_notification_Channel.gif)

After saving, go to [**Notification mapping**](/help/docs/notification-mapping) to configure which events trigger notifications.

<a id="slack-notification-channel"></a>

## Slack notification channel

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Slack integrates with Document360 to send notifications about portal, site, and widget changes to designated channels.

Example: Customer support teams receive real-time alerts for new knowledge base articles.

---

## Setting up Slack notification channel

### Step 1: Create a new app in Slack

1. [Create a Slack account](https://slack.com/intl/en-in/) and workspace if needed.
2. Log in and navigate to your apps.

### Step 2: Get the webhook URL

1. Open [Slack API](https://api.slack.com/apps) and select **Create New App**.
2. Choose your app.
3. Go to **Features** > **Incoming Webhooks** and toggle **ON**.
4. Copy the webhook URL from **Webhook URLs for Your Workspace**.

![4_Screenshot-Slack_webhook_Link.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Slack_webhook_Link.png)

#### Generate new webhook

If no webhooks exist:
1. Click **Add New Webhook to Workspace**.
2. Choose destination channel and click **Allow**.
3. Copy the new webhook URL.

### Step 3: Configure in Document360

1. Go to **Settings** > **Knowledge base portal** > **Notification channels**.
2. Click **New channel**.
3. Select **Slack** and click **Next**.
4. Enter **Friendly name**.
5. Paste the **Webhook URL**.
6. Click **Save**.

![1_ScreenGIF-Slack_notification_channel.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-Slack_notification_channel.gif)

Go to [**Notification mapping**](/help/docs/notification-mapping) to assign specific events to this channel.

<a id="microsoft-teams-notification-channel"></a>

## Microsoft Teams notification channel

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Microsoft Teams receives Document360 notifications directly in channels, keeping teams updated on portal, site, and widget changes.

Example: Teams users get alerts when knowledge base articles publish or update.

---

## Setting up Microsoft Teams notification channel

Required steps:
* [Create Teams channel](/help/docs/microsoft-teams-notification-channel#creating-a-channel-in-microsoft-teams)
* [Get webhook URL](/help/docs/microsoft-teams-notification-channel#get-the-webhook-url)
* [Configure Document360](/help/docs/microsoft-teams-notification-channel#setup-the-configuration-in-document360)

### Step 1: Create Teams channel

1. Open Microsoft Teams.
2. Go to **Teams**, click **More** (⋯) next to your team.
3. Click **Add channel**.
4. Enter name and click **Add**.

![1_Screenshot-Creating_a_channel_in_Microsoft_teams.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Creating_a_channel_in_Microsoft_teams.png)

### Step 2: Get webhook URL

1. In your channel, click **More** (⋯) and select **Manage channel**.
2. Click **Edit** in **Settings**.
3. Search for **Incoming webhook** and click **Add**.
4. Name your webhook connection.
5. Upload image if needed.
6. Click **Create**.
7. Copy the webhook URL.
8. Click **Done**.

![2_ScreenGIF-Getting_the_Webhook_URL.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGIF-Getting_the_Webhook_URL.gif)

*Image source: Microsoft Teams*

### Step 3: Configure Document360

1. Go to **Settings** > **Knowledge base portal** > **Notification channels**.
2. Click **New channel**.
3. Select **Microsoft Teams** and click **Next**.
4. Enter **Friendly name**.
5. Paste the webhook URL.
6. Click **Save**.

![3_ScreenGIF-Settings_up_the_configuration_in_Document360.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGIF-Settings_up_the_configuration_in_Document360.gif)

Go to [**Notification mapping**](/help/docs/notification-mapping) to assign events.

---

## FAQ

**How do I confirm Teams notifications work?**

Test by mapping a sample notification or updating a test article. Check your Teams channel. If problems persist, verify webhook URL and Teams permissions.

**Can I customize Teams notification types?**

Yes, use **Notification mapping** to select specific events like "new article published" or "article updated."

**What if I get authorization errors in Teams?**

Generate a new webhook URL in Teams and update it in Document360. Check channel permissions.

**How do I disable specific Teams notifications?**

In **Notification mapping**, unselect unwanted notification types.

**Can I use different Teams channels for different notifications?**

Yes, create separate Teams channels and configure individual webhooks in Document360. Assign different events through **Notification mapping**.

<a id="smtp-email-notification-channel"></a>

## SMTP notification channel

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

SMTP sends email notifications about critical updates to designated addresses.

Example: Team members receive email alerts when important knowledge base articles update.

---

## Setting up SMTP notification channel

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Click **New channel**.
3. Select **SMTP** and click **Next**.
4. Enter **Friendly name**.
5. Enter recipient emails in **Email to** field.

> NOTE
> 
> * Separate multiple addresses with semicolons (;) and no spaces.
> * Don't add semicolon after last address.
> 
> Example: xyz@gmail.com;abc@gmail.com;mno@gmail.com

6. Click **Save**.

![1_ScreenGIF-setting_up_the_SMTP_notification_Channel.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGIF-setting_up_the_SMTP_notification_Channel.gif)

Go to [**Notification mapping**](/help/docs/notification-mapping) to assign events.

<a id="notification-mapping"></a>

## Notification mapping

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Map notifications to channels for specific events across documentation, security, analytics, and other modules.

---

## Mapping channels to events

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Select **Notification mapping** tab.

> NOTE
> 
> All events are disabled by default.

3. Toggle **All events** to enable everything.
4. Toggle specific modules to enable their notifications.
5. Expand modules to enable individual events.

Example: Enable **Documentation editor** for all editor notifications, or just **Article published** for publish-only alerts.

6. Click **Map to channel** to assign channels to events.
7. Click the icon next to each event to map channels.

> NOTE
> 
> Enabled events require at least one assigned channel.

![1_Screenshot-Notification_mapping_in_the_Knowledge_base_portal.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Notification_mapping_in_the_Knowledge_base_portal.png)

### Analytics weekly report

Project owners can enable weekly analytics reports:

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Select **Notification mapping** tab.
3. Expand **Analytics** and toggle **Analytics weekly mail**.

![2_Screenshot-Analytics_toggle_in_the_Notification_mapping.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Analytics_toggle_in_the_Notification_mapping.png)

---

## Notification events

### Documentation editor

| Event | Function |
| --- | --- |
| Article visibility changed | Visibility settings altered |
| Article settings updated | Settings modified |
| Article slug updated | URL name changed |
| Article title updated | Title changed |
| Article published | Article published |
| Article created | New article created |
| Article renamed | Article renamed |
| Article deleted | Article deleted |
| Article forked | Article copied to new version |
| Article version deleted | Specific version removed |
| Bulk delete article versions | Multiple versions deleted |
| Updated translation status | Translation status changed |
| Articles reordered | Article order changed |
| Article contributors updated | Contributors modified |
| Article workflow status updated | Workflow status changed |
| Article workflow due date updated | Workflow deadline changed |
| Article workflow assignee updated | Workflow assignee changed |
| Category created | New category created |
| Category type updated | Category type changed |
| Category settings updated | Category settings modified |
| Category slug changed | Category URL name changed |
| Category contributors updated | Category contributors changed |
| Category deleted | Category deleted |
| Category renamed | Category renamed |
| Categories reordered | Category order changed |
| Category published | Category published |
| Category forked | Category copied to new version |
| Category version deleted | Specific category version removed |
| Bulk delete category versions | Multiple category versions deleted |
| Category workflow status updated | Category workflow status changed |
| Category workflow due date updated | Category workflow deadline changed |
| Category workflow assignee updated | Category workflow assignee changed |
| Category visibility changed | Category visibility altered |
| Article review reminder status updated | Review reminder status changed |
| Article pushed to Crowdin | Article sent for translation |
| Categories/Articles restored | Deleted items restored |
| Categories/Articles permanently deleted | Items permanently removed |
| Recycle bin emptied | All deleted items permanently removed |
| Shared article created | Collaboration article created |
| Clone article created | Article duplicated |
| Removed reference article | Linked article removed |
| Multiple shared articles created | Multiple collaboration articles created |
| Article publish later canceled | Scheduled publish canceled |
| Article scheduled for publish | Article scheduled for future publish |
| Share link deleted | Private share link removed |
| Share link generated | New private share link created |

### Drive

| Event | Function |
| --- | --- |
| Folder added | New folder created |
| Folder renamed | Folder name changed |
| Folder deleted | Folder deleted |
| File(s) added | New files added |
| File(s) updated | Files modified |
| File(s) deleted | Files removed |

### Knowledge base portal settings

| Event | Function |
| --- | --- |
| Workspace updated | Workspace settings changed |
| Workspace deleted | Workspace removed |
| Workspace created | New workspace created |
| Workspace display order changed | Workspace order modified |
| Plan tier changed | Subscription plan changed |
| Payment details updated | Billing information updated |
| Project general settings updated | Project settings changed |
| Backup created | Backup generated |
| Backup restored | Backup applied |
| Notification channel deleted | Notification channel removed |
| Notification channel created | New notification channel created |
| Notification channel updated | Notification channel modified |
| Addons purchased | Additional features purchased |
| Subscription created | New subscription created |
| API token added | New API token created |
| API token deleted | API token removed |
| Extension token generated | Extension token created |
| Extension token deleted | Extension token removed |
| Crowdin token added | Crowdin translation token created |
| Crowdin token deleted | Crowdin translation token removed |
| Display workspaces as menu | Workspace menu format enabled |

### Knowledge base site settings

| Event | Function |
| --- | --- |
| Site design settings updated | Site appearance changed |
| Custom JavaScript updated | JavaScript code modified |
| Custom CSS updated | CSS styles modified |
| Article settings updated | Article display settings changed |
| Project sub-domain updated | Sub-domain changed |
| Integration created | New service integration established |
| Integration deleted | Service integration removed |
| Integration updated | Service integration modified |
| Home page builder restored | Homepage builder reverted |
| Home page builder settings updated | Homepage builder settings changed |
| Robots.txt updated | Search engine crawling rules changed |
| Site domain updated | Main domain changed |
| Cookie consent enabled | Cookie consent activated |
| Cookie consent disabled | Cookie consent deactivated |
| Cookie consent updated | Cookie consent settings modified |
| Smart bar added | Quick access bar added |
| Smart bar updated | Quick access bar modified |
| Smart bar enabled | Quick access bar activated |
| Smart bar disabled | Quick access bar deactivated |
| Smart bar deleted | Quick access bar removed |
| Ticket deflector deleted | Support request management removed |
| Ticket deflector added | Support request management added |
| Ticket deflector updated | Support request management modified |
| Ticket deflector helpdesk added | Helpdesk added to support requests |
| Ticket deflector helpdesk updated | Helpdesk settings modified |
| Ticket deflector helpdesk deleted | Helpdesk removed from support requests |
| Article redirection rule added | New redirect rule created |
| Article redirect rule updated | Redirect rule modified |
| Article redirection rule(s) deleted | Redirect rules removed |
| Redirect rule(s) exported to CSV | Redirect rules exported |
| Redirect rules import requested | Redirect rules import initiated |
| Meta description generated | SEO description created |
| Meta details updated | SEO settings modified |
| Knowledge base builder updated | Content creation tools modified |
| Knowledge base builder published | Content creation tools published |
| Read receipt rule created | Article view tracking rule created |
| Read receipt rule updated | Article view tracking rule modified |
| Read receipt rule deleted | Article view tracking rule removed |

### Knowledge base widget settings

| Event | Function |
| --- | --- |
| Knowledge base widget settings updated | Widget behavior changed |
| URL mapping created | New URL mapping created |
| URL mapping updated | URL mapping modified |
| URL mapping deleted | URL mapping removed |
| Knowledge base widget settings deleted | Widget functionality removed |
| Knowledge base widget settings created | Widget functionality enabled |

### Users & Security settings

| Event | Function |
| --- | --- |
| Site visibility changed | Site access settings changed |
| Role added | New user role created |
| Role updated | User role permissions modified |
| Role deleted | User role removed |
| Security group added | New security group created |
| Security group updated | Security group settings changed |
| Security group deleted | Security group removed |
| Content access added | Content permissions granted |
| Site access added | Site access granted |
| Content access updated | Content permissions modified |
| Site access updated | Site permissions modified |
| Content access removed | Content permissions revoked |
| Site access removed | Site permissions revoked |
| Team account added | New team account created |
| Team account updated | Team account modified |
| Team account deleted | Team account removed |
| IP restrictions updated | IP access rules changed |
| IP restriction added | New IP restriction created |
| IP restriction deleted | IP restriction removed |
| Self sign-up settings updated | Registration settings changed |
| Import readers requested | Reader import initiated |
| Import team account requested | Team account import initiated |
| Export team account(s) to CSV | Team account data exported |
| Export reader(s) to CSV | Reader data exported |
| SSO configuration added | New SSO authentication created |
| SSO configuration updated | SSO settings modified |
| SSO configuration deleted | SSO authentication removed |
| SSO users invited | SSO access invitations sent |
| JWT created | New authentication token created |
| JWT regenerated | Authentication token refreshed |
| JWT saved | Authentication token stored |
| JWT updated | Authentication token modified |
| JWT deleted | Authentication token removed |
| Inheritance settings updated | Permission inheritance changed |
| Convert to reader | User account changed to reader |
| Convert to SSO team account | User converted to SSO team account |
| Convert to SSO reader | User converted to SSO reader |
| Convert to team account | User converted to team account |

### Tools settings

| Event | Function |
| --- | --- |
| Project exported | Project backup completed |
| Project imported | External content integrated |
| External project import requested | External project import initiated |
| Export PDF requested | PDF export initiated |
| Export PDF content template added | New PDF format template created |
| Export PDF content template updated | PDF format template modified |
| Export PDF content template deleted | PDF format template removed |
| Export PDF design template added | New PDF design template created |
| Export PDF design template deleted | PDF design template removed |
| Export PDF design template updated | PDF design template modified |
| Article review reminder created | Article evaluation reminder set |
| Article review reminder updated | Review reminder modified |
| Article review reminder deleted | Review reminder removed |
| Content reuse variable added | New content management variable created |
| Content reuse variable updated | Content variable modified |
| Content reuse variable deleted | Content variable removed |
| Content reuse snippet added | New content snippet created |
| Content reuse snippet updated | Content snippet modified |
| Content reuse snippet deleted | Content snippet removed |
| Article template added | New article format template created |
| Article template updated | Article template modified |
| Article template deleted | Article template removed |
| Tag added | New content tag created |
| Tag updated | Content tag modified |
| Tag deleted | Content tag removed |
| Article imported | New article added |
| Workflow status added | New content workflow status created |
| Workflow status updated | Workflow status modified |
| Workflow status deleted | Workflow status removed |
| Workflow status reordered | Workflow status sequence changed |
| Update feedback assignee | Feedback reassigned |
| Update feedback status | Feedback status changed |
| Find and replace | Content search and replace executed |
| Content reuse glossary suggested | Content management suggestion made |
| Export PDF password removed | PDF security removed |

### Knowledge site

| Event | Function |
| --- | --- |
| Feedback received | User feedback submitted |
| Reader email updated | Reader email changed |
| Reader self-registration | New reader registered |
| Like received | Article received positive feedback |
| Dislike received | Article received negative feedback |

### AI notifications

| Event | Function |
| --- | --- |
| Credit usage alert | AI credits running low |

### Analytics

| Event | Function |
| --- | --- |
| Analytics weekly metrics | Weekly performance reports available |

### All comments notification

| Event | Function |
| --- | --- |
| All comments notifications | Contributors notified of inline comments |

---

## FAQ

**How do I get Slack notifications for article publishing?**

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Expand **Documentation editor** and enable **Article published**.
3. Ensure Slack channel is configured. If not, click the icon next to the toggle and enable Slack.

> NOTE
> 
> See [Slack notification channel](/help/docs/slack-notification-channel).

**How do I get Teams notifications when projects export?**

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Expand **Tools settings** and enable **Project exported**.
3. Ensure Microsoft Teams channel is configured. If not, click the icon and enable Teams.

> NOTE
> 
> See [Microsoft Teams notification channel](/help/docs/microsoft-teams-notification-channel).

**How do I get email notifications for new team accounts?**

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Expand **Users & Security settings** and enable **Team account added**.
3. Ensure SMTP channel is configured. If not, click the icon and enable SMTP.

> NOTE
> 
> See [SMTP notification channel](/help/docs/smtp-email-notification-channel).

**How do I get alerts for Eddy AI credit usage?**

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Expand **Eddy AI notifications** and enable **Credit usage alert**.

Document360 notifies configured channels when credits fall to 20%, 10%, or expire.

**How do contributors get inline comment notifications?**

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Enable **All comments notification**.

Contributors receive email alerts for inline comments on their articles.

**Why aren't I receiving email notifications for article creation?**

Enable **Article created** notification:

1. Go to **Settings** > **Knowledge base portal** > **Notifications** > **Notification mapping**.
2. Expand **Documentation editor**.
3. Toggle **Article created** ON.

> NOTE
> 
> Article creation via [Word import](/help/docs/importing-articles-from-a-docx-file) doesn't trigger this notification.

If issues persist, contact [Document360 support](https://document360.com/support/).

<a id="notification-history"></a>

## Notification history

**Plans supporting notification settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Track notification delivery to troubleshoot failures.

Example: Verify critical Slack alerts delivered successfully. Identify and resolve delivery failures quickly.

---

## Managing notification history

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Select **Notification history** tab.

![1_Screenshot-Notification_history_overview_page.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Notification_history_overview_page.png)

### Understanding notification history

Each notification shows:

1. **Channel name:** Slack, Webhook, SMTP, or Teams
2. **Status:** Success or Failure
3. **Submitted on:** Trigger date
4. **Sent on:** Delivery date
5. **History:** Click **View details** for message content

<a id="send-notifications-from-custom-email-domain"></a>

## Email domain

**Plans supporting email domain settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Send notifications from branded email addresses like `support@yourcompany.com` instead of `support@document360.com`.

---

## Prerequisites

* Access to DNS provider (GoDaddy, Hostinger, Namecheap, etc.)
* Available only on **Enterprise plan**

---

## Configuring custom email domain

1. Go to **Settings** > **Knowledge base portal** > **Notifications**.
2. Select **Email Domain** tab.
3. Enter domain name (e.g., `yourcompany.com`).
4. Click **Add Domain** to generate DNS records.

### Adding DNS records

5. Open your DNS provider's website.
6. Copy configuration details from Document360 and paste into DNS settings.

> NOTE
> 
> Adding these records won't override existing MX records.

7. Return to Document360 **Email domain** page.
8. Check **I've added the records** and click **Verify & Save**.

After verification, enter sender information:
* **Email field:** From address (e.g., `support@yourcompany.com`)
* **Name field:** Sender name (e.g., `Your Company Support`)

![1_Screenshot-Email_domain.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Email_domain.png)

---

## Troubleshooting

If configuration remains inactive after 24 hours:
1. Verify MX and TXT records saved on domain host
2. Confirm records match Document360's provided values
3. Delete and re-add records if needed

Contact `support@document360.com` for assistance.

---

## FAQ

**What are MX records and how do they work?**

MX records route emails to correct mail servers. Lower numbers indicate higher priority.

Example:
* `10 mail1.example.com` (primary)
* `20 mail2.example.com` (backup)

**How do TXT records work for email authentication?**

TXT records store text information for domain verification and email security policies like SPF, DKIM, and DMARC.

SPF example: `v=spf1 include:_spf.google.com ~all`

This specifies authorized mail servers, preventing spoofing.

<a id="how-to-use-postman"></a>

## How to use Postman?

**Plans supporting API token settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Postman builds and tests APIs. Link your Document360 project in minutes using desktop or web versions.

---

## Linking Document360 project in Postman

1. Open Postman.
2. In **My Workspace**, click **Import**.
3. Enter URL: `https://apihub.document360.io/swagger/v2/swagger.json`.
4. Select import option (Postman Collection or OpenAPI 3.0).
5. Click **Import**.

Creates sample requests for each endpoint.

![10_ScreenGif-Postman.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_ScreenGif-Postman.gif)

### Authentication in Postman

1. Expand **Document360 Customer API** in tree view.
2. Set **Auth Type** to API Key.
3. Enter variable name in **Key** field.
4. Enter API token in **Value** field. Generate tokens at **Settings** > **Knowledge Base portal** > **API tokens**.

![11_ScreenShot-Postman.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/11_ScreenShot-Postman.png)

### Environment setup

1. Go to **Environments** in left navigation.
2. Click **Create Environment**.
3. Add variable 'base_URL' with type 'default'.
4. Enter `https://apihub.document360.io` in **INITIAL VALUE** and **CURRENT VALUE**.
5. Click **Save**.

Authentication complete. Access endpoints freely.

![9_ScreenShot-Postman.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_ScreenShot-Postman.png)

### Use cases

* [Create and publish articles](https://apidocs.document360.com/v2/docs/how-to-create-and-publish-an-article)
* [Update published articles](https://apidocs.document360.com/v2/docs/how-to-update-a-published-article)
* [Update SEO details](https://apidocs.document360.com/v2/docs/how-to-update-seo-details)

---

## FAQ

**What if my Postman session ends after refresh?**

Re-authenticate following the setup steps above.

<a id="how-to-use-swagger"></a>

## How to use Swagger?

**Plans supporting API token settings**

| Professional | Business | Enterprise |
| --- | --- | --- |

Swagger creates interactive, machine-readable API documentation for RESTful APIs.

---

## Swagger documentation site

1. Open [Swagger documentation](https://apihub.document360.io/).
2. Click **Authorize**.
3. Enter API token in **Value** field.

> NOTE
> 
> Generate new tokens at **Settings** > **API tokens**:
> * Name your token
> * Select HTTP methods (GET, PUT, POST, DELETE)
> * Copy the generated token

4. Click **Authorize**.
5. Click **Close**.

![17_ScreenShot-Swagger.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/17_ScreenShot-Swagger.png)

> NOTE
> 
> To change tokens: Click **Authorize** > **Logout** > enter new token > **Authorize** > **Close**.

### GET

Retrieve information. Example: Get team account records.

![12_ScreenShot-Swagger_Get.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/12_ScreenShot-Swagger_Get.png)

1. Fill required fields.
2. Click **Execute**.
3. View results in **Responses**.

![13_ScreenShot-Swagger_Get.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/13_ScreenShot-Swagger_Get.png)

### POST

Add items. Example: Add team account.

![14_ScreenShot-Swagger_Post.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/14_ScreenShot-Swagger_Post.png)

1. Enter account details (email_id, first_name, last_name).
2. Click **Execute**.
3. Success if status is 200 and success is true.

### PUT

Update items. Example: Update user role.

![15_ScreenShot-Swagger_Put.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/15_ScreenShot-Swagger_Put.png)

1. Enter userId.
2. Update role (1=Administrator, 2=Editor, 3=Draft Writer, 4=Reader, 7=Owner).
3. Click **Execute**.
4. Success if status is 200 and success is true.

### DELETE

Delete items. Example: Delete userId.

1. Enter userId.
2. Click **Execute**.
3. Success if status is 200 and success is true.

![16_ScreenShot-Swagger_Delete.png](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/16_ScreenShot-Swagger_Delete.png)

> NOTE
> 
> Required fields marked with asterisks must be filled.

---

## FAQ

**What if refreshing ends my session?**

Re-authenticate following the steps above.

**How should I format fields requiring specific characters?**

Use underscores. Example: "email_id" not "email id". Spaces cause errors.

<a id="full-portal-search"></a>

## Portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |

Search all project content, files, tags, users, tools, and settings across workspaces and languages.

---

## Accessing full portal search

1. Click **Search** icon in top navigation bar.
2. Enter keyword and use **All** dropdown to narrow results.

Six search modules available:
* [All](/help/docs/full-portal-search)
* [Article](/docs/article-full-portal-search)
* [Drive file](/docs/drive-full-portal-search)
* [Users & Groups](/docs/users-groups-full-portal-search)
* [Tags](/docs/tags-full-portal-search)
* [Settings](/docs/settings-full-portal-search)

> NOTE
> 
> Press **Escape** to close search screen.
> Only five results per module displayed initially.

3. Click **More articles** for additional results.
4. Apply **Filter** if needed.
5. Click search item to preview.
6. Click **Go to article** to navigate.

![1_ScreenGif-Full_portal_search.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Full_portal_search.gif)

---

## FAQ

**What can I search and are keywords highlighted?**

Search articles/categories, Drive files, Users & Groups, Tags, Content tools, and Settings. Keywords highlighted in results.

**Why isn't analytics information appearing in search results?**

Analytics data excluded from search. Settings module shows Analytics-related information.

<a id="article-full-portal-search"></a>

## Article portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |

Search all project articles and category pages across workspaces and languages.

---

## Accessing articles through portal search

1. Click **Search** icon in top navigation bar.

> NOTE
> 
> Press **Escape** to close search screen.

2. Select **Articles** from **All** dropdown.
3. Type keyword to search.
4. Results display automatically with:

* Article title
* Breadcrumb
* Workspace
* Language
* Status

5. Apply filters using **Filter** option.
6. Click result to preview.
7. Click fullscreen icon to expand preview. Use navigation buttons to move between results.
8. Click **Go to article** in preview to navigate.

![2_ScreenGif-Article_full_portal_search.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGif-Article_full_portal_search.gif)

---

## Filters

### a. Workspace/Language

Select Workspaces and Languages. Language options appear when Workspace dropdown expands. Select **Workspace** checkbox or apply no filter to search all.

### b. Visibility

Filter by article visibility: **None** (default, no filter), **Visible**, or **Hidden**.

### c. Status

Filter by article status: **None** (default, no filter), **New article**, **Draft**, or **Published**.

### d. Contributors

Filter by contributors. Use dropdown and search by username.

### e. Tags

Filter by specific tags. Search and select multiple tags.

### f. Updated on

Filter by update date range: **7 days**, **30 days**, **3 months**, **1 year**, or **custom date**.

Select filters and click **Apply**. Click **Clear** to reset.

<a id="drive-full-portal-search"></a>

## Drive portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |

Search all Drive files in your project.

---

## Accessing Drive portal search

1. Click **Search** icon in top navigation bar.

> NOTE
> 
> Press **Escape** to close search screen.

2. Select **Drive** from **All** dropdown.
3. Type search keyword.

Results display in **List view**.

> NOTE
> 
> Switch to **Grid view** using icon next to **Filter** option.

Search results show:
* **Name**
* **Dependencies**
* **Updated on**
* **Updated by**
* **Size**
* **Tags**

4. Click file name or eye icon to open **File details** pane.

Shows file location, size, type, upload date, uploader, and tags.

5. Click **View dependencies** to see where files are used.

Clicking dependent articles/categories redirects to Editor.

![3_ScreenGif-Drive_full_portal_search.gif](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Drive_full_portal_search.gif)

---

## Filters

### a. Status

Filter files: **All files** (default), **Deleted files**, or **Starred files**.

### b. Type

Filter by file type: **Images**, **Word**, **Excel**, **PPT**, **PDF**, **ZIP**, **Video**, **Audio**, or **Others**. Select multiple types.

### c. Uploaded by

Filter by uploader account.

### d. Tags

Filter by specific tags. Search and select multiple tags.

### e. Uploaded

Filter by upload date range: **7 days**, **30 days**, **3 months**, **1 year**, or **custom date**.

Click **Apply** after selecting filters. Click **Clear** to reset.

<a id="users-groups-full-portal-search"></a>

## Users & groups portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |

Search team accounts, team account groups, readers, and reader groups in your knowledge base project.## Users & groups portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Search team accounts, team account groups, readers, and reader groups in your knowledge base project.

### Accessing Users & Groups search

1. Click the **Search** icon in the top navigation bar
2. Select **Users & Groups** from the dropdown next to the search bar
3. Enter your search keyword

Results display in two tabs: **Team accounts & groups** and **Readers & groups**.

**Team accounts & groups tab** shows:
* Name
* Portal role  
* Login activity

**Readers & groups tab** shows:
* Name
* Login activity

### Team accounts

Click any team account to open the **View access permissions** panel. Click **Manage permissions** to go to the Team account page.

### Team account groups

Click any team account group to open the **View access permissions** panel. Click **View associated team members** to go to the Team account group page.

![Search team accounts and groups](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_ScreenGif-Users&Groups_Search.gif)

### Readers

Click any reader to navigate to the **Readers** page.

### Reader groups

Click **View associated readers** to see readers in that group and their content access.

![Search readers and groups](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_ScreenGif-Readers&Groups_Search.gif)

---

## Filters

![Users and groups filter option](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-users-and-groups-filter.png)

### 1. Type

Filter by entity type: **All entity**, **Team account**, **Team account groups**, **Reader**, **Reader Groups**

Default: **All entity**

### 2. Last logged in

Filter by login date: **All**, **7 days**, **30 days**, **3 months**, **1 year**, **Custom date**

Default: **All**

Click **Apply** after selecting filters. Click **Clear** to reset.

---

## Tags portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Search and view tags in your knowledge base project. See dependency information for each tag.

---

### Accessing Tags search

1. Click the **Search** icon in the top navigation bar
2. Select **Tags** from the dropdown next to the search bar  
3. Enter your search keyword

Results show:
* Tag name
* Dependency in articles
* Dependency in category pages
* Dependency in drive files

### Viewing tag dependencies

Click any tag to open the **Tag Dependency** panel.

**Article/category dependencies show:**
* Name
* Version
* Language
* Contributor
* Status indicator
* Publish date

Click any article/category to open the documentation editor.

**File dependencies show:**
* Thumbnail (images only)
* Filename and format

Click **Download** to save files locally.

### Removing dependencies

1. Select checkboxes next to dependencies in the panel
2. Click **Remove dependencies**
3. Click **Cancel** to close panel

![Search tags in articles, categories, and files](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_ScreenGif-Tags_Full_portal_search.gif)

---

## Settings portal search

**Plans supporting portal search**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Search through knowledge base portal features and settings.

---

### Accessing Settings search

1. Click the **Search** icon in the top navigation bar
2. Select **Settings** from the dropdown next to the search bar
3. Enter your search keyword

Settings grouped under:
* Knowledge base portal
* Knowledge base site  
* Users & Security

Results display in **Grid view** showing:
* Setting/feature name
* Feature icon
* Description

Click any setting to navigate to its page.

![Search settings in portal](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_ScreenGif-Settings_search.gif)

---

## Custom domain mapping

**Plans supporting custom domain mapping**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Document360 automatically generates a default domain like `project-name.document360.com`. You can create a custom domain like `help.yourcompany.com` for better branding and user experience.

Navigate to **Settings** > **Knowledge base site** > **Custom domain**.

> NOTE: New projects use the project name as the default domain. A project named "Project Greenfield" gets `project-greenfield.document360.com`.

---

### Editing default domain

1. Go to **Custom domain** page
2. Click **Edit** next to the default domain
3. Enter your preferred domain

* If unavailable, **Update** button is disabled
* If available, **Update** button is enabled

4. Click **Update**

![Edit default domain](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1729603511681.png)

---

### Creating custom domain

1. [Add custom domain in Document360](/docs/custom-domain-mapping#add-domain-in-document360)
2. [Configure CNAME at domain registrar](/docs/custom-domain-mapping#setting-up-your-cname)  
3. [Verify custom domain](/docs/custom-domain-mapping#verify)

---

#### Adding custom domain in Document360

![Add custom domain](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1729689317870.png)

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Custom domain mapping**
2. Enter custom domain in **Domain configuration** field
3. Click **Add domain**

![Domain configuration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1729689397597.png)

Once setup completes, DNS records generate and you'll see a notification.

---

#### Configuring CNAME record

After adding your domain in Document360, configure a CNAME record at your domain registrar to point to Document360's servers.

1. Log into your domain registrar (GoDaddy, Namecheap, etc.)
2. Go to DNS settings
3. Add new CNAME record:
   * Enter your custom domain in Name/Host field
   * Enter Document360's CNAME value in Points to/Value field
4. Save the record

---

##### Example: Hostinger

1. Go to Hostinger domain management
2. Select your domain
3. Click **DNS/Nameservers** > **DNS records** tab
4. Choose CNAME from record type dropdown
5. Paste Document360's value in **Points to** field
6. Add TTL and click **Add record**

![Hostinger DNS configuration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1729715957848.png)

---

##### Common registrars

* **NameCheap** - [Support article](https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/)
* **Domain.com** - [Support article](https://www.domain.com/help/article/dns-management-how-to-update-dns-records)
* **Google Domains** - [Support article](https://support.google.com/a/answer/47283)
* **Dreamhost** - [Support article](https://help.dreamhost.com/hc/en-us/articles/360035516812-Adding-custom-DNS-records)
* **Hover** - [Support article](https://help.hover.com/hc/en-us/articles/217282457-Managing-DNS-records-)
* **GoDaddy** - [Support article](https://in.godaddy.com/help/add-a-cname-record-19236)
* **Cloudflare** - [Support article](https://community.cloudflare.com/t/how-do-i-add-a-cname-record/59)
* **Bluehost** - [Support article](https://www.bluehost.com/hosting/help/cname)

---

#### Verifying custom domain

1. Return to Document360 **Custom domain** settings
2. Check "**I've added the records**" box
3. Click **Verify**
4. Success message appears if verification works

> NOTE: Contact [support](mailto:support@document360.com) if issues occur.

Click **Go to your knowledge base site** icon to see the new URL.

---

### Post-mapping issues

**"'Deceptive site ahead' message after successful mapping**

Google flagged your custom domain as unsafe.

* Check status at [Google Safe Browsing](https://transparencyreport.google.com/safe-browsing/search)
* Enter your domain to see issues
* Fix detected problems (phishing, malware, guideline violations)
* Submit review request through Google Search Console

[Google support article](https://support.google.com/chrome/answer/99020?hl=en&co=GENIE.Platform%3DDesktop)

![Site status troubleshooting](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1730023063313.png)

---

## Load balancer

A load balancer distributes traffic across multiple servers to keep your knowledge base fast and reliable during high traffic. It prevents server overload and improves performance and security.

Upgrading provides better security features and traffic management.

---

### Upgrading load balancer

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Custom domain mapping**
2. Click **Upgrade**
3. Verify custom domain configuration
4. Copy generated CNAME record
5. Set up CNAME at domain registrar
6. Verify configuration again

> NOTE:
> * No downtime occurs, but upgrade during off-hours
> * Upgrade is free
> * Contact [support](mailto:support@document360.com) for help

---

## Configuring custom domain for Apex domains

Use your root domain (like `abc.com`) without subdomains. While subdomains are straightforward, Apex domains require extra DNS steps.

**DNS flattening** lets you use CNAME records at the root domain level. Not all registrars support this.

---

### Configuring Apex domains

If your registrar doesn't support DNS flattening (like GoDaddy), use a DNS provider that does, such as Cloudflare. Cloudflare offers free DNS flattening.

For example, switch from GoDaddy to Cloudflare to add CNAME records for Apex domains.

> NOTE: Read Cloudflare's [CNAME flattening article](CNAME flattening) for details.

---

### Custom SSL certificates

Use Document360's automatic SSL certificate for seamless renewal. If you prefer your own certificate, provide:

* **Common Name (CN)**: Fully qualified domain name
* **Organization (O)**: Legal organization name  
* **Organizational Unit (OU)**: Department/division

> NOTE: Certificates valid for 90 days. Renew on time and provide updated certificate.

---

## Troubleshooting

---

### Domain verification failed

Ensure CNAME matches domain host. Other records (like AAAA) in CNAME's place cause errors.

**Solution**: Use DNS lookup tools like [Digwebinterface](https://www.digwebinterface.com/) or [Google DNS lookup](https://toolbox.googleapps.com/apps/dig/) to check records.

![Troubleshooting invalid records](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1729966781926.png)

> NOTE: Some registrars (like Cloudflare) mask DNS records for security. Contact registrar for details.

Correct CNAME may take up to 24 hours to propagate.

---

### Wait time after DNS record updates

If CNAME matches but verification fails, TTL might be the issue.

DNS record changes take time to reflect globally. TTL of 3600 means up to 1 hour for global propagation.

---

### CAA restrictions

Some registrars restrict SSL certificates to specific Certificate Authorities (CAs).

Example: CAA record "0 issue letsencrypt.org" allows only Let's Encrypt certificates. Other CAs (like DigiCert) will be denied.

Check DNS configuration for CAA records.

---

### "This site can't be reached" error

1. Verify record configuration timing
2. Confirm DNS propagation (24-hour rule)
3. Use Google Dig tool to check records for duplicates
4. Check CAA records at [dnschecker.org](https://dnschecker.org/)
5. Ensure CAA entries exist for Document360's SSL providers:
   * Lets Encrypt
   * DigiCert  
   * Google

Add these CAA records:
```
@ IN CAA 0 issue digicert.com
@ IN CAA 0 issue letsencrypt.org
@ IN CAA 0 issue pki.goog
```

---

### "Connection not private/secure" errors

---

#### A. SSL certificate expired

1. Check certificate expiration
2. Visit site and click **View site information** in URL bar
3. Click **Connection is secure** to see certificate details

---

#### B. Other troubleshooting steps

1. Try different browser
2. Disable browser extensions
3. Check if all users affected
4. Clear browser cache or try another browser

---

#### C. VPN issues

1. Disable VPN and test
2. If fixed, VPN caused problem
3. Contact IT team

---

#### D. DNS record issues

1. Use DNS checker (like [DNS Checker](https://dnschecker.org/)) to verify records
2. Confirm all records updated
3. If not synced, contact DNS provider or registrar

Contact [Document360 support](https://document360.com/support/) if problems persist.

---

## FAQs

---

### Do I need an SSL certificate for custom domains?

Document360 provides automatic SSL certificates. No purchase needed. For custom certificates, contact [support@document360.com](mailto:support@document360.com).

---

### Will custom domains appear in reader invitation emails?

Yes, emails sent after successful mapping use custom domain links.

---

### What if CNAME doesn't verify after DNS updates?

Reconfigure custom domain:

1. Remove current configuration
2. Re-add custom domain
3. Update CNAME records
4. Verify setup

---

### Can I configure two custom domains for one KB site?

No. One custom domain per KB site. Set up redirects between domains instead.

---

### Can I set multiple domains for one project?

Currently, Document360 supports one custom domain per project.

---

### What is a Naked Domain?

Domain without "www" prefix. `example.com` is naked, `www.example.com` is not.

Most domains default to "www" subdomain. Naked domains like `yourcompany.com` exclude this.

---

### What is a domain registrar?

Company where you purchase and manage domain names (GoDaddy, Namecheap, Google Domains). Update settings here to connect domains to Document360.

---

### What is a CNAME record?

DNS setting that connects your custom domain (like `help.yourcompany.com`) to another address. Ensures users reach your knowledge base when typing custom domain.

---

### Why upgrade to new load balancer?

* SSL offloading reduces server load and improves security
* Web Application Firewall (WAF) protects against common attacks
* Dynamic traffic management for optimal distribution

Recommended for improved security and reliability.

---

### Can I create separate domains for each project version?

No. Versions share the same domain. Customize path within existing domain only.

---

## Hosting Document360 on subdirectory

**Plans supporting subdirectory hosting**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

---

### What is subdirectory hosting?

Organize website content using folders under root domain. Subdirectory comes after domain name.

Example: Document360's root domain is `document360.com`. Subdirectory URL: `document360.com/docs/`

Most companies use subdirectories like `/docs` or `/support`.

SEO benefit: subdirectories (`example.com/docs`) rank better than subdomains (`docs.example.com`).

> NOTE: Works with Document360 domains and custom domains.

---

### Enabling subdirectory hosting

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Subfolder hosting** tab
2. Default path is `/docs`
3. Turn on toggle for "This documentation is hosted on a sub folder"

![Subfolder hosting settings](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Subfolder_hosting_tab_in_settings.png)

---

### Custom subdirectory paths

Use paths other than `/docs` like `/help` or `/support`.

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Subfolder hosting** tab
2. Clear **Subfolder path** field
3. Enter custom path (e.g., `/help`)
4. Click **Update**

> NOTE: For projects with custom domains and subfolder hosting, **Article preview** not supported.

![Custom subfolder path](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Custom_domain_subfolder_path.png)

---

### Custom Site API paths

Available only for KB site 2.0 projects. Default path is `/api`.

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Subfolder hosting** tab
2. Clear **Site API path** field
3. Enter custom path (e.g., `/docs-api`)
4. Click **Update**

> CAUTION: KB site 2.0 requires both **Subfolder path** and **Site API path** defined.

> NOTE: This is not for **API Documentation**.

![Custom API path](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Custom_domain_site_api_path.png)

---

## Web servers

Common web servers:
* Apache HTTP server
* Nginx server  
* ASP.NET Core server
* Microsoft IIS server
* OpenResty server
* LiteSpeed server
* Cloudflare server

> NOTE: Web server stores and delivers website content to clients (usually browsers).

---

## What happens next?

Knowledge base goes live on custom subdirectory. Original URL still works.

Example: `example.document360.io` and `example.com/docs` both point to same site.

Causes duplicate content in search engines. Enable redirect to prevent this.

> NOTE: Contact [support@document360.com](mailto:support@document360.com) to enable redirect.

---

## FAQs

---

### What is a Canonical URL?

Official URL that tells search engines which version to index when multiple URLs show same content. Prevents duplicate content issues.

Example URLs for same page:
* `https://example.com/page`
* `https://www.example.com/page`  
* `https://example.com/page?utm=123`

Set one (e.g., `https://www.example.com/page`) as canonical.

---

### How to configure canonical URL in Document360?

Use Canonical domain setting to globally replace project subdomain with specified domain in all articles.

1. Go to **Settings** > **Knowledge base site** > **Custom domain** > **Subfolder hosting** tab
2. Find **Canonical domain** option
3. Enter desired domain (e.g., `https://www.yourdomain.com`)
4. Click **Save**

---

## Nginx server - Subfolder hosting

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Nginx is open-source web server. [Documentation](https://nginx.org/en/docs/)

---

### Setting up subdirectory

Example configuration:

> NOTE: Replace example domains with your Document360 domain or custom domain.
> * Example: `example.document360.io`
> * Subdirectory: `/docs`

1. Add location blocks to Nginx config (`/etc/nginx/default`):

```
location /docs {
    proxy_pass https://example.document360.io/docs;
    proxy_set_header Host example.document360.io;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header "requested-by" "proxy";
    proxy_ssl_server_name   on;
}
```

2. Restart Nginx:
`$ sudo systemctl restart nginx`

> NOTE: KB Site 2.0 requires both Subfolder path and Site API path defined.

---

### Setup for non-`/docs` paths

Use paths like `/help` or `/support`.

When setting custom paths, add languages for each workspace.

```
location /help {
    proxy_pass https://example.document360.io/docs;
    proxy_set_header Host example.document360.io;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header "requested-by" "proxy";
    proxy_ssl_server_name   on;

    sub_filter "v1/docs/" "v1/help/";
    sub_filter "docs/he/" "/help/he";
    sub_filter "/docs/" "/help/";
    sub_filter_once off;
}
```

1. Restart Nginx
2. `$ sudo systemctl restart nginx`

---

### Enable workspace dropdown

Add code blocks for each workspace in your project.

Example with two workspaces (**v1** and **v2**):

```
location /v2/help {
    proxy_pass https://example.document360.io/v2/docs;
    proxy_set_header Host example.document360.io;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header "requested-by" "proxy";
    proxy_ssl_server_name   on;

    sub_filter "v2/docs/" "v2/help/";
    sub_filter "docs/he/" "/help/he";
    sub_filter "/docs/" "/help/";
    sub_filter_once off;
}
-----------------------------------------------------
location /v1/help {
    proxy_pass https://example.document360.io/v1/docs;
    proxy_set_header Host example.document360.io;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header "requested-by" "proxy";
    proxy_ssl_server_name   on;

    sub_filter "v1/docs/" "v1/help/";
    sub_filter "docs/he/" "/help/he";
    sub_filter "/docs/" "/help/";
    sub_filter_once off;
}
-----------------------------------------------------
location = /v2/docs {
    return 301 /v2/help;
}
-----------------------------------------------------
location = /v1/docs {
    return 301 /v1/help;
}
```

> NOTE: Add location blocks for all public workspaces to enable dropdown navigation.

1. Restart Nginx
2. `$ sudo systemctl restart nginx`

---

## Helpful links

* [NGINX Docs: Configuring NGINX as Web Server](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/)
* [DigitalOcean: Understanding Nginx Location Blocks](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms)

---

## Sitemap generation

Example configuration:

> NOTE: Replace example domain with your Document360 or custom domain.
> * Example: `example.document360.io`
> * Sitemap: `example.document360.io/sitemap.xml.en`

```
location /sitemap.xml.en {
proxy_pass https://example.document360.io/sitemap.xml.en;
proxy_set_header Host example.document360.io;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header "requested-by" "proxy";
proxy_ssl_server_name   on;
```

---

## Homepage on subdirectory

Add code blocks for each workspace homepage.

Example with two workspaces (**V1** and **V2**):

```
location =/v1 {
proxy_pass https://example.document360.io/;
proxy_set_header Host example.document360.io;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header "requested-by" "proxy";
proxy_ssl_server_name   on;
}
location =/v2 {
proxy_pass https://example.document360.io/;
proxy_set_header Host example.document360.io;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header "requested-by" "proxy";
proxy_ssl_server_name   on;
}
location /v1/en {
  return 301 /v1;
}
location /v2/en {
  return 301 /v2;
}
```

> PRO TIP: Equal sign matches exact URI. When matched, search stops. [Details](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/#locations)

1. Restart Nginx
2. `$ sudo systemctl restart nginx`

**Knowledge base homepage**

Default appears at root (e.g., `example.document360.io`). Workspace/language-specific: `example.document360.io/v2/he`

---

## What happens next?

Knowledge base goes live on custom subdirectory. Original URL still works.

Example: `example.document360.io` and `example.com/docs` both point to same site.

Causes duplicate content in search engines. Enable redirect to prevent this.

> NOTE: Contact [support@document360.com](mailto:support@document360.com) for redirect setup.

---

## Troubleshooting

---

### Invalid location directive

**Error:** nginx: [emerg] "location" directive not allowed here

Occurs when location blocks are outside server context.

**Fix:**
1. Place location blocks within server block:

```
server {
    listen 80;
    server_name example.com;
    location /docs {
        proxy_pass https://example.document360.io/docs;
        proxy_set_header Host example.document360.io;
    }
}
```

2. Don't place location directives in global `http` context

Contact [support](https://document360.com/support/) if issues persist.

---

### Certbot package unavailable

**Error:** No package Certbot available

EPEL repository not enabled on RHEL-based systems.

**Fix:**
1. Enable EPEL:
`sudo yum install epel-release`

2. Install Certbot:
`sudo yum install certbot`

3. Verify internet access and repository files in `/etc/yum.repos.d/`

Contact [support](https://document360.com/support/) if problems persist.

---

### Nginx configuration test failed

**Error:** NGINX configuration test failed

Syntax error in configuration file.

**Fix:**
1. Test configuration:
`sudo nginx -t`

2. Review error message and line number:

```
nginx: [emerg] invalid parameter "proxy_pas" in /etc/nginx/sites-enabled/example:22
nginx: configuration file /etc/nginx/nginx.conf test failed
```

3. Fix configuration (example):

```
# Incorrect
proxy_pas https://example.com;

# Correct  
proxy_pass https://example.com;
```

4. Restart Nginx:
`sudo systemctl restart nginx`

Contact [support](https://document360.com/support/) if issues persist.

---

### SSL certificate not working

Certificate details don't match configuration or installation failed.

**Fix:**
1. Verify certificate:
`openssl x509 -in /etc/letsencrypt/live/yourdomain.com/fullchain.pem -text -noout`

2. Confirm configuration matches certificate details

3. Correct SSL configuration example:

```
server {
    listen 443 ssl;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
}
```

4. Restart Nginx:
`sudo systemctl restart nginx`

Contact [support](https://document360.com/support/) if problems persist.

---

### FAQ

**Why is homepage not available?**

Ensure homepage is published in site builder and accessible to intended audience.

---

## ASP.NET Core server

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Integrate documentation into existing website using subfolders like `/help` to access knowledge base at `example.document360.io/help`.

Replace example domains with your Document360 or custom domain.

---

### Setting up subfolder path

1. Install [ASP.Net Core package](https://www.nuget.org/packages/Microsoft.AspNetCore.Proxy/)
2. Configure `Standard.cs`:

```
public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            /// ...
            app.MapWhen(ctx => ctx.Request.Path.StartsWithSegments("/docs"),
                builder => builder.RunProxy(new ProxyOptions() {
                    Scheme = "https",
                    Host="example.document360.io"
            }));
            
           /// ...
```

> NOTE: KB Site 2.0 requires both Subfolder path and Site API path defined.

---

## What happens next?

Knowledge base goes live on custom subfolder. Original URL still works.

Example: `example.document360.io` and `example.com/docs` both point to same site.

Causes duplicate content in search engines. Enable redirect to prevent this.

> NOTE: Contact [support@document360.com](mailto:support@document360.com) for redirect setup.

---

## Microsoft IIS server

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Integrate documentation into existing website using subfolders like `/help` to access knowledge base at `example.document360.io/help`.

Replace example domains with your Document360 or custom domain.

---

### Prerequisites

* [Application Request Routing module](https://www.iis.net/downloads/microsoft/application-request-routing)  
* [URL Rewrite Module](https://iis-umbraco.azurewebsites.net/downloads/microsoft/url-rewrite)

---

### Setting up subfolder path

1. Install [URL Rewrite module](https://www.iis.net/downloads/microsoft/url-rewrite)
2. Install and enable Application Request Routing module
3. Add rewrite rules to `web.config` for `/help` path:

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
                <rule name="ReverseProxy_HomePage" enabled="true" stopProcessing="true">
                    <match url="^help$" />
                    <action type="Rewrite" url="https://example.document360.io/v1" />
                    <serverVariables>
                        <set name="HTTP_requested_by" value="proxy" />
                        <set name="HTTP_X_ORIGINAL_ACCEPT_ENCODING" value="{HTTP_ACCEPT_ENCODING}" />
                        <set name="HTTP_ACCEPT_ENCODING" value="" />
                    </serverVariables>
                </rule>
        <rule name="ReverseProxy_DocsPage" enabled="true" stopProcessing="true">
                    <match url="^help/(.*)" />
                    <action type="Rewrite" url="https://example.document360.io/help/{R:1}" />
                    <serverVariables>
                        <set name="HTTP_requested_by" value="proxy" />
                        <set name="HTTP_X_ORIGINAL_ACCEPT_ENCODING" value="{HTTP_ACCEPT_ENCODING}" />
                        <set name="HTTP_ACCEPT_ENCODING" value="" />
                    </serverVariables>
                </rule>
            </rules>
            <outboundRules>
                <rule name="RestoreAcceptEncoding" preCondition="NeedsRestoringAcceptEncoding">
                    <match serverVariable="HTTP_ACCEPT_ENCODING" pattern="^(.*)" />
                    <action type="Rewrite" value="{HTTP_X_ORIGINAL_ACCEPT_ENCODING}" />
                </rule>
        <rule name="RewriteLinksToSourceDomain1" preCondition="ResponseIsHtml">
                    <match filterByTags="None" pattern="^https://example.document360.io/(.*)" />
                    <action type="Rewrite" value="https://example.com/{R:1}" />
                </rule>
        <rule name="RewriteLinksToSourceDomain2" preCondition="ResponseIsHtml">
                    <match filterByTags="None" pattern="&quot;/help&quot;" />
                    <action type="Rewrite" value="&quot;/help&quot;" />
                </rule>
        <rule name="RewriteLinksToSourceDomain3" preCondition="ResponseIsHtml" patternSyntax="ECMAScript">
                    <match filterByTags="A" pattern="(.*)/docs/(.*)" />
                    <action type="Rewrite" value="/help/{R:2}" />
                </rule>
                <preConditions>
        <preCondition name="ResponseIsHtml">
                        <add input="{RESPONSE_CONTENT_TYPE}" pattern="^text/html" />
                    </preCondition>
                    <preCondition name="NeedsRestoringAcceptEncoding">
                        <add input="{HTTP_X_ORIGINAL_ACCEPT_ENCODING}" pattern=" .+" />
                    </preCondition>
                </preConditions>
            </outboundRules>
        </rewrite>
    </system.webServer>  
</configuration>
```

Backup `web.config` before changes.

> NOTE: KB Site 2.0 requires both Subfolder path and Site API path defined.

---

## What happens next?

Knowledge base goes live on custom subfolder.

Original URL still works.

Example: `example.document360.io` and `example.com/help` both point to same site.

Causes duplicate content in search engines. Enable redirect to prevent this.

> NOTE: Contact [support@document360.com](mailto:support@document360.com) for redirect setup.

---

### FAQs

**What is Internet Information Services (IIS)?**

Microsoft's flexible, secure web server for hosting websites and applications on Windows. Supports HTTP, HTTPS, FTP protocols.

**What is Application Request Routing (ARR) module?**

IIS extension enabling load balancing and request routing based on rules.

**What is URL Rewrite module in IIS?**

Module for modifying URLs and redirecting users seamlessly.

**Purpose of `web.config` file in IIS?**

Stores configuration settings like rewrite rules, security settings, and server behavior.

---

## Apache HTTP server

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Apache HTTP server is free, open-source, and highly customizable.

> NOTE: Replace example domains with your Document360 or custom domain.
> * Example domain: `example.document360.io`
> * Subdirectory: `example.document360.io/v1`
> * Homepage path: `example.document360.io/help`

---

### Setting up subfolder path

Enable these Apache modules:
* proxy
* proxy_http  
* headers
* substitute
* proxy_html

Enable with bash command:
`sudo a2enmod proxy proxy_http headers substitute proxy_html`

---

#### Homepage

Configure Virtual Host location blocks:

**Location Block** - Proxy requests where path starts with "/help":

```
<Location /help>
   ProxyPreserveHost off
   RequestHeader set Host example.document360.io
   RequestHeader set requested-by proxy
   RequestHeader unset Accept-Encoding
   ProxyPass https://example.document360.io/v1
   ProxyPassReverse https://example.document360.io/v1

   AddOutputFilterByType SUBSTITUTE text/html
   substitute 's|href="/docs|href="/help|ni'
   substitute 's|href="/v1/docs|href="/help|ni'
   substitute 's|href="https://example.document360.io/docs|href="https://docs.example.com/help|ni'
</Location>
```

**Redirect block for article preview links:**

Article preview links contain workspace/language slug.

Example:
* Article URL: `docs.example.com/getting-started`
* Preview: `docs.example.com/v1/en/getting-started`

Set redirect from `/v1/en` to `/`:

```
RewriteEngine on
RewriteRule ^v1/en$ / [R=301,L,NC]
```

Install rewrite module:
`sudo a2enmod rewrite`

---

#### Article/Category pages

**Location Block** - Proxy requests where path starts with "/help/":

```
<Location /help/>
   ProxyPreserveHost off
   RequestHeader set Host example.document360.io
   RequestHeader set requested-by proxy
   ProxyPass https://example.document360.io/docs/
   ProxyPassReverse https://example.document360.io/docs/

   AddOutputFilterByType SUBSTITUTE text/html
   substitute 's|href="/docs|href="/help|ni'
   substitute 's|href="/v1/docs|href="/help|ni'
   substitute 's|href="https://example.document360.io/docs|href="https://docs.example.com/help|ni'
</Location>
```

4. Restart Apache server:
`$ sudo systemctl restart apache2`

> NOTE: KB Site 2.0 requires both Subfolder path and Site API path defined.

---

## Sitemap generation

> NOTE: Replace example domain with your Document360 or custom domain.
> * Example: `example.document360.io`
> * Sitemap: `example.document360.io/sitemap.xml.en`

```
<Location /sitemap.xml.en>
    RequestHeader set Host example.document360.io;
    RequestHeader set requested-by proxy;
    ProxyPass https://example.document360.io/sitemap.xml.en;
    ProxyPassReverse https://example.document360.io/sitemap.xml.en;
</Location>
```

---

## What happens next?

Knowledge base goes live on custom subfolder.

Original URL still works.

Example: `example.document360.io` and `example.com/docs` both point to same site.

Causes duplicate content in search engines. Enable redirect to prevent this.

> NOTE: Contact [support@document360.com](mailto:support@document360.com) for redirect setup.

---

## Readers self-registration

**Plans supporting Readers self-registration**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

> NOTE: Self-registration only available when Knowledge base access is **Private** or **Mixed**.

---

### Reader self-registration

Users create reader accounts without invitations. Share knowledge base URL for independent signup.

Registered readers appear in **Readers** list. Project members with **User & Security** access can edit/remove readers.

---

### Self-register on Knowledge base site

1. Go to Knowledge base site
2. Click **Sign up** at login screen bottom

![Signup step](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/new%20account(1).png)

3. Enter **First name**, **Last name**, **Email**
4. Click **Sign up**

![Self signup page](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Self sign up.png)

Confirmation: "Account created successfully"

![Account created](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/New account created.png)

Receive invitation email. Verify, set password, and login.

> NOTE: Email verification required only once. Works across multiple projects.

---

### Accessing Reader self-registration option

1. Go to Settings > **Users & Security** > **Readers & groups**
2. Select **Reader self-registration** tab

![Self registration tab](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1731477666955.png)

3. If **Enable Self-Registration** toggle is off, page is empty
4. If toggle is on, options appear:

**Add to default reader group** (optional)

New readers automatically join selected default groups. Email domain mapping takes precedence.

To assign default reader group:
1. Click **Default Reader Group** field
2. Select one or more reader groups
3. Groups appear in field
4. Click 'X' to remove groups
5. Click **Save**

**Restrict registration by domain** (optional)

Allow or block self-registrations based on email domain.

* **Allow Specific Domains:** Restrict to organization employees. Example: `@examplecorp.com` with **Allow** status
* **Block Specific Domains:** Prevent unauthorized users. Example: `@genericmail.com` with **Block** status

---

### Adding domain restrictions

1. Go to Settings > **Users & Security** > **Readers & groups** > **Reader self-registration** tab
2. Scroll to **Domain Restriction** section
3. Enter domain in **Domain Name** field (e.g., `@genericmail.com`)
4. Select option:
   * **Allow (Whitelist)**: Permit specified domains, block others
   * **Block (Blacklist)**: Prevent specified domains, allow others

5. Assign reader groups to each domain:
   * Select groups from dropdown
   * Click 'X' to remove groups
   * Click **Save** to confirm
   * Click clear icon to clear line entries
   * Click **Remove** to delete line completely

6. Click **Add domain** for additional restrictions

> NOTE: Domain-specific settings override default reader groups.

---

### FAQs

**What happens if no default reader group selected?**

Self-registered readers get unrestricted access to entire knowledge base.

**What access do readers with multiple group memberships get?**

Highest level of access for each content item.

Example: Reader in Group A (all V1 languages) and Group B (V1 English only) gets access to all V1 languages.

**Does individual content access override group access?**

No. Reader gets highest privilege from both individual and group settings.

Example: Individual English-only V2 access plus group all-languages V2 access = all V2 languages.

**How is reader access prioritized?**

Highest privilege at each content level. Readers only access granted content.

**Why isn't self-registration working?**

SSO bypasses Document360 login page where self-registration occurs. Domain configuration only works on Document360 login page.

---

## Managing reviewer accounts

**Plans supporting reviewer role settings**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Reviewer role allows content review without editing. Access Documentation module to view articles/categories, add comments, update workflow status.

---

### Creating Reviewer account

1. Go to **Settings** > **Users & security** > **Team accounts & groups**
2. Click **Create** > **Team account**
3. Enter user email address
4. Select **Reviewer** from **Portal role** dropdown. Content role auto-sets to **Reviewer**
5. Or select other portal role and manually assign **Reviewer** content role
6. Assign content access permissions
7. Click **New team account**

![Create reviewer account](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Create_new_revieiwer_account.png)

---

### Bulk importing reviewers

1. Go to **Settings** > **Users & security** > **Team accounts & groups**
2. Select **Add** > **Import Team Accounts**
3. Select **Reviewer** account type
4. Check **SSO account** for SSO reviewers
5. Click **Download template**
6. Prepare CSV with user email addresses
7. Upload CSV file
8. Assign portal and content roles
9. Click **Import**

![Import reviewers](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_ScreenGIF-Importing_reviewer_roles.gif)

---

## Reviewer permissions and access

Documentation module access only. Permissions limited to reviewed content.

> NOTE: Reviewers can review one article at a time. Banner shows "Reviewer [Name] is currently reviewing the article."

Can:
* View articles in Draft mode or workflow state
* Add comments (inline included)
* Update workflow status
* Set due dates and manage assignments
* Bulk update workflow statuses from Workflow assignments page

> NOTE: Read-only workflow status blocks comments for all team accounts.

---

### Managing reviewer accounts

Update through **Team accounts & groups** section. Convert between Reviewer and Reader roles.

---

#### Edit or delete reviewer

1. Go to **Settings** > **Users & security** > **Team accounts & groups**
2. Find user, hover cursor, select **Edit** or **Delete**

---

#### Convert reviewer to reader

1. Go to **Settings** > **Users & security** > **Team accounts & groups**
2. Check user box
3. Click **Convert to reader**
4. Assign content access from **Content access** dropdown
5. Map to reader groups (optional)
6. Click **Confirm**

---

#### Purchasing reviewer accounts as add-ons

1. Go to **Settings** > **Knowledge base portal** > **Billing**
2. Click **Purchase add-on** in **My plan** tab
3. Add number of **Reviewer accounts** needed
4. Click **Confirm payment**

![Add reviewer accounts](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Adding_Reviewer_role_As_Add-ons_.png)

---

### Reviewer role functionality

Streamline content review without allowing edits. Access Draft articles for comments, suggestions, workflow updates.

---

#### Reviewing an article

1. Navigate to article from **Category & article** pane
2. Click **Start Review** at top right

To add comment:
1. Highlight text, click floating Comment icon
2. Enter comment, click **Post** or press **Ctrl+Enter**

When complete, click **Mark as Reviewed** at top right.

![Review article](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_GIF-Reviewing_an_article.gif)

To update workflow status:
1. Click Workflow status dropdown
2. Select status
3. Click **Set due date** icon, choose date
4. Click **Assign** icon, search team account
5. Click **Set status**

---

### FAQs

**How many reviewers included in each plan?**

* Professional: 5 Reviewers
* Business: 10 Reviewers
* Enterprise: 20 Reviewers

**Can reviewers edit articles?**

No. Comments and workflow updates only.

**Can reviewers access all articles?**

No. Only articles they have permission to review.

---

## Account locked

**Plans allowing password changes**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Account locked after 5 consecutive failed login attempts for 30 minutes.

Message: **Account locked due to multiple failed attempts! Please try again after 30 minutes.**

---

### Resetting password

1. Click **Forgot password?** on login page
2. Enter email address, click **Send**
3. Check inbox for reset email
4. Click **Reset Password** link
5. Enter new password, confirm it
6. Click **Reset**

> NOTE: Password changes apply to entire account, not specific projects.

![Account locked, forgot password](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Account_locked_forgot_password.png)

---

### New password requirements

* Minimum 8 characters
* At least 1 uppercase letter
* At least 1 lowercase letter  
* At least 1 number
* At least 1 special character

---

### Changing current password

Visit [Change password article](https://docs.document360.com/v3/docs/change-password) for instructions.

---

## Block inheritance

**Plans supporting block inheritance**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Restrict content access even with inherited permissions. Prevent users/teams from accessing content regardless of inherited rights.

---

### Content access at workspace level

Example: 6 inherited team accounts in workspace V1, want access for only 1 account plus yourself.

1. Go to **Settings** > **Users & Security** > **Content access**
2. Click workspace
3. Turn on **Block inherited account** toggle

Only accounts with direct content access display. Inherited accounts hidden.

![Block inheritance at workspace level](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_ScreenGif-Block_inheritance.gif)

---

### Disable inheritance for category or article

1. Go to Documentation, hover over category/article
2. Click **More** (•••) icon
3. Click **Security** > **Knowledge base portal** Access control
4. **Assign control access** panel appears
5. Turn on **Block inherited account** toggle
6. Only non-inherited accounts display
7. Click **Assign article access** for specific accounts
8. Select accounts, click **Apply**
9. Click **Close**

![Block inheritance at content level](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_ScreenGif-Block_inheritence.gif)

---

#### What happens after blocking inheritance?

Only listed accounts can access content level. Later add desired accounts to access list.

---

### Allow inheritance

Turn off **Block inherited account** toggle for inherited access.

---

#### Enable inheritance for category or article

1. Go to Documentation, hover over category/article
2. Click **More** (•••) icon
3. Click **Security** > **Knowledge base portal Access control**
4. **Assign control access** panel appears
5. Turn off **Block inherited account** toggle
6. Click **Yes** in **Allow inheritance** prompt
7. Click **Close**

![Enable inheritance](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_ScreenGif-Block_inheritance.gif)

---

### FAQs

**What happens when inheritance disabled?**

Only listed accounts can access that category or article.

**Is performing account automatically selected when blocking inheritance?**

Yes, and cannot be removed.## IP restriction

**Plans supporting IP restriction settings**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

**IP restriction** adds security by limiting access to specified IP addresses.

> NOTE
> 
> This setting applies to all workspaces and languages in the project.

Document360 supports **IPv4** and **IPv6** unicast addresses.

---

## IP restriction page

1. Navigate to Settings > **User & Security** > **IP restriction**
2. The IP restriction overview page appears

**Fields:**

* **Friendly name** - Identifier for the restriction (no character limit)
* **IP address** - Individual address or range (**IPv4** or **IPv6**)
* **Allow/Block** - Set restriction type
* **Remove** - Delete restriction using icon
* **Save** - Save restriction using icon

![IP restriction overview](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/54_ScreenShot-IP_restriction.png)

---

## Add IP restriction

1. Click **Add IP address**
2. Enter **Friendly name** (required)
3. Enter IP address or range

   Example: 79.15.135.189 - 79.15.135.229
4. Click **Save** icon
5. Click **Reset** icon to clear entries

![Add IP restriction](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/image-1725352385689.png)

New restrictions appear in the overview list.

**Alternative:** Click **Add my current IP address** to auto-fill your IP.

---

## Supported IPv6 formats

* 2001:0db8:85a3:0000:0000:8a2e:0370:7334  ✅
* 2001:0db8:85a3::8a2e:0370:7334  ❌
* 2001:db8:85a3:0:0:8a2e:370:7334  ✅

---

## Allow/Block IP addresses

* Select **Allow** for permitted IP addresses
* Select **Block** for restricted IP addresses

> NOTE
> 
> Duplicate IP entries trigger warning: '*A restriction with this IP address already exists*'

---

## Delete IP restriction

Click **Delete** icon next to the IP address.

Popup confirms: **IP restriction deleted**

> NOTE
> 
> Deleted restrictions cannot be recovered.

---

## FAQ

**What is an IP address?**

Numeric identifier for computers on a network. Enables internet communication.

**What is IPv4 format?**

Four numbers (0-255) separated by dots.

Example: 49.206.113.170

**What is IPv6 format?**

128-bit addresses in eight groups of hexadecimal digits separated by colons.

Example: FE38:DCE3:124C:C1A2:BA03:6745:EF1C:683D

* **Starting address**: 0000:0000:0000:0000:0000:0000:0000:0000
* **Ending address**: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff

**What is IPv6 unicast address?**

Identifies single network interface. Ensures point-to-point communication.

<a id="single-sign-on-sso"></a>

## Single Sign-On (SSO)

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

## What is SSO?

**Single Sign-On** authenticates users across multiple applications with one login.

Users access linked applications without re-entering credentials.

---

## Benefits of SSO

1. **Improved security** - Reduces credential storage locations
2. **Increased productivity** - Eliminates multiple login steps
3. **Better user experience** - Fewer password prompts
4. **Simplified IT management** - Centralized access control
5. **Compliance** - Meets regulatory requirements
6. **Reduced IT costs** - Minimizes authentication infrastructure

---

## How SSO works

Document360 (Service Provider) relies on external Identity Provider (IdP) for authentication:

1. User visits Document360 sign-in page
2. Redirected to IdP login page
3. User authenticates with IdP
4. IdP sends **Access token** or **ID token** to Document360
5. Document360 validates token
6. Trust relationship established

Successful authentication grants access to all SSO-enabled applications.

Document360 supports multiple IdP configurations simultaneously.

---

## What is an IdP?

Identity Provider stores user credentials and manages authentication for applications.

Each stored entity is a '**principal**'.

**Supported IdPs:**

* **Okta**
* **Entra ID**
* **Google**
* **ADFS**
* **OneLogin**

---

## SSO Standards

Document360 supports two protocols:

![SSO standards](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/sso_in_knowledge_base_Document360-1200x683.jpg)

### **SAML 2.0**

* [**Enabling SAML SSO**](https://docs.document360.com/docs/enabling-saml-sso)
* [**Removing SAML SSO**](https://docs.document360.com/docs/removing-a-configured-saml-sso)
* **Okta:** [**SAML with Okta**](https://docs.document360.com/docs/saml-sso-with-okta)
* **Entra ID:** [**SAML with Entra ID**](https://docs.document360.com/docs/saml-sso-with-entra)
* **Google:** [**SAML with Google**](https://docs.document360.com/docs/google-sso-saml-configuration)
* **OneLogin:** [**SAML with OneLogin**](https://docs.document360.com/docs/saml-sso-with-onelogin)
* **ADFS:** [**SAML with ADFS**](https://docs.document360.com/docs/saml-sso-with-adfs)
* **Other IdPs:** [**SAML with Other IdPs**](https://docs.document360.com/docs/saml-sso-with-other-configurations)

---

### **OpenId Connect**

* [**Enabling OpenID SSO**](https://docs.document360.com/docs/enabling-openid-sso)
* [**Removing OpenID SSO**](https://docs.document360.com/docs/removing-a-configured-openid-sso)
* **Okta:** [**OpenID with Okta**](https://docs.document360.com/docs/okta-with-openid-sso)
* **Auth0:** [**OpenID with Auth0**](https://docs.document360.com/docs/auth0-with-openid-sso)
* **ADFS:** [**OpenID with ADFS**](https://docs.document360.com/docs/adfs-with-openid-sso)
* **Other IdPs:** [**OpenID with Other IdPs**](https://docs.document360.com/docs/other-configurations-with-openid-sso)

Security Assertion Markup Language (SAML) enables secure authentication across multiple applications with single credentials.

<a id="login-using-sso-knowledge-base-portal"></a>

## Login using SSO - Knowledge base portal

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Access Document360 portal with existing IdP credentials. Eliminates separate password management.

---

## Logging in via SSO

1. Open browser and enter Document360 **Knowledge base portal** URL
2. Enter email address or domain name in **Email or Subdomain** field
3. Click **Continue with SSO**
4. Redirected to IdP login page
5. Authenticate with IdP credentials

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-KBportal_login_using_SSO.png)

Successful authentication logs you into Document360 portal.

---

## IdP initiated sign-in

When **Allow IdP initiated sign-in** is enabled during SSO setup:

1. Navigate to IdP dashboard
2. Locate Document360 application
3. Click application to initiate login

No need to visit Document360 portal first.

---

## Troubleshooting

### User access not assigned in IdP

**Error:** "Sorry, but we're having trouble signing you in. Your administrator has configured the application Document360 to block users unless specifically granted access."

User not assigned in IdP.

![Access error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Troubleshooting_user_access_not_assigned_idp.png)

**Solution:**

1. Log in to IdP portal
2. Navigate to **Applications**
3. Select Document360 application
4. Add required users or groups

---

### No projects associated with email

**Error:** "No projects associated with this email address. Contact Project administrator."

Account exists in IdP but not linked to Document360 project.

![No project error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Troubleshooting_no_project_associated.png)

**Solution:**

1. Log in to **Knowledge base portal** as administrator
2. Select project
3. Navigate to **Settings** > **Users & security** > **Team accounts & groups**
4. Check user account status:

   * If account exists but isn't SSO-enabled: Select checkbox > Click **Convert to SSO account**
   * If user not listed: Click **Add** > **Team account** > Check **SSO user** checkbox

---

### Missing email in SAML/ODIC response

**Error:** "Email address missing in SAML/ODIC response. Check SSO configuration or contact support."

Email/name attributes misconfigured in IdP. Case-sensitive fields.

![Missing email error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Troubleshooting_email_address_missing_in_saml_odic.png)

**Solution:**

**Check IdP attribute mapping**

1. Log in to IdP as administrator
2. Verify email/name attribute mapping
3. Confirm exact match with Document360 requirements:

   * Correct: "**email**" and "**name**"
   * Incorrect: "**Email**", "**EMAIL**", "**Name**", or "**NAME**"

**Update Document360 SSO configuration**

1. Log in to **Knowledge base portal** as administrator
2. Select project
3. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Edit** for existing configuration
5. In **IdP configurations** section, verify mapped attributes match IdP settings
6. Save updated configuration

Test login to confirm fix.

---

### SSO not enabled for email

**Error:** "Single sign-on isn't enabled for this email"

Email not properly configured in IdP or Document360.

**Solution:**

1. Log in to IdP portal
2. Navigate to **Applications**
3. Select Document360 application
4. Verify team accounts/readers added with proper permissions

Check Document360 SSO configuration using [**SAML**](/help/docs/saml) and [**OpenID**](/help/docs/openid) guides.

Contact [Document360 support](mailto:support@document360.com) with IdP and Document360 configuration screenshots if issue persists.

---

### Unable to login via SSO

**Error:** "Single Sign-on not enabled for this subdomain"

Incorrect subdomain or portal link used.

![Subdomain error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Troubleshooting_sso_not_enabled.png)

**Solution:**

**Verify subdomain and portal URL**

* US domain: [**https://portal.us.document360.io/**](https://portal.us.document360.io/)
* EU domain: [**https://portal.document360.io/**](https://portal.document360.io/)

**Check subdomain**

* Navigate to **Settings** > **Knowledge base portal** > **Custom domain**
* Project link shows subdomain (e.g., `https://test1.document360.io` = subdomain "**test1**")
* Also found on **Configure the Service Provider (SP)** page in SSO configuration

---

### SSO login failure

**Error:** "This page isn't working - identity.us.document360.io unable to handle request. HTTP ERROR 500."

Identity certificate changed. Signing certificates rotate every three months.

![HTTP 500 error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Troubleshooting_sso_http_error_500.png)

**Solution:**

1. Configure **metadata URL** correctly in IdP
2. Metadata URL available on Document360 **SSO page** - shows latest certificate information
3. Contact [**support@document360.com**](mailto:support@document360.com) if issue persists

---

## FAQ

#### Why can't I access project despite granted access?

You may be SSO user for some projects, non-SSO for others. Use correct login method.

Contact [support team](https://support.kovai.co/a/tickets/support@document360.com) if issue persists.

#### Why 500 error during SSO authentication?

Likely outdated SAML certificate. Check if site is public - SSO typically for secure access. Update SAML certificate.

<a id="login-using-sso-knowledge-base-site"></a>

## Login using SSO - Knowledge base site

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Access Document360 knowledge base site with existing IdP credentials.

---

## Logging in via SSO

1. Open browser and enter Document360 **Knowledge base site** URL
2. Select available SSO login button (e.g., "Login using Google")
3. Redirected to IdP login page
4. Authenticate with credentials

> NOTE
> 
> Available buttons depend on configured SSO providers.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-KBsite_login_using_SSO.png)

Successful authentication logs you into knowledge base site.

---

## IdP initiated sign-in

When **Allow IdP initiated sign-in** enabled during SSO setup:

1. Navigate to IdP dashboard
2. Locate Document360 application
3. Click application to initiate login

No need to visit Document360 site first.

<a id="inviting-or-adding-sso-users"></a>

## Inviting or Adding SSO users

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Once SSO configured (SAML or OpenID), users access projects with existing IdP credentials.

Benefits:
* Eliminates separate password management
* Simplifies login process

Options:
* **Add new team accounts as SSO users**
* **Invite existing users to SSO**

---

## Add new team account as SSO user

Process mirrors [adding regular team account](/help/docs/managing-team-account) with extra step.

1. Navigate to **Settings** > **Users & security** > **Team accounts & groups**
2. Click **Create** > **Team account**
3. In **Create team account** window > **Basic details**:
   * Add user email in **Email** field
   * Email must match domain in SSO configuration
4. Check **SSO user** checkbox
5. Select SSO configuration from **Select SSO** dropdown
6. Check **Skip invitation email** if preferred

Complete remaining steps per [adding team account](/help/docs/managing-team-account) guide.

> NOTE
> 
> Only **Owner** and **Admin** roles can add team accounts.

---

## Invite existing users

1. Log in to Document360
2. Navigate to project
3. Go to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Edit** icon for target SSO configuration
5. Navigate to **More settings** tab
6. In **Convert existing team and reader accounts to SSO** section:
   * **All users** - Invites all project users
   * **Selected users only** - Choose specific users from list
7. Click **Save**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Invite_users_to_SSO.png)

Team members receive invitation email with login details.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Invitation_email_sample.png)

> NOTE
> 
> Inviting existing user creates additional SSO account. Original team account remains.

---

## Delete SSO user

1. Log in to Document360
2. Navigate to project
3. Go to **Settings** > **Users & security** > **Team accounts & groups**
4. Click **Delete** icon for target account
   * SSO accounts identified by SSO label next to email
5. Confirm deletion in popup

> NOTE
> 
> Deleting SSO account doesn't remove associated team account.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Delete_SSO_user.png)

---

## FAQ

**Why can't I create SSO reader account?**

If user already exists as SSO reader, **Create reader account** button disables automatically when SSO checkbox checked.

<a id="mapping-an-existing-sso-configuration-to-other-projects"></a>

## Map existing SSO configuration to other projects

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Apply existing SSO configuration (SAML or OpenID) to other Document360 projects.

1. Log in to Document360
2. Navigate to target project
3. Go to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Create SSO**
5. Select appropriate identity provider
   * Must match existing SSO configuration IdP
6. Select SAML or OpenID
   * Must match existing SSO protocol
7. Select existing configuration from **Configure existing connection** dropdown
8. Complete setup in **More settings** page
9. Click **Create**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Select_existing_SSO_dropdown.png)

New configuration created based on selected existing setup.

<a id="disable-document360-login-page"></a>

## Disable Document360 login page

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Redirect users directly to SSO login when only SSO users exist.

> CAUTION
> 
> Don't disable if both SSO and regular team accounts exist. Regular accounts lose login access.

---

## Disable login page

1. Log in to Document360
2. Navigate to project
3. Go to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Settings** button (next to **Create SSO**)

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-SSO_settings_page_settings_button.png)

5. Toggle **ON** **Disable Document360 login page**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Disable_D360_login_page_toggle.png)

6. Click **Save**

Available for both SAML and OpenID configurations.

---

## FAQ

**Effect of disabling login page?**

Users see only SSO options. Email/password login unavailable.

<a id="auto-assign-reader-group"></a>

## Auto assign reader group

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Automatically grant access to readers who sign in via IdP. No manual invitations required.

---

## Auto assign SSO readers

1. Log in to Document360
2. Navigate to project
3. Go to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Edit** icon for target SSO configuration
5. Navigate to **More settings** tab
6. Toggle **ON** **Auto assign reader group**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Auto_assign_reader_groups_toggle.png)

7. Select reader groups for auto-assignment
8. Click **Save**

> NOTE
> 
> Requires existing reader groups. Create via **Settings** > **Users & security** > **Reader & groups** > **Reader groups**

<a id="convert-to-sso-account"></a>

## Convert to SSO account

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

## Convert Document360 account to SSO

Single Sign-On authenticates users across multiple applications with one login.

Convert existing accounts to SSO without changing roles/access.

> NOTE
> 
> Only available for SAML and OpenID configured projects.

---

## Convert team accounts to SSO

1. Navigate to **Settings** > **Users & Security** > **Team accounts & groups** > **Team account**
2. Select target account checkboxes
3. Click **Convert to SSO account**

![Convert team accounts](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/39_ScreenShot-SSO_conversion.png)

4. **Account convert** popup appears
5. Check box and click **Yes**

![Confirm conversion](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/40_ScreenShot-SSO_conversion.png)

> NOTE
> 
> * User contributions retained but previous activity shows as **Anonymous**
> * Cannot convert own account
> * Converting owner account creates duplicate - both regular and SSO accounts remain

---

## Convert readers to SSO

1. Navigate to **Settings** > **Users & Security** > **Readers & groups** > **Readers**
2. Select target reader checkboxes
3. Click **Convert to SSO account**

![Convert readers](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/41_ScreenShot-SSO_conversion.png)

4. **Account convert** popup appears
5. Check box and click **Proceed**

![Confirm reader conversion](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/42_ScreenShot-SSO_conversion.png)

> NOTE
> 
> SSO accounts cannot convert back to regular Document360 accounts.

---

## FAQ

**Who can convert accounts?**

**Owner**, **Admin**, or team accounts with **Manage team accounts** permission.

**Can convert in JWT projects?**

No. Only SAML and OpenID configured projects.

**Mistakenly converted accounts?**

No direct reversal. Delete SSO account and manually recreate regular account. Replicate roles/access.

<a id="team-account-idle-timeout"></a>

## Sign out idle SSO team account

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Automatically log out inactive SSO team accounts for enhanced security.

Account considered idle after predefined inactivity period.

Applies only to SAML and OpenID configurations.

---

## Enable idle sign out

1. Navigate to **Settings** > **Users & Security** > **SAML/OpenID**
2. Click **Edit** icon for existing SSO configuration
3. Go to **More settings** tab
4. Toggle **ON** **Sign out idle SSO team account**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Sign_out_idle_SSO_team_account(1).png)

5. Enter timeout duration in **hours:minutes** format
6. Click **Save**

> NOTE
> 
> Only affects SSO team accounts. Regular Document360 accounts unaffected.

---

## FAQ

**What happens after idle logout?**

User must re-authenticate to access Knowledge Base portal.

**Default timeout duration?**

2 hours. Configurable per project requirements.

<a id="saml"></a>

## SAML

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

**SAML 2.0** enables single credentials access to multiple web applications.

Secure, convenient Document360 access via existing IdP credentials.

Supports multiple SSO endpoints for team accounts and readers.

---

## Supported IdPs

* **Okta**
* **Entra ID**
* **Google**
* **Auth0**
* **ADFS**
* **OneLogin**
* **Others**

---

## Configure SAML SSO

1. Log in to Document360
2. Navigate to project
3. Go to **Settings** > **Users & security** > **SAML/OpenID**
4. Click **Create SSO**
5. Select identity provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Create_SSO_Choose_idp_page.png)

6. Select **SAML** protocol
7. Use **Configure the Service Provider (SP)** details to set up application in IdP

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-SSO_configuration_configure_sp.png)

8. Use IdP details to complete Document360 configuration

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-SSO_configuration_configure_idp.png)

9. Click **Create**

Users can now login via SSO or email/password.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-SSO_configuration_document360_login_page.png)

---

## Troubleshooting

### Invalid SAML request (Untrusted key)

**Error:** "Invalid SAML Request - SAML signature valid but uses untrusted key"

Inactive SAML certificate uploaded to Document360.

![Untrusted key error](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Troubleshooting_issue_untrusted_key.png)

**Solution:**

**Download active certificate**

1. Access IdP
2. Download current active SAML certificate

**Re-upload in Document360**

1. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
2. Click **Edit** for relevant SSO configuration
3. Locate **SAML Certificate** field under **Configure the Identity Provider (IdP)**
4. Click **Browse** to upload new active certificate

---

### SAML message signature invalid

**Error:**

* "SignatureInvalid: SAML message signature invalid"
* "AssertionSignatureInvalid: SAML Assertion signature invalid"
* "Invalid SAML Request: SAML signature valid but uses untrusted key"

Incorrect or expired SAML certificate in Document360.

**Solution:**

**Verify certificate validity**

1. Check uploaded certificate is active and unexpired
2. Generate new certificate in IdP if needed

**Re-upload correct certificate**

1. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
2. Click **Edit** for relevant SSO configuration
3. Locate **SAML Certificate** field under **Configure the Identity Provider (IdP)**
4. Click **Browse** to upload new active certificate

**Capture logs if issue persists**

1. Install [**SAML Tracer**](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/) browser extension
2. Open SAML Tracer before SSO login
3. Trigger SSO process
4. Right-click in SAML Tracer window
5. Select **Export** or save logs

Contact [**Document360 support**](mailto:support@document360.io) with:
* IdP configuration screenshots
* Uploaded SAML certificate details
* SAML Tracer logs

<a id="saml-sso-with-okta"></a>

## SAML SSO with Okta

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

**Okta** simplifies access management with single credentials for multiple applications.

This guide configures SSO between Okta and Document360.

> PRO TIP
> 
> Open Document360 and Okta in separate tabs for easier configuration switching.

---

## Okta setup

### Sign up

1. Navigate to <https://developer.okta.com/signup/>
2. Complete registration
3. Check email for credentials and activation link
4. Click activation link
5. Log in to Okta Domain
6. Redirected to Okta developer console

---

## Add Okta application

1. Log in to Okta with admin credentials
2. Click **Admin** (top right)
3. Expand **Applications** > Click **Applications**
4. Click **Create App Integration**
5. Select **SAML 2.0** as sign-in method
6. Click **Next**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_GIF-Okta_create_app_integration.gif)

---

## Create SAML integration

### General settings

1. Enter application name in **App name** field
2. Upload logo if required
3. Set app visibility
4. Click **Next**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Okta_general_settings.png)

### Configure SAML

Get Document360 parameters:

1. Navigate to **Settings** > **Users & security** > **SAML/OpenID** in Document360
2. Click **Create SSO**
3. Select **Okta** as Identity Provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Choose_idp_okta.png)

4. **Configure the Service Provider (SP)** page shows required parameters

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Okta_document360_parameters.png)

**Mapping:**

| Document360 | Okta |
| --- | --- |
| Callback path | Single sign-on URL |
| Service provider entity id | Audience URI (SP Entity ID) |

5. Enter Document360 parameters in Okta fields
6. Select **EmailAddress** from **Name ID format** dropdown
7. Select **Email** from **Application username** dropdown
8. Configure **Attribute Statements**:

| **Name** | **Name format** | **Value** |
| --- | --- | --- |
| urn:oasis:names:tc:SAML:2.0:nameid | URI Reference | user.email |
| name | Unspecified | user.email |
| email | Unspecified | user.email |

> NOTE
> 
> Email and name parameters are case-sensitive

9. Click **Next**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Okta_configure_saml.png)

### Feedback

1. Select **This is an internal app that we have created**
2. Click **Finish**

---

## Okta to Document360 configuration

### Get Okta parameters

1. In Okta dashboard > **Applications** > **Applications**
2. Select active application
3. Click **Sign On** tab
4. Click **View SAML setup instructions**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_GIF-Okta_app_signon_setup_instructions.gif)

Parameters appear in new window:

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Okta_setup_instructions_page.png)

### Configure Document360

1. Return to Document360 **Configure the Service Provider (SP)** page
2. Click **Next** to **Configure the Identity Provider (IdP)** page
3. Enter Okta parameters:

| Document360 | Okta |
| --- | --- |
| Sign on URL | Identity Provider Single Sign-On URL |
| Entity ID | Identity Provider Issuer |
| SAML certificate | X.509 Certificate |

4. Download **X.509 Certificate** from Okta
5. Upload **okta.cert** file to Document360 **SAML certificate** field
6. Toggle **Allow IdP initiated sign in** per project requirements

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Okta_document360_configuration.png)

7. Click **Next** to **More settings** page
8. Enter **SSO name**
9. Enter **Customize login button** text
10. Configure **Auto assign reader group** and **Sign out idle SSO team account** toggles
11. Invite users via **Convert existing team and reader accounts to SSO**
12. Click **Create**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Okta_document360_configuration_save.png)

SSO configuration complete.

<a id="saml-sso-with-entra"></a>

## SAML SSO with Entra

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure Document360 **SAML Single Sign-On** with **Microsoft Entra**.

> PRO TIP
> 
> Open Document360 and Entra in separate tabs for easier configuration switching.

---

## Add Azure application

### Access Azure AD portal

1. Log in to Microsoft Azure account
2. Click **Portal** (top-right)
3. Redirected to Azure portal (<https://portal.azure.com/#home>)

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Image_2-ScreenGIF-Azure_Active_Directory_Portal_access.gif)

### Add application

1. Click **+ New application**
2. Select **Non-gallery application**
3. Enter application name
4. Click **Add**
5. In **Getting started** section > Select **Set up single on**
6. Choose **SAML** option
7. Refer to [**Azure AD configuration guide**](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-setup-sso) for detailed walkthrough

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Image_3-ScreenGIF-Azure_Active_Directory_adding_new_application.gif)

---

## Configure SAML in Entra

1. Open Document360 in separate tab
2. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
3. Click **Create SSO**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Settings_create_sso(2).png)

4. Select **Entra ID** as Identity Provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Choose_idp_entra.png)

5. **Configure the Service Provider (SP)** page shows required parameters

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Configure_sp_saml_generic.png)

**Mapping:**

| Azure AD fields | Document360 portal |
| --- | --- |
| Identifier (Entity ID) | Service provider entity id |
| Reply URL (Assertion Consumer Service URL) | Callback path |
| Sign on URL | https://identity.document360.io |
| Logout URL | Signed out callback path |

6. Copy parameters from Document360
7. In Azure AD **Set up Sign-On with SAML** page > Click **Edit** icon
8. Paste data in corresponding fields
9. Click **Save**

![Azure AD SAML configurations](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Image_4-Screenshot-Azure_AD_SAML_configurations.jpg)

---

## Document360 configuration

1. Return to Document360 **Configure the Service Provider (SP)** page
2. Click **Next** to **Configure the Identity Provider (IdP)** page
3. Enter Azure AD parameters:

| Document360 portal fields | Azure AD portal values |
| --- | --- |
| Sign On URL | Login URL |
| Entity ID | Azure AD identifier |
| Sign Out URL | Logout URL |
| SAML Certificate | Download Certificate (Base64) from Azure AD and upload |

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Configure_idp_saml_generic.png)

4. Toggle **Allow IdP initiated sign in** per requirements
5. Click **Next** to **More settings** page

---

## More settings

Configure:

* **SSO name** - Configuration identifier
* **Customize login button** - User-facing button text
* **Auto assign reader group** - Toggle as needed
* **Sign out idle SSO team account** - Toggle per requirements
* **Convert existing team and reader accounts to SSO** - Choose invite method

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Create_SSO_more_settings_generic(2).png)

6. Click **Create**

---

## Additional Azure AD settings

1. Edit **User Attributes & Claims** section
2. **Add new claim** or **Add group claim**
3. In **SAML signing certificate** section:
   * Add **New certificates**
   * **Import certificates**
4. Add multiple notification email addresses
5. Click **Test** option
6. Log in to Document360 with registered user credentials

<a id="google-sso-saml-configuration"></a>

## SAML SSO with Google

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure **Google SAML Single Sign-On** with **Google Workspace**.

> PRO TIP
> 
> Open Document360 and Google Workspace in separate tabs for easier configuration switching.

---

## Add Google SAML app

1. In admin console > Click **Apps** > Select **SAML apps**
2. Click **Add app** > Select **Add custom SAML app**
3. Enter app name in **App details**
4. Click **Continue**
5. Note **SSO URL**, **Entity ID**, and **Certificate** details
6. In Certificate section > Click Download icon to save certificate (.pem format)
7. Upload this certificate later in Document360 **Configure the Identity Provider (IdP)** page

![Google certificate](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/41_Screenshot-Google-user-access-service-status.jpg)

8. In **User access** > Change **Service status** from **OFF for everyone** to **ON for everyone**

![Google service status](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/42_Screenshot-Google-user-access-changing-service-status.jpg)

---

## Service Provider configuration

Get Document360 SP details:

1. Navigate to **Settings** > **Users & Security** > **SAML/OpenID**
2. Click **Create SSO**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Settings_create_sso(2).png)

3. Select **Google** as Identity Provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Choose_idp_google.png)

4. From **Configure the Service Provider (SP)** page > Copy parameters:

| Google custom SAML app | Document360 SSO SAML settings |
| --- | --- |
| ACS URL | Callback path |
| Entity ID | Service provider entity Id |
| Start URL (optional) |  |

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Configure_sp_saml_generic.png)

5. Switch to Google Workspace tab > Paste parameters
6. In **Name ID format** > Select **EMAIL**
7. In **Name ID** > Select **Basic Information > Primary email**
8. Click **Continue**

---

## Attributes mapping

Map Google Directory attributes to app attributes:

| Google Directory attributes | App attributes |
| --- | --- |
| Primary email | name |
| Primary email | email |
| Primary email | urn:oasis:names:tc:SAML:2.0:nameid |

Click **Add Mapping** for each attribute > Click **Finish**

---

## Identity Provider configuration

1. Return to Document360 **Configure the Service Provider (SP)** page
2. Click **Next** to **Configure the Identity Provider (IdP)** page
3. Enter Google parameters:

| Document360 SSO settings | Info from Google custom SAML app |
| --- | --- |
| Sign on URL | SSO URL |
| Entity id | Entity ID |
| Sign Out URL (Optional) | NA |
| SAML Certificate | Upload recent .pem file downloaded from Google |

4. Toggle **Allow IdP initiated sign in** per requirements

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Okta_document360_configuration.png)

5. Click **Next** to **More settings** page
6. Enter **SSO name**
7. Enter **Customize login button** text
8. Configure **Auto assign reader group** and **Sign out idle SSO team account** toggles
9. Invite users via **Convert existing team and reader accounts to SSO**
10. Click **Create**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Create_SSO_more_settings_generic.png)

SSO configuration complete.

<a id="saml-sso-with-onelogin"></a>

## SAML SSO with OneLogin

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure Document360 SSO using OneLogin as Identity Provider.

> PRO TIP
> 
> Open Document360 and OneLogin in separate tabs for easier configuration switching.

---

## Add OneLogin application

1. Log in to OneLogin Admin Portal
2. Select **Applications** (top menu)
3. Click **Add App**
4. Search "SAML" > Select **SAML Custom Connector (Advanced)**
5. Name application (e.g., "Document360 SSO")
6. Click **Save**

---

## Configure SAML in OneLogin

1. Open Document360 in separate tab
2. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
3. Click **Create SSO**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Settings_create_sso(2).png)

4. Select **OneLogin** as Identity Provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Choose_idp_onelogin.png)

5. **Configure the Service Provider (SP)** page shows required parameters

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Configure_sp_saml_generic.png)

6. Switch to OneLogin tab > Navigate to **Configuration** tab
7. Enter Document360 parameters:

| OneLogin | Document360 |
| --- | --- |
| Audience (EntityID) | Service provider entity id |
| Recipient | Callback path |
| ACS (Consumer) URL Validator | Callback path |
| ACS (Consumer) URL | Callback path |

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Configuration_tab.png)

8. Click **Save**
9. Navigate to **Parameters** tab > Click + icon
10. Configure parameters:

| Field Name | Value |
| --- | --- |
| urn:oasis:names:tc:SAML:2.0:nameid | Email |
| email | Email |
| name | Email |

> NOTE
> 
> Check **Include in SAML assertion** for each parameter

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Parameters_tab.png)

11. Click **Save**
12. Navigate to **SSO** tab > Click **View Details**
13. Download **X.509 Certificate**
14. Copy **Issuer URL** and **SAML 2.0 Endpoint (HTTP)**

> NOTE
> 
> Select **SHA256** from **SHA fingerprint** dropdown
> Select download format as **X.509.PEM**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-SSO_tab.png)

---

## Document360 configuration

1. Return to Document360 **Configure the Service Provider (SP)** page
2. Click **Next** to **Configure the Identity Provider (IdP)** page
3. Enter parameters:

| **Identity Provider** | **Document360** |
| --- | --- |
| Issuer URL | Entity id |
| SAML 2.0 Endpoint (HTTP) | Sign on URL |
| Downloaded SAML Certificate (X.509) | SAML Certificate |

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Configure_idp_saml_generic.png)

4. Toggle **Allow IdP initiated sign in** per requirements
5. Click **Next** to **More settings** page

---

## More settings

Configure:

* **SSO name** - Configuration identifier
* **Customize login button** - User-facing button text
* **Auto assign reader group** - Toggle as needed
* **Sign out idle SSO team account** - Toggle per requirements
* **Convert existing team and reader accounts to SSO** - Choose invite method

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Create_SSO_more_settings_generic(2).png)

6. Click **Create**

<a id="saml-sso-with-adfs"></a>

## SAML SSO with ADFS

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure Document360 SSO with ADFS using SAML protocol.

> PRO TIP
> 
> Open Document360 and ADFS in separate tabs for easier configuration switching.

---

## Add ADFS application

1. Log in to ADFS Management console
2. Navigate to **Relying Party Trusts**
3. Right-click > Select **Add Relying Party Trust**
4. Choose **Claims aware** > Click **Start**
5. Select **Enter data about the relying party manually** > Click **Next**
6. Provide display name (e.g., "Document360 SAML SSO") > Click **Next**
7. **Configure Certificate** step > Click **Next** (skip if not using certificate)
8. Under **Configure URL** > Select **Enable support for the SAML 2.0 WebSSO protocol**

---

## Document360 Service Provider configuration

1. Open Document360 in separate tab
2. Navigate to **Settings** > **Users & security** > **SAML/OpenID**
3. Click **Create SSO**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Settings_create_sso(2).png)

4. Select **ADFS** as Identity Provider

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/9_Screenshot-Choose_idp_adfs(1).png)

5. Choose **SAML** protocol on **Configure the Service Provider (SP)** page
6. Note parameters:

* **Subdomain name** - Unique Document360 instance identifier
* **Callback path** - Post-sign-in redirect URI
* **Signed out callback path** - Post-sign-out redirect URI
* **Metadata path** - SAML metadata URL
* **Service provider entity ID** - Document360 service provider identifier

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Configure_sp_saml_generic.png)

7. Enter parameters in ADFS:

* **Relying Party Identifier** - Use Document360 **Service provider entity ID**
* **Sign-On URL** - Enter Document360 **Callback path**
* **Sign-Out URL** - Enter Document360 **Signed out callback path**
* **Relying Party Trust Identifier** - Use Document360 **Subdomain name**
* **Metadata URL** - Enter Document360 **Metadata path**

8. Click **Next** > Complete wizard steps
9. Review settings > Click **Next** to add relying party trust
10. Check **Open the Edit Claim Rules dialog** > Click **Close**

---

## Configure Claim Rules

1. In **Edit Claim Rules** dialog > Click **Add Rule**
2. Select **Send LDAP Attributes as Claims** > Click **Next**
3. Name claim rule (e.g., "Send LDAP Attributes")
4. Configure:

* **Attribute Store** - Select **Active Directory**
* **Mapping**:
  + **LDAP Attribute**: User-Principal-Name | **Outgoing Claim Type**: Name ID
  + **LDAP Attribute**: E-Mail-Addresses | **Outgoing Claim Type**: Email
  + **LDAP Attribute**: Display-Name | **Outgoing Claim Type**: Name

5. Click **Finish** > **Apply** > Close dialog

---

## Document360 SAML configuration

1. Return to Document360 **Configure the Service Provider (SP)** page
2. Click **Next** to **Configure the Identity Provider (IdP)** page
3. Enter ADFS parameters:

| **ADFS** | **Document360** |
| --- | --- |
| SAML Sign-On URL | Identity Provider Single Sign-On URL |
| Identifier (Entity ID) | Identity Provider Issuer |
| X.509 Certificate | SAML Certificate |

4. Download X.509 Certificate from ADFS
5. Upload to Document360 **SAML Certificate** field
6. Toggle **Allow IdP initiated sign in** per requirements

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Configure_idp_saml_generic.png)

7. Click **Next** to **More settings** page

---

## More settings

Configure:

* **SSO name** - Configuration identifier
* **Customize login button** - User-facing button text
* **Auto assign reader group** - Toggle as needed
* **Sign out idle SSO team account** - Toggle per requirements

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Create_SSO_more_settings_generic(2).png)

8. Click **Create**

<a id="saml-sso-with-other-configurations"></a>

## SAML SSO with other configurations

**Plans supporting SSO**

| Professional | Business | Enterprise |
| --- | --- | --- |
|  |  |  |

Configure Document360 SSO with any unsupported Identity Provider.

> PRO TIP
> 
> Open Document360 and IdP in separate tabs for easier configuration switching.

---

## Add IdP application

1. Log in to IdP admin console
2. Locate application management section (typically **Applications** or **Enterprise Applications**)
3. Select option to create new application
4. Configure basic settings:

* **Application Name** - e.g., "Document360 SSO"
* **Application Type** - Select **SAML 2.0** sign-in method

5. Save application settings

Continue with standard SAML configuration process using Document360 parameters.## Configure IdP SAML settings

Next, configure SAML in your Identity Provider using Document360 parameters:

1. Open Document360 in a separate tab
2. Navigate to **Settings > Users & security > SAML/OpenID**
3. Click **Create SSO**

![Create SSO button](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/5_Screenshot-Settings_create_sso(2).png)

4. Select **Others** as your Identity Provider to automatically navigate to the **Configure the Service Provider (SP)** page

![Choose Others IdP](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Choose_idp_others(1).png)

5. On the **Configure the Service Provider (SP)** page, find the parameters needed for your IdP SAML configuration:

In your Identity Provider's SAML configuration, enter:

* **Single Sign-On URL** - Use the **Callback path** from Document360
* **Entity ID** - Use the **Service provider entity ID** from Document360  
* **Audience URI** - Typically the **Service provider entity ID** or **Single Sign-On URL** from Document360

![SP configuration parameters](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_Screenshot-Configure_sp_saml_generic.png)

### Attribute mapping

Configure attribute statements in your IdP:

| Attribute Name | Value |
| --- | --- |
| NameID | user.email or user ID |
| email | user.email |
| name | user.name |

Case sensitivity may matter depending on your IdP.

### Additional IdP requirements

Some Identity Providers require extra configuration details. Review and save your SAML settings in the IdP before proceeding.

## Document360 SSO setup

Complete the SSO configuration in Document360:

1. Return to Document360 and click **Next** on the **Configure the Service Provider (SP)** page
2. Enter values from your Identity Provider on the **Configure the Identity Provider (IdP)** page:

| Document360 Field | Identity Provider Value |
| --- | --- |
| Single Sign-On URL | Identity Provider Single Sign-On URL |
| Entity ID | Identity Provider Issuer |
| SAML Certificate (X.509) | SAML Certificate |

3. Download the X.509 Certificate from your IdP and upload it to Document360
4. Toggle **Allow IdP initiated sign in** based on project requirements

![IdP configuration](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_Screenshot-Configure_idp_saml_generic.png)

5. Click **Next** to proceed to **More settings**

### More settings configuration

Configure these final options:

* **SSO name** - Name for this SSO configuration
* **Customize login button** - Text displayed on login button
* **Auto assign reader group** - Toggle as needed
* **Sign out idle SSO team account** - Toggle based on requirements
* Choose whether to invite existing team and reader accounts to SSO

![More settings page](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/10_Screenshot-Create_SSO_more_settings_generic(2).png)

6. Click **Create** to complete SSO setup

Your SSO configuration is now active using your selected Identity Provider.## Add-ons

Document360 offers various add-ons to extend your plan's capabilities. These can be purchased at any time to enhance specific features or increase limits.

### Available add-ons

| Add-on | Description | Available in plans |
| --- | --- | --- |
| **Additional projects** | Create more knowledge base projects beyond your plan's default limit | Professional, Business, Enterprise |
| **Additional workspaces** | Add extra workspaces to organize content better | Professional, Business, Enterprise |
| **Additional languages** | Increase the number of languages supported | Professional, Business, Enterprise |
| **Translation credits** | Purchase additional machine translation characters (1 million per credit) | Professional, Business, Enterprise |
| **Additional storage** | Extend your Drive storage capacity | Professional, Business, Enterprise |
| **Additional team accounts** | Add more team members beyond your plan's default limit | Professional, Business, Enterprise |
| **Additional reader accounts** | Increase the number of reader accounts | Professional, Business, Enterprise |

### Purchasing add-ons

1. Navigate to **Settings** () > **Knowledge base portal** > **Billing**
2. In the **My plan** tab, click **Purchase add-on**
3. Select the desired add-on from the list
4. Choose the quantity you need
5. Click **Add to cart** and complete the checkout process

> NOTE
>
> Add-ons are billed separately from your main subscription and may have different billing cycles. Check your invoice for details.

### Managing add-ons

From the **Billing** page, you can view your current add-ons under the **My plan** tab. Add-ons can be modified or removed at any time:

* To **modify** an add-on: Click the **•••** menu next to the add-on and select **Edit**
* To **remove** an add-on: Click the **•••** menu next to the add-on and select **Remove**

> WARNING
>
> Removing add-ons may affect your knowledge base functionality if you're using features that exceed your base plan limits.## Purchasing add-ons

### Available add-ons by plan

Document360 scales with your projects through add-ons that enhance documentation capabilities. The **Professional**, **Business**, and **Enterprise** plans support:

* **Workspaces**
* **Languages**
* **Translation credits (1 million characters)**
* **Storage (1 unit = 50 GB)**
* **Team accounts**
* **Readers (1 unit = 5000 readers)**
* **PDF export limit (1 unit = 2GB)**

**Business** plan users can also purchase:

* **Crowdin extension**
* **Phrase extension**

**Enterprise** plan users gain access to:

* **Salesforce extension**
* **Additional sandbox environment**

These add-ons provide flexibility in knowledge base configuration.

> NOTE
>
> To purchase add-ons, save a card in your Document360 account. Add a card via **Settings ()** > **Knowledge base portal** > **Billing** > **Payment information** tab.

---

### Purchasing add-ons

To purchase add-ons:

1. From the knowledge base portal, go to **Settings ()** > **Knowledge base portal** > **Billing**

![Billing page](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Billing_page_purchase_addon_button.png)

2. In the **My plan** tab, click **Purchase add-on**

![Purchase add-ons](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Billing_page_purchase_addon_details.png)

3. Select required add-ons using + and - buttons
4. Click **Confirm payment**

> NOTE
>
> Legacy plan customers can only purchase: Projects, Workspaces, Languages, Translation Credits, Storage, Team Accounts, and Readers. Online customers access this feature directly; offline customers contact support.

<a id="upgrading-from-trial-version"></a>

## Upgrading from trial version

Document360 provides a 14-day trial period with full access to all plan features. Switch between plans during trial to evaluate capabilities. Upgrade anytime during or after trial.

> NOTE
>
> Only project **Owner(s)** can access **Billing** features.

---

## Changing your plan during the trial period

Switch plans during the 14-day trial to explore different tiers. Start with **Enterprise** to test advanced features, then switch to lower-tier plans to understand cost-effective options. All changes are free during trial.

From the Knowledge base portal, navigate to **Settings ()** > **Knowledge base portal** > **Billing**. View current plan, remaining trial time, and feature summaries.

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/2_Screenshot-Trial_plan_billing_screen.png)

To change plans during trial:

1. Click the dropdown on the **TRIAL ENDS IN N DAYS** button
2. Select **Try other plans** to open the **Change plan** page
3. Click **Try now** under the desired plan

> NOTE
>
> Selecting a lower-tier plan shows features you'll lose access to.

4. If moving to:
   * **Lower tier**: Check the box to proceed with downgrading and deleting unavailable configurations, then click **Change plan**
   * **Higher tier**: Receive success message after upgrade

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/3_GIF-Trial_plan_try_other_plans.gif)

> NOTE
>
> From the dropdown, you can also:
> * Click **Buy now** to subscribe
> * Click **Book a demo** to schedule demonstration
> * Click **Chat with us** to contact support

---

## Subscribing to a Document360 plan

To subscribe during or after trial:

1. From the Knowledge base portal, go to **Settings ()** > **Knowledge base portal** > **Billing**
   
   View plan features and remaining trial days.

2. Click **Buy now** to access the **Upgrade** page. See available plans and costs. Scroll to **Compare plans & features** for detailed feature lists.

3. Select preferred plan and click **Let's talk**

![](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/4_GIF-Trial_plan_buy_plans.gif)

Document360 sales will contact you to complete the subscription.

## FAQs

**What features are available during the trial period?**

Full access to all Document360 features and plans.

**Will I lose my data if I downgrade during the trial?**

No data loss, but features and limits (workspaces, readers, storage) adjust to the lower plan.

**Can I extend my trial period?**

Possibly. Contact support to discuss extension options.

**What happens when my trial ends?**

Subscribe to continue using features. Without subscription, projects pause then delete automatically. You'll receive warnings before deletion.

**Are there limitations during trial compared to paid plans?**

No. Trial provides identical access to paid plans.

**What if I need help during trial?**

Use chat, book a demo, or contact support directly.

**Will I be charged automatically after trial?**

No. Manual subscription required before trial expires.

**Does pricing vary by currency?**

Yes. Select currency to view local pricing.

**Does pricing change with exchange rates?**

Pricing remains fixed. Changes occur only during scheduled updates, with advance notification via email.

<a id="changing-payment-information"></a>

## Changing payment information

## How to change payment information

![1_Screenshot-changing_the_payment_information](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/Payment information - new.png)

NOTE

Only team accounts with owner access can modify billing settings.

1. From the Knowledge base portal, go to **Settings** > **Billing**
2. Navigate to **Payment information** tab (My plan opens by default)
3. Below **Credit card** tile, change payment method and billing address
   
   View primary card details.

4. Click **Add another card** to include secondary payment method

NOTE

Primary card handles billing. If primary card fails, secondary card processes renewal.

---

## FAQs

**How can I delete my primary payment card?**

Cannot delete primary card. Can edit card details. Secondary cards can be edited or deleted.

**How can I delete my secondary card?**

1. Go to **Settings** > **Billing** > **Payment information**
2. Hover over secondary card
3. Click **Delete** icon, then confirm in popup

**How can I set secondary card as primary?**

1. Go to **Settings** > **Billing** > **Payment information**
2. Hover over secondary card
3. Select **Set as primary** radio button
4. Click **Make Primary** in confirmation popup

**How do I edit my primary card?**

1. Go to **Settings** > **Billing** > **Payment information**
2. Hover over primary card
3. Click **Edit** icon to update details
4. Click **Update** to save changes

The knowledge base portal where project members manage and create content. Users create categories, articles, and templates; manage files, team accounts, and readers; configure branding, domain, and security settings.

<a id="february-2025-1112"></a>## March 2022

---

## Enhancements

### 1. Image formatting in Advanced WYSIWYG editor

In the Advanced WYSIWYG editor, you can now specify image dimensions using percentages for both width and height.

![7_Screenshot-UpdatedImage_percentage](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-%28Updated%29Image_percentage.png)

---

## Improvements

Minor security updates, bug fixes, and performance improvements were implemented in both the Knowledge base portal and Knowledge base site.

Application Programming Interface - A set of rules that allows one software application to communicate with another.

<a id="february-2024"></a>

## February 2024

Document360 released another monthly update in February 2024. Here are the enhancements and improvements made to the Document360 knowledge base.## New features

### 1. Shared articles

This feature was added to Document360 based on popular customer requests. The **Shared article** feature lets you display one article in multiple categories. Shared articles are termed as **References**.

* Use the ••• **More option** next to the article, select **Also display in**, choose the category/subcategory, and click **Share**. You can choose multiple categories when sharing an article.  
  ![1_Screenshot-Accessing_also_display_in_method_1](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/1_Screenshot-Accessing_also_display_in_method_1.png)
* The shared article feature can also be accessed when creating a new article. Select **Link existing** in the **Add article** module. Select an article from the **Select article** search bar, and click **Create**.

![8_Screenshot-Add_article_module_Link_existing](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/8_Screenshot-Add_article_module_Link_existing.png)

The article appears as a reference in the selected category/subcategory and is identified by a shared icon.

#### Original article & Referenced article

* The original article serves as the primary copy. All content and setting changes reflect across all shared copies (references).
* Click the **View references** icon on the right in the editor to see linked instances.
* You can navigate to the shared article or remove the reference (stop sharing) in the selected category
* Referenced articles cannot be edited. Except for the article slug, all other elements link to the original article.

![6_Screenshot-Shared_article_POV](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/6_Screenshot-Shared_article_POV.png)

[**Read more →**](/v3/docs/shared-articles)

### 2. Cloning articles

Create a **clone article** from an existing article in your project's version and language.

Select **Copy existing** in the **Add article** module. Select an article from the **Select article** search bar, edit the title, and click **Create**.

![7_Screenshot-Add_article_module_Copy_existing](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/7_Screenshot-Add_article_module_Copy_existing.png)

Your clone article appears in the respective category/subcategory with a new article indicator (light-blue dot) showing it hasn't been published.

[**Read more →**](/v3/docs/creating-an-article)

---

## Enhancements

### 1. Intercom extension

Two notable enhancements to the Intercom extension:

* When sharing an article link in chat, customers can open and read Document360 articles within their messenger window. Previously, articles opened in the knowledge base site
* Create articles from Intercom. They appear as drafts in the selected category

[**Read more →**](/v3/docs/intercom-integration)

### 2. Internal links in new versions

When creating a new version using an existing version as base, you can choose how internal article links behave:

![14_Screenshot-Internal_links_in_new_version](https://cdn.document360.io/860f9f88-412e-4570-8222-d5bf2f4b7dd1/Images/Documentation/14_Screenshot-Internal_links_in_new_version.png)

* **New** (default): Internal links point to the new version's articles

  > **Example**: */****v2****/docs/Installation* becomes */****v3****/docs/Installation*

* **Existing**: Internal links continue pointing to the base version's articles

[**Read more →**](/v3/docs/getting-started-with-project-version)

### 3. Knowledge base assistant

You can now add category pages and category indexes in **Single** and **List** actions for URL mapping in the Knowledge base assistant. Previously, only articles could be added. This allows categories to appear in your knowledge base assistant.

[**Read more →**](/v3/docs/url-mapping)

### 4. Analytics

* Category page and index analytics now appear under **Leading categories** in **Performance** analytics. Identify them with the **View in knowledge base** icon
* Category page link validation was introduced in this release
* Category pages now appear in **Team accounts** analytics under **Most viewed articles** and **Articles created** sections. Identify them with the folder icon
* A new **Feedback status** column was added to the **Feedback** page. Shows a percentage bar comparing **likes** (green) to **dislikes** (red)

[**Read more →**](/v3/docs/analytics)

### 5. Users & Security

* Bulk selection is now available when adding team accounts or readers to groups. Previously, accounts had to be added individually
* For new or invited SSO team accounts and readers (including regular Document360 users), you can now view who invited them and when. Check the **Team accounts** or **Readers** page in **Users & Security**

[**Read more →**](/v3/docs/users-and-security)

---

## Improvements

### UI/UX improvements

* The **Add article** module was redesigned to support clone and shared article features
* Two new fields were added to the **mobile sign up** page: subdomain and project access type (Public/Private/Mixed)
* Category pages now support likes, dislikes, and feedback options, matching article functionality

### Other improvements

* Project version name limit increased from 20 to **30 characters**
* **Previous** and **Next** buttons at article bottom can now be localized in selected languages *(Settings → Localization & versions → Localization variables → Article bottom)*
* In the **Home page builder** header section, you can now add article slugs in Custom URL selection
* Minor performance, bug fixes, and security improvements were made to the knowledge base portal and site

<a id="march-2022-release-note"></a>

## March 2022

Document360 released its monthly update in March 2022. Here are the enhancements and improvements made to the Document360 knowledge base.## April 2021

Document360 released its monthly update in April 2021 with several new features and enhancements. Key additions include article templates, updated category management, and a new Salesforce extension. Other improvements cover team account imports, automatic article status indicators, Enterprise SSO binding types, and performance optimizations.

---

## New features

### Article templates

Create articles from predefined templates for consistent formatting across your knowledge base. Templates can be used for user guides, FAQs, release notes, or any custom format you define.

Access templates through the **Templates** option at the bottom of the category manager.

[**Read more →**](https://docs.document360.com/docs/article-templates)

### Category types

Categories now support three distinct types beyond the basic folder structure:

1. **Folder**: Simple container for articles and sub-categories
2. **Index**: Displays all articles within the folder with preview excerpts
3. **Page**: Functions like a standard article

Select category types during creation or modify existing categories. The category manager UI has also been updated with a new Templates option in the left navigation pane.

[**Read more →**](https://docs.document360.com/docs/category-types)

---

## New Extensions

### Salesforce

Integrate Document360 directly with Salesforce to enhance support agent productivity. Search, share, and create knowledge base articles without leaving the Salesforce platform.

[**Read more →**](https://docs.document360.com/docs/salesforce)

---

## New Integrations

Four new integrations were added:

|  | Integration | Type | Description |
| --- | --- | --- | --- |
| 1 | **Belco** | Chat | Live chat and messaging for website visitors |
| 2 | **Gorgios** | Chat | Multi-channel customer communication platform |
| 3 | **FullStory** | Analytics | Customer experience optimization and problem solving |
| 4 | **Sunshine Conversations** | Chat | Cross-platform messaging for businesses |

[**Read more →**](https://docs.document360.com/docs/integrations-getting-started)

---

## Enhancements

### Import team accounts

Import team accounts from local CSV files, similar to reader account imports. Use the standard template available in the portal.

### Article attachments from external sources

Add article attachments via external URLs instead of being limited to Document360 Drive files.

### Automatic article status indication

Set automatic status indicators (New/Updated) for initial or forked article publishes. Configure this feature at *(Settings → Knowledge base site → Article settings & SEO → Category manager)*.

Default period is 30 days, adjustable between 1-90 days.

### Table of contents in PDF exports

PDF exports now include a table of contents with navigation links based on your category structure.

---

## Improvements

* Overall performance improved with reduced load times
* Link status feature enhanced with hidden article filtering
* Added HttpPost and HttpRedirect binding types for Enterprise SSO SAML configuration
* 'What's new' feature now supported on sub-folder hosted projects with security fixes
* Latest changes option moved from profile section to top right of portal

<a id="march-2021-release-note"></a>

## March 2021

Document360 March 2021 updates focused on knowledge base design improvements and security enhancements. Key changes include external URL support for logos and favicons, SSO login updates, and fixes for the recently released 'What's new' feature.

---

## Enhancements

### Knowledge base site design

Add logos and favicons from external URLs. Choose indent levels (small/medium) in fluid layout. Combined with February's font selection options, these updates make knowledge base design more flexible.

### 'What's new' security update

Fixed a security issue where readers could access the 'What's new' page through bookmarked URLs even when the feature was disabled. Now access is properly restricted based on portal settings *(Settings → Knowledge base site → Article Settings & SEO → Document header)*.

---

## Improvements

* Project creation performance optimized
* File replace functionality now supports Draw.io format files

<a id="february-2021-release-note"></a>

## February 2021

February 2021 brought the File replace feature to Document360 Drive, allowing easier file updates in documentation. Additional improvements covered UI/UX refinements and knowledge base font customization options.

---

## New Features

### File replace

Replace existing files in Drive with the same extension and filename. Useful for updating article assets without breaking links.

Access through the **more options** menu (•••) next to any file, or by selecting the file and clicking **File replace** in the right panel.

[**Read more →**](https://docs.document360.com/docs/file-replace)

---

## Improvements

* SSO user handling improved in public [**API Documentation**](https://apidocs.document360.com/docs/get-users) under Teams
* Reorder project versions for reader display through drag-and-drop *(Settings → Project Admin → Localization & versions)*
* Customize **Body** and **heading fonts** in Knowledge base design settings *(Settings → Knowledge base site → Design)*
* Control individual social media sharing options for articles
* Analytics **Overview** renamed to **Geography**<a id="document360-support-generating-a-har-file"></a>

## Generating a HAR file

### What is an HAR file?

An **HAR** (HTTP Archive) file is a JSON-formatted log of a web browser's interaction with a web page. It records requests and responses, cookies, timings, and other metadata related to page loading and rendering.

> Document360 uses HAR files for debugging and performance analysis—they provide a detailed record of browser interactions with your project.

### How to generate a HAR file?

Most modern browsers can generate HAR files through their developer tools.

---

## Generate HAR files in web browsers

Follow these steps to generate a HAR file for troubleshooting Document360 issues:

1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge
4. Safari
5. Opera

The steps are generally similar across browsers, with minor UI differences.

### Google Chrome

1. Open Chrome and go to [**portal.document360.io**](https://portal.document360.io/)
2. Select your Document360 project
3. Click **Chrome menu** (three dots) > **More Tools** > **Developer Tools**
4. Click the **Network** tab
5. Check **Preserve log** to prevent clearing network activity during navigation
6. Ensure recording is active (look for a red dot; click Record icon if needed)
7. Reproduce the issue
8. Stop recording with **Ctrl+E** or by clicking the red dot again
9. Right-click in the network table and select **Save all as HAR with content**
10. Save the file to your local storage

### Mozilla Firefox

1. Open Firefox and go to [**portal.document360.io**](https://portal.document360.io/)
2. Select your Document360 project
3. Click **Firefox menu** (three lines) > **Web Developer** > **Network**
4. Click **Persist Logs** to keep network data during navigation
5. Select the **All** tab to capture all network activity
6. Verify recording is active (red dot; click Record icon if needed)
7. Reproduce the issue
8. Stop recording with **Ctrl+E** or by clicking the red dot
9. Right-click network requests and select **Save All As HAR**
10. Save the file to your local storage

### Microsoft Edge

1. Open Edge and go to [**portal.document360.io**](https://portal.document360.io/)
2. Select your Document360 project
3. Click **Edge menu** (three dots) > **More Tools** > **Developer Tools**
4. Click the **Network** tab
5. Check **Preserve log** to maintain network data during navigation
6. Confirm recording is active (red dot; click Record icon if needed)
7. Reproduce the issue
8. Stop recording by clicking the red dot
9. Right-click network requests and select **Save all as HAR with content**
10. Save the file to your local storage

### Safari

1. Open Safari and go to [**portal.document360.io**](https://portal.document360.io/)
2. Select your Document360 project
3. Enable **Develop** menu: **Safari** > **Preferences** > **Advanced** > **Show Develop menu in menu bar**
4. From **Develop** menu, select **Show Web Inspector**
5. Click the **Network** tab
6. Check **Preserve log** to prevent clearing network activity
7. Verify recording is active (red dot; click Record icon if needed)
8. Reproduce the issue
9. Stop recording by clicking the red dot
10. Right-click network requests and select **Export HAR**
11. Save the file to your local storage

### Opera

1. Open Opera and go to [**portal.document360.io**](https://portal.document360.io/)
2. Select your Document360 project
3. Click **Opera menu** (three lines) > **Developer** > **Developer Tools**
4. Click the **Network** tab
5. Check **Preserve log** to maintain network data during navigation
6. Confirm recording is active (red dot; click Record icon if needed)
7. Reproduce the issue
8. Stop recording by clicking the red dot
9. Right-click network requests and select **Save as HAR with Content**
10. Save the file to your local storage

Share the generated HAR file with Document360 support for faster issue resolution.