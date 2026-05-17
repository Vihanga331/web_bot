# working Project, hand coded. 
first commit

# developing in spiral

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
