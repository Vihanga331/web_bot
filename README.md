# Ai Bot - This bot

### This bot can gather data from websites and analyze them.

### Future Updates
    * Add excel automation tools to auto generate exel sheets with AI
    * Add automated workflow to work with exel and google sheets
    * Add real API to scan webpages and extract contents for reasearch and related tasks
    * Send reports to telegram via bot.

# Project Current Status
Currently this is a template. this will develop overtime to final product that user can used with a website/app

### Architecture Overview - UNFINISHED(ONLY A TEMPLATE)

```mermaid
graph TD
    %% Nodes definition
    WP1[wikipedia.org]
    WP2[news.blog]
    API[API]
    Skill[Skill]
    Agent[The Agent]

    %% Connections
    WP1 --- API
    WP2 --- API
    API --> Skill
    Skill --- Agent

    %% Formatting styling
    style API stroke:#333,stroke-width:2px
    style Agent stroke:#333,stroke-width:2px
