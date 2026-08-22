# B. AI 组织转型的权威报告与实证数据

> **用途**：为《AI 原生组织（AI-Native Organization）》一书提供权威报告的一手数据支撑。
> **编制说明**：本文件所有数据均基于 2025 年 7 月—2026 年 8 月对原始报告、原始新闻稿、机构官网的逐条核验（web_extract 抓取原文/PDF 核对），并标注来源 URL。凡引用媒体转述处均明确标注「媒体转述」；无法在原始机构官网核验的数字一律标注「未在官网核验，二手来源」。各数据点附**局限性说明**（样本量、口径、时间窗口），请勿在书中直接引用未经核验的二手数字。
> **关键提醒**：中文互联网广泛流传的「Gartner 预测 2025 年 90% 大企业设立 CAIO」**查无实据，并非 Gartner 官方预测**（详见 §4.1 勘误）。

---

## 1. MIT NANDA《The GenAI Divide: State of AI in Business 2025》——「95% 失败率」的原始出处

- **报告**：Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari，《The GenAI Divide: State of AI in Business 2025》，MIT Project NANDA，2025 年 7 月（初步报告，preliminary findings）。
- **来源 URL（报告 PDF 原文）**：https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- **研究期间**：2025 年 1—6 月。

### 1.1 「95% 失败率」的具体数字与口径（报告原文）

| 数据点 | 精确表述 | 口径 |
|---|---|---|
| 投资规模 | 企业 GenAI 投入 **300–400 亿美元**（$30–40 billion） | 报告估算的企业级 GenAI 总投资 |
| 「95%」的原始表述① | 「**95% of organizations are getting zero return**」（95% 的组织投资回报为零） | 按组织计，非按项目计 |
| 「95%」的原始表述② | 「The 95% failure rate for enterprise AI solutions represents the clearest manifestation of the GenAI Divide」（企业级 AI 解决方案 95% 的失败率是 GenAI 鸿沟最清晰的体现） | 报告摘要层表述 |
| 通用大模型漏斗 | 超过 **80%** 的组织「探索或试点过」ChatGPT/Copilot 类工具；近 **40%** 报告已部署 | 通用型 LLM（个人效率工具） |
| 定制/任务型工具漏斗 | **60%** 的组织评估过此类工具 → 仅 **20%** 进入试点 → 仅 **5%** 进入生产（production） | 「成功实施」定义为：用户/高管确认带来显著且持续的生产力或 P&L 影响 |
| 失败率的计算来源 | 95% = 定制型企业 AI 工具中未能进入生产（5% 进入生产）的占比 | 注意：**不是**「95% 的试点项目失败」的统计口径 |

> **关键口径辨析（写书时务必使用）**：媒体普遍将 MIT 报告概括为「95% 的 AI 试点失败」，但报告原文的准确口径是两层：
> ① 按**组织**计——95% 的组织从 GenAI 投资中「零回报」；
> ② 按**工具漏斗**计——定制/任务型企业级 AI 工具只有 5% 能走到生产部署（60% 评估 → 20% 试点 → 5% 生产）。
> 而通用聊天工具（ChatGPT 等）的「试点→部署」转化率约为 83%（约 80%→40% 的漏斗），并不失败。**「失败」指的是深度嵌入业务流程的定制系统，不是所有 AI 项目。**

### 1.2 报告的完整关键发现

1. **GenAI 鸿沟（GenAI Divide）**：买方（企业/中市场/SMB）与卖方（创业公司/厂商/咨询公司）的结果两极分化——约 5% 的整合型 AI 试点创造数百万美元价值，绝大多数组织「卡住」且无 measurable P&L 影响。
2. **核心障碍是「学习缺口」（learning gap），不是模型质量或监管**：大多数 GenAI 系统不保留反馈、不适应上下文、不随时间改进。
3. **行业扰乱指数（AI Market Disruption Index，0–5 分）**：仅 2 个行业（科技、媒体与电信）出现结构性扰乱信号；其余 7 个行业（专业服务、医疗、消费零售、金融、先进制造、能源材料等）大量试点但结构几乎未变——报告正文口径为「7/9 行业落后」（执行摘要中一处写「2 of 8」，两处口径不一致，属报告自身瑕疵）。
4. **企业悖论**：大企业（年收入 >1 亿美元）试点数量最多、投入 AI 人员最多，但**试点→规模化转化率最低**；中市场公司更快——头部中市场企业从试点到全面实施平均 **90 天**，企业平均 **9 个月以上**。
5. **投资错配**：过半 GenAI 预算流向销售与市场等前台部门，而最高 ROI 在后台自动化（削减 BPO 外包支出、外部代理成本）。
6. **实施方式差异**：外部合作伙伴实施的**成功率约为内部自建的 2 倍**（报告原文表述）。媒体采访补充：「购买/合作的成功率约 67%，内部自建成功率仅为前者的 1/3」（媒体转述，见 §1.3）。
7. **就业影响有限但开始显现**：多数实施**并未带来裁员**；已跨过鸿沟的组织在客服、软件工程、行政岗位出现选择性用工影响，主要通过「职位空缺不补」而非大规模裁员；裁员集中于低价值的外包岗位。
8. **五个迷思**：包括「AI 几年内取代大多数工作」被研究否定（研究发现裁员有限）。
9. **影子 AI 普遍**：未经批准的 ChatGPT 等工具广泛使用；衡量 AI 对生产力的影响仍困难。
10. **先行者的方向**：领先组织开始试验「可学习、可记忆、可在边界内自主行动」的代理式（agentic）AI 系统。

### 1.3 媒体转述 vs 报告原文（重要差异）

- **Fortune 报道（Sheryl Estrada，2025-08-18）**：https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
  - 媒体称研究方法为「**150 次高管访谈 + 350 名员工问卷 + 300 个公开 AI 部署分析**」。
  - **报告原文**的方法学是：「**系统回顾 300+ 个公开披露的 AI 项目 + 与 52 个组织的结构化访谈 + 在 4 个行业大会收集的 153 名高管问卷**」。
  - **两者不一致**：媒体报道的样本量与报告原文不同（媒体版本的数字无法在报告中核实，应为记者与作者沟通后的口径，或报道错误）。写书引用样本量时请以报告原文（52 组织访谈 / 153 高管问卷 / 300+ 项目）为准。
- 媒体称「购买工具与伙伴合作成功率约 67%，内部自建成功率只有其三分之一」——报告原文仅写「外部合作成功率约为内部自建的 2 倍」。写书建议采用报告原文口径，或标注为「作者接受 Fortune 采访时的表述」。

### 1.4 局限性（报告自述 + 本研究补充）

- 报告在方法学章节明确自述：「这些数字是基于访谈的方向性估计（directionally accurate），而非官方公司报告；各分类样本量不一；不同组织的成功定义不同。」
- 观察窗口仅 6 个月（2025 年 1—6 月），对复杂企业系统的「成功」评估可能不足，**可能低估长期成功率**。
- 行业扰乱分数基于公开可观察指标与访谈判断，可能遗漏私有/新兴进展；受权重方案影响（专业服务行业得分在 1.2–2.1 之间波动）。
- 存在选择偏差（愿意参与 AI 研究的组织可能更激进或更保守）。
- 报告为 MIT 学者独立研究，声明不代表任何雇主立场；未经同行评审（初步报告）。
- 本研究的补充提醒：MIT NANDA 项目与 NANDA 软件（记忆/学习框架）存在商业关联，引用「学习型系统」结论时宜留意潜在利益关系。

---

## 2. McKinsey《The State of AI in 2025: Agents, innovation, and transformation》

- **报告**：McKinsey Global Survey on AI（第 8 次年度调查），2025 年 11 月 5 日发布。
- **来源 URL**：https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **方法**：在线高管调查（McKinsey 全球调查，受访者为各行业企业高管/管理者，样本偏向大企业；报告未公开精确 N，属于长期连续调查）。

### 2.1 关键组织数据（报告原文）

1. **采用率**：**88%** 的受访者称其组织至少在**一个业务职能**中「定期使用 AI」（上一轮为 78%）。
2. **规模化滞后**：约 **2/3** 受访者称组织仍处于**实验/试点阶段**，尚未开始企业级规模化；仅约 **1/3** 报告已开始规模化。
   - 分化：营收 >50 亿美元的公司中**近一半**进入规模化阶段；营收 <1 亿美元的公司仅 **29%**。
3. **AI 代理（agentic AI）**：**62%** 的受访者称组织至少在「尝试」AI 代理；**23%** 报告已在至少一个职能中**规模化**代理系统；但在**任意单一职能**中规模化代理的受访者不超过 **10%**。
4. **财务影响罕见**：仅 **39%** 的受访者将任何程度的 EBIT 影响归因于 AI，且其中多数称 AI 贡献不到 EBIT 的 5%。「AI 高绩效者」（EBIT 影响 ≥5% 且自评「显著」价值）= 受访者中约 **6%**。
5. **创新等定性收益**：**64%** 称 AI 正在赋能组织创新；近半数报告客户满意度改善。
6. **目标设定**：**80%** 将「效率」设为目标；而价值最高的公司常把「增长/创新」作为附加目标；**一半**的 AI 高绩效者打算用 AI 做企业级转型，且多数在**重新设计工作流**。
7. **用工预期（未来一年 AI 对总人力规模的影响）**：预期**减少** 32%，**不变** 43%，**增加** 13%。
8. **多职能渗透**：>2/3 的受访者称组织在**多个职能**使用 AI；**一半**在 3 个及以上职能使用 AI。

### 2.2 与本书主题直接相关的结论（报告原文）

- 「从试点到规模化影响的转变在大多数组织仍是未竟之事」；「多数组织尚未把 AI 深嵌到工作流与流程中，因此没有实现可观的**企业级**收益」。
- 职能分布：IT 与知识管理是代理使用最多的职能；行业上科技、媒体电信、医疗的代理使用最普遍。

### 2.3 局限性

- 基于高管**自报**（perception-based），非客观使用数据；样本向大型企业倾斜；「定期使用」定义各受访者理解可能不同；EBIT 归因受主观判断影响；代理数据反映「实验」多于「生产」。

---

## 3. BCG《AI at Work》系列（2025 / 2026）

### 3.1 BCG《AI at Work 2025: Momentum Builds, but Gaps Remain》（2025-06-26）

- **来源 URL**：https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain ；新闻稿：https://www.bcg.com/press/26june2025-beyond-ai-adoption-full-potential
- **样本**：**11 个国家/地区、10,600+** 领导者、管理者与一线白领员工（2025 年版年度调查；比 2024 年版 13,000 人/18 国的样本略有缩减）。

**关键数据（报告/新闻稿原文）**：

1. **领导层与一线断层**：超过 **3/4** 的领导者与管理者「每周多次」使用 GenAI；一线员工「经常使用」比例**停滞在 51%**（2024 年为 64%、2018 年为 46%——管理者的比例轨迹；一线为 51%）。
2. **从部署到重塑**：**一半**的公司正从「部署（Deploy）」走向「重塑工作流（Reshape）」，金融与科技行业领先。
3. **AI 代理仍早期**：**3/4** 的员工认为 AI 代理对未来成功至关重要；但仅 **13%** 认为代理已深度集成到日常工作流；仅 **1/3** 理解其运作方式。
4. **工作安全感**：处于全面 AI 重构组织中的员工更担心工作安全（**46%**），高于 AI 集成度较低组织（**34%**）；领导者/管理者（**43%**）比一线员工（**36%**）更担心未来十年失业。
5. 员工用得越多，担忧反而越多（报告原文）。

### 3.2 BCG《AI at Work 2026: Why Strategy Matters More Than Tools》（2026-06-03）

- **来源 URL**：https://www.bcg.com/publications/2026/ai-at-work-why-strategy-matters-more-than-tools
- **样本**：接近 **12,000** 名一线员工、管理者与领导者，覆盖十余个全球市场。
- **关键数据**：一线员工「每天或每周几次」使用 AI 的比例升至 **74%**，较 2025 年 **+23 个百分点**（一线采用率从停滞转为跃升）。

### 3.3 局限性

- 样本为自愿参与调查的受访者，白领/办公室员工为主（"frontline white-collar employees"），对蓝领/实体一线代表性有限；「经常使用」定义由调查方设定；BCG 同时向客户出售 AI 转型咨询服务，存在利益相关；不同年份样本构成不同（13,000→10,600→12,000），跨年比较需谨慎。

---

## 4. Gartner 系列预测与调查

### 4.1 CAIO（首席 AI 官）预测——附中文媒体勘误 ⚠️

- **可核验的 Gartner 预测**：「到 **2025 年，35%** 的大型组织将设立向 CEO 或 COO 汇报的 Chief AI Officer」（Gartner，2023 年发布的预测）。Gartner 官网原始新闻稿链接未能检索到，此数字见于大量二手引用（如 Andela CIO Guide、LinkedIn 分析文章等）；标注为**二手广泛引用、未在 gartner.com 核验**。
- **常见但未能核验的预测**：「到 2026 年 75% 的大企业将在 C 级设有 AI 负责人」——中文/英文网络广泛引用，但本研究未能在 gartner.com 找到对应原始发布物，**建议谨慎使用或标注来源不明**。
- **勘误**：中文互联网流传「Gartner 预测 2025 年 90% 大企业设立 CAIO」——**查无实据，不是 Gartner 官方预测**（Gartner 可查的原预测为 35%）。书稿中凡引用「90%」处应删除或改为「35%（Gartner 2023 预测）」。

### 4.2 Gartner：GenAI 项目失败率预测（2024-07-29 新闻稿）

- **预测**：到 **2025 年底，至少 30%** 的生成式 AI 项目将在概念验证（proof of concept）后被**放弃**，原因是数据质量差、成本上升、价值不清晰等。
- **来源 URL**：https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
- **与 MIT NANDA 95% 的关系（写书建议）**：两者口径完全不同——Gartner 是「预测 30% 在 PoC 后被放弃」（按项目、按阶段）；MIT 是「95% 组织零回报 / 5% 定制工具进生产」（按组织/按完整漏斗）。**引用时应并列说明口径差异，避免混用造成「AI 项目 30% 失败 vs 95% 失败」的假矛盾。**

### 4.3 Gartner：企业应用嵌入 AI 代理预测（2025-08-26 新闻稿）

- **预测**：到 **2026 年底，40%** 的企业应用将集成**任务型 AI 代理**，2025 年这一比例不足 **5%**。
- **来源 URL**：https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

### 4.4 Gartner 调查：2030 年 IT 工作全面 AI 化（2025-11-10 新闻稿）

- **数据**：到 2030 年，CIO 预计 **0%** 的 IT 工作由「无 AI 的人类」完成；**75%** 由「人类 + AI 增强」完成；**25%** 由 **AI 代理独立完成**。
- **来源 URL**：https://www.gartner.com/en/newsroom/press-releases/2025-11-10-gartner-survey-finds-artificial-intelligence-will-touch-all-information-technology-work-by-2030
- 说明：这是 CIO 的**预期调查**（expectation），非实测；按 CIO 估计口径。

### 4.5 Gartner 2026+ 战略预测（2025-10-21 新闻稿）

- **来源 URL**：https://www.gartner.com/en/newsroom/press-releases/2025-10-21-gartner-unveils-top-predictions-for-it-organizations-and-users-in-2026-and-beyond
- 代表性预测（与组织转型相关）：
  - 到 **2027 年，75%** 的招聘流程将包含**工作场所 AI 熟练度认证/测试**。
  - 到 **2028 年**，利用**多代理 AI 处理 80% 客户面对流程**的组织将占据主导地位。
  - 到 **2028 年，90%** 的 B2B 采购将由 AI 代理中介，推动超 **15 万亿美元** B2B 交易。

### 4.6 局限性

- Gartner 预测为**分析师判断**（predictions），非实证统计，历史命中率不一；所有数字都是面向未来的预测，引用时须注明「预测」而非「事实」；部分预测基于 Gartner 客户调查，样本不可公开核验。

---

## 5. Forrester《Predictions 2026》

- **博客/报告**：
  - 《Predictions 2026: AI Moves From Hype To Hard Hat Work》（2025-10-08）：https://www.forrester.com/blogs/predictions-2026-ai-moves-from-hype-to-hard-hat-work/
  - 《Predictions 2026: AI Agents, Changing Business Models, And Workplace Culture Impact Enterprise Software》（2025-11-05）：https://www.forrester.com/blogs/predictions-2026-ai-agents-changing-business-models-and-workplace-culture-impact-enterprise-software/
- **可核验的数据点（博客公开部分）**：
  1. 到 2026 年，**30%** 的大企业将**强制 AI 培训**；21% 的 AI 决策者将员工体验与培训列为……（原文见付费报告，博客仅列要点）。
  2. 2026 年，**30%** 的企业应用厂商将推出自己的 **MCP 服务器**（Model Context Protocol）。
  3. 企业软件从「以用户为中心」转向「以工人与流程为中心」——2026 年企业应用将容纳「AI 代理数字劳动力」。
  4. Forrester 宣传材料：多数组织 AI 投资 ROI **低于 50%**（「Most orgs get less than 50% ROI on AI」，为其咨询宣传口径，非严格统计）。
- **局限性**：Forrester 核心预测在付费报告（RES184992 / RES185008）中，公开博客只列标题式要点，具体预测数字大多**无法公开核验**；引用时宜以「Forrester 预测 2026：……」（带年份）并注明「博客公开内容」；「ROI<50%」为营销文案，不建议作为数据引用。

---

## 6. 微软《Work Trend Index》（2024 / 2025 / 2026 年度报告）

### 6.1 WTI 2024《AI at Work Is Here. Now Comes the Hard Part》（2024-05-08）

- **来源 URL**：https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- **样本**：31,000 名知识工作者，31 个国家（微软与 LinkedIn 联合，含 M365 遥测与 LinkedIn 劳动力数据）。
- **关键数据（报告原文）**：
  - **75%** 的全球知识工作者已使用 AI 办公；过去六个月使用量**近乎翻倍**。
  - 46% 的用户开始使用 AI 不到 6 个月；**79%** 认为 AI 技能将拓宽职业机会。

### 6.2 WTI 2025《2025: The Year the Frontier Firm Is Born》（2025-04-23）

- **来源 URL**：https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
- **样本**：31,000 名员工/领导者（31 国）问卷调查 + M365 遥测（截至 2025-02-15，排除教育/欧盟租户）+ LinkedIn 数据；另访谈 AI 原生创业公司、学者与经济学家。
- **关键数据（报告原文）**：
  1. **82%** 的领导者认为 2025 年是重新思考战略与运营的关键年；**81%** 预计未来 12–18 个月代理会「中等或深度」融入公司 AI 战略。
  2. **24%** 的领导者称已**全组织部署** AI；仅 **12%** 仍处于试点模式。
  3. **82%** 的领导者有信心未来 12–18 个月用**数字劳动力**扩充产能。
  4. **产能缺口**：**53%** 的领导者认为生产力必须提高；而 **80%** 的全球员工（含领导者）表示缺乏时间/精力完成工作。
  5. **遥测数据（工作碎片化）**：核心工作时间平均每 **2 分钟**被打断一次（约 **275 次/天**）；**60%** 的会议是临时性的；PowerPoint 在会议前 10 分钟编辑量飙升 **122%**；9-5 之外的消息 **+15% YoY**（平均 58 条/天）；**48%** 的员工与 **52%** 的领导者称工作「混乱且碎片化」。
  6. **Frontier Firm（前沿企业，占受访领导者所在公司的约 9.3%：9,037 名领导者中 844 家达标）**：
     - **71%** 的 Frontier Firm 领导者称公司「蓬勃发展」，全球员工仅 **39%**。
     - **55%** 称能承担更多工作（全球 25%）；**90%** 认为工作有意义（全球 77%）；**93%** 对未来机会乐观（全球 80%）；担心 AI 抢走工作仅 **21%**（全球 **43%**）。
  7. **人力战略**：未来 12–18 个月，**47%** 领导者优先对现有员工 AI 技能培训；**45%** 用 AI 作数字劳动力扩充产能；**33%** 考虑**用 AI 削减人力**（其中 32% 同时奖励顶尖员工）；**32%** 计划增加人力。

### 6.3 WTI 2026《Agents, Human Agency, and the Opportunity for Every Organization》（2026-05-05）

- **来源 URL**：https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
- **样本**：20,000 名「正在使用 AI」的员工，10 国（2026-02-18—04-20 问卷；Edelman Data x Intelligence 执行；有效绘图样本 16,971）+ M365 Copilot 遥测（2026 年 2 月一周，>100,000 段对话）。
- **关键数据（报告原文）**：
  1. **49%** 的 Copilot 对话属于**认知工作**（分析、决策、解决问题、创造性思维）；其余：与人协作 19%、产出 17%、找信息 15%。
  2. **66%** 的 AI 用户称 AI 让他们把更多时间花在**高价值工作**上；**58%** 称能产出一年前做不出的工作；在「前沿专业人士」（Frontier Professionals，占 AI 用户的 **16%**）中升至 **80%**。
  3. 人类技能优先级：**50%** 认为「AI 输出质量控制」更重要；**46%** 认为「批判性思维」更重要；**86%** 把 AI 输出当起点而非最终答案。
  4. **转型悖论**：仅 **19%** 的 AI 用户处于「前沿（Frontier）」（个人能力与组织准备双高）；**16%**「停滞」；**10%**「能力被阻塞」（个人强、组织弱）；**5%**「能力未被利用」（组织强、个人弱）；约 **50%** 处于中间的「萌芽（emergent）」区。
  5. 仅 **1/4（26%）** 的 AI 用户称领导层对 AI 「清晰且一致」。
  6. **组织因素（文化、管理者支持、人才实践）对 AI 影响的贡献是个体努力的 2 倍**（AI Impact 分析：29 个因素、随机森林置换重要性，R²≈0.68–0.69；自报数据，相关性非因果）。

### 6.4 局限性

- WTI 是微软（Copilot/M365 供应商）的研究，遥测仅覆盖微软生态（M365/Copilot），「AI 用户」样本可能高估；「知识工作者」以办公室白领为主；问卷为自报；2026 版问卷**仅限已在用 AI 的人**（20,000 名 AI 用户），不能代表全员；「Frontier Firm」为微软自定义概念；跨年样本设计不同（31,000 全样本 vs 20,000 AI 用户），比例不可直接跨年比较。

---

## 7. 斯坦福 HAI《AI Index 2025》（补充：企业采用率基线）

- **报告**：Stanford HAI，AI Index Report 2025（2025 年 4 月发布）。
- **来源 URL**：https://hai.stanford.edu/ai-index/2025-ai-index-report （PDF：https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf）
- **关键数据**：2024 年 **78%** 的组织报告使用 AI（2023 年为 55%）；美国 2024 年私营 AI 投资 **1,091 亿美元**（中国 93 亿美元）。
- **局限性**：基于国际管理发展研究院（IMD）等调查的二手汇总；「使用 AI」定义宽泛。

---

## 8. 世界银行 / IMF / OECD / WEF——AI 对就业与组织的影响

### 8.1 世界银行《Digital Progress and Trends Report 2025: AI Foundations》

- **报告**：World Bank，Digital Progress and Trends Report 2025（AI 基础篇，2025 年发布，数据可视化更新于 2025 年 11 月）。
- **来源 URL**：https://www.worldbank.org/en/publication/dptr2025-ai-foundations （PDF：https://openknowledge.worldbank.org/bitstreams/86903114-6212-4c45-9011-938925cc61d1/download）
- **要点（报告原文）**：AI 重塑经济与社会的速度空前；中低收入国家在规模化采用与部署 AI 上面临陡峭挑战；新兴趋势是「**小 AI（Small AI）**」——更便宜、可在手机等日常设备运行的 AI 应用，已在农业、健康、教育等领域延伸 AI 触达。报告提出「**四 C 基础**」：连接（connectivity）、算力（compute）、情境/数据（context）、能力（competency）。
- **局限性**：国家/宏观视角，**不含组织层级（企业）的量化数据**；主要面向发展议题；本书可将其作为「国家/宏观 AI 基础」背景引用，不宜用于组织转型数据。

### 8.2 IMF

**(a) IMF《Gen-AI: Artificial Intelligence and the Future of Work》（SDN/2024/001，2024-01-14）**
- **来源 URL**：https://www.imf.org/en/publications/staff-discussion-notes/issues/2024/01/14/gen-ai-artificial-intelligence-and-the-future-of-work-542379
- **关键数据（报告原文，经 IMF 总裁 Georgieva 2024-01-14 博客及全球媒体报道）**：
  - AI 将影响全球约 **40%** 的工作；**发达经济体约 60%**、**新兴市场约 40%**、**低收入国家约 26%** 的工作面临 AI 暴露。
  - 约一半暴露岗位可能被 AI 增强（生产力提升），另一半可能被替代（工资/就业承压）——注意这是**暴露（exposure）**估计，不是失业预测。
- **局限性**：基于任务暴露度的模型估计，非实测失业；「暴露」≠「被取代」。

**(b) IMF《The Global Impact of AI: Mind the Gap》（WP/25/76，2025-04）**
- **来源 URL（PDF）**：https://www.imf.org/-/media/Files/Publications/WP/2025/English/wpiea2025076-print-pdf.ashx
- **关键结论（报告摘要原文）**：AI 将加剧国家间收入不平等，**发达经济体的增长影响可能是低收入国家的 2 倍以上**；AI 在非贸易部门的巨大影响可能削弱汇率调节的传统作用（「逆巴拉萨-萨缪尔森效应」）。
- **局限性**：多部门动态一般均衡（DSGE/GIMF）模型的**情景模拟**，取决于 AI 暴露度/准备度/获取度的假设，非事实数据。

### 8.3 OECD

**(a) OECD AI 雇主与员工调查（2022 年首轮）**
- **来源 URL**：项目页 https://www.oecd.org/en/about/projects/aisurveysofemployersandworkers.html ；报告页 https://www.oecd.org/en/publications/the-impact-of-ai-on-the-workplace-main-findings-from-the-oecd-ai-surveys-of-employers-and-workers_ea0a0fe1-en.html
- **样本**：2022 年初调查制造业与金融业 **5,334 名员工**和 **2,053 家企业**（多国）。
- **关键结论（报告/摘要原文）**：
  - 员工与雇主对 AI 在绩效与工作条件上的影响「总体非常正面」。
  - 员工/雇主报告 AI 带来**高度任务重组**（媒体/二手汇总口径：金融业 66%、制造业 72% 的雇主报告任务重组——二手来源，建议标注）。
  - OECD《就业展望 2023》（https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en/full-report/artificial-intelligence-job-quality-and-inclusiveness_a713d0ad.html ）：多数员工报告因 AI 获得更高工作乐趣、心理与身体健康改善；但同时，金融业 **42%** 的员工预期 AI 将降低工资。
  - 60% 的金融/制造业员工担心 AI 取代自己（The Next Web 2023-07-12 报道：https://thenextweb.com/news/oecd-finance-and-manufacturing-workers-fear-ai-replacement ——**媒体转述**）。
- **局限性**：2022 年数据早于 GenAI 普及；仅覆盖制造业与金融业两行业；任务重组/担忧比例部分来自二手转述，引用建议回到 OECD 原文。

**(b) OECD《Generative AI and the SME Workforce》（2025-11）**
- **来源 URL**：https://www.oecd.org/en/publications/generative-ai-and-the-sme-workforce_2d08b99d-en/full-report/component-3.html
- **要点**：面向中小企业的 GenAI 用工新调查（2025 年）；未及深度核验，可作书目线索。

### 8.4 WEF《Future of Jobs Report 2025》（2025-01-08）

- **来源 URL**：新闻稿 https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/ ；报告 PDF https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- **样本**：**1,000+ 家雇主**（覆盖 **22 个行业、55 个经济体、1,400 万+ 员工**）。
- **关键数据（报告/新闻稿原文）**：
  1. 到 2030 年，就业扰乱相当于现有岗位的 **22%**：创造 **1.7 亿**新岗位、淘汰 **9,200 万**，净增 **7,800 万**。
  2. 约 **39%** 的岗位所需技能将改变；**63%** 的雇主将技能缺口列为转型最大障碍。
  3. 以 100 人为例，**59 人**需要到 2030 年前再培训/升级技能，其中 **11 人**可能得不到培训——即超 **1.2 亿**工人面临中期裁员风险。
  4. 企业 AI 应对：**77%** 的雇主计划**提升员工技能**；**41%** 计划因 AI 自动化**缩减人力**；约一半雇主计划将受 AI 冲击岗位的员工转岗至其他业务。
- **局限性**：雇主**预期调查**（前瞻性），非实际就业数据；样本偏大企业与国际组织生态；各国抽样不均。

---

## 9. HBS / INSEAD 研究补充（AI 原生组织 / 人机比的实证）

> 已知素材（书稿已含）：HBS 26-090《AI-Native Firms》（小 25%、扁平半级、产品通道 vs 流程通道、服务型小 70%）。以下为**新增补充**：该论文的更细数据 + 一项新的随机实验研究。

### 9.1 HBS 26-090《AI-Native Firms》补充细节

- **论文**：Hyunjin Kim（INSEAD）、Rembrand Koning（HBS）等，《AI-Native Firms》，HBS Working Paper 26-090（2026-06-09 版）/ SSRN 6905079。
- **来源 URL**：https://www.hbs.edu/ris/download.aspx?name=26-090.pdf ；SSRN：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6905079 ；HBS 学院页：https://www.hbs.edu/faculty/Pages/item.aspx?num=69077
- **样本**：Y Combinator W20—F24 批次 + 美国风投支持公司（同行业-同批次对照组）。
- **补充数据点（论文摘要原文）**：
  - AI 原生公司**小 25%**（员工数）；
  - **工程师占比高 13 个百分点**（engineers share is 13% greater）；
  - 入门级（entry-level）与非工程师岗位占比更低；
  - 层级更扁平（书稿已含「扁平半级」）；
  - 与可比初创相比，规模更小、更扁平、更工程师密集，但估值相当。
- **局限性**：以 YC/风投初创为样本，未必外推到成熟大企业；「AI-native」分类为研究者定义；工作论文未经同行评审。

### 9.2 INSEAD/HBS《Mapping AI into Production》随机田野实验（新增，强烈建议写入书中）

- **论文**：Hyunjin Kim, Dahyeon Kim, Rembrand Koning，《Mapping AI into Production: A Field Experiment on Firm Performance》，INSEAD Working Paper 2026/20/STR（2026 年 3 月），SSRN 6513481。
- **来源 URL（HBS AI 研究所解读）**：https://aiinstitute.hbs.edu/everyone-has-ai-which-firms-are-going-to-win/ ；SSRN：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6513481
- **设计（这是稀缺的因果证据）**：**515 家**高增长初创企业随机分组；**所有**企业获得同等 API 额度、前沿模型访问权与技术培训；**处理组**额外获得「AI 原生公司如何重组生产流程、团队与商业模式」的案例研究材料（对照组只上普通创业课）——在**工具、技能、预算完全拉平**的情况下，只改变「组织搜索空间」。
- **结果（处理组 vs 对照组，论文原文）**：
  - 发现/使用 AI 用例数量 **+44%**（尤其集中在战略、产品开发等高杠杆环节）；
  - 完成任务数 **+12%**；获得付费客户的可能性 **+18%**；营收 **1.9 倍**；
  - 外部资本需求反而 **下降 39.5%**（用 AI 扩产出而不用等比例扩投入）；
  - 收益集中在**分布上端**（AI 抬升的是顶尖企业的天花板）。
  - 例证：一家初创 10 周内用端到端 AI 管道（分类、合规检查、投标定价）从零做到 4 万美元收入、4 个付费客户，且**未招任何技术人员**。
- **核心概念「映射问题（mapping problem）」**：限制 AI 收益的不是技术成本或技能，而是「发现 AI 在自身生产流程中何处、如何创造价值」的认知瓶颈——与本书「组织摩擦/流程重设计」论点高度互证。
- **局限性**：10 周短期实验；初创样本；「营收 1.9 倍」为短期相对增量，绝对值小（如 4 万美元级）；案例材料效应=组织学习效应，不能完全分离「知识」与「激励」；单一（美国/全球创业生态）情境。

### 9.3 其他 HBS/INSEAD 组织实证线索（供延伸）

- HBS AI 研究所《Less Headcount, More Valuation: How AI-Native Firms Change the Game》（2026-06-23）：https://aiinstitute.hbs.edu/less-headcount-more-valuation-how-ai-native-firms-change-the-game/ （26-090 的解读文章）。
- HBS/INSEAD 还有「AI 是否会形成技术垄断」等后续研究（https://aiinstitute.hbs.edu/is-genai-heading-for-a-tech-monopoly/ ），可作延伸阅读。

---

## 10. 跨报告数字对照表（写书快速取用）

| 指标 | 数字 | 出处（报告+年份） | 口径/局限 |
|---|---|---|---|
| 企业 GenAI 零回报组织占比 | 95% | MIT NANDA《GenAI Divide》2025 | 按组织计；定制工具漏斗 60%→20%→5% |
| GenAI 项目 PoC 后放弃率（预测） | ≥30%（2025 年底） | Gartner 2024 预测 | 按项目计；预测非实测 |
| 至少一职能定期使用 AI | 88%（2025）vs 78%（2024） | McKinsey State of AI 2025 | 高管自报 |
| 已开始企业级规模化 | ~1/3（大企业近半） | McKinsey 2025 | 同上 |
| AI 高绩效者（EBIT≥5%） | ~6% 受访者 | McKinsey 2025 | 自报 EBIT 归因 |
| 一线员工经常使用 GenAI | 51%（2025）→ 74%（2026） | BCG AI at Work 2025/2026 | 白领一线样本 |
| 领导者/管理者每周多次使用 | >75%（2025） | BCG 2025 | 同上 |
| 知识工作者使用 AI | 75%（2024） | 微软 WTI 2024 | 31 国、31,000 人 |
| 领导者称已全组织部署 AI | 24% | 微软 WTI 2025 | 领导者自报 |
| 全组织 AI 部署后考虑减员 | 33% 领导者 | 微软 WTI 2025 | 意向非行动 |
| 组织采用 AI（公司级） | 78%（2024）vs 55%（2023） | 斯坦福 AI Index 2025 | 二手汇总调查 |
| 全球工作受 AI 影响（暴露） | ~40%；发达 60% | IMF SDN/2024/001 | 暴露度模型估计 |
| 2030 年岗位净变化 | +7,800 万（创造 1.7 亿/淘汰 9,200 万） | WEF FoJ 2025 | 雇主预期 |
| 雇主计划因 AI 缩减人力 | 41% | WEF FoJ 2025 | 预期非事实 |
| AI 原生公司员工规模 | 小 25%、工程师占比 +13pp | HBS 26-090（2026） | YC/风投初创样本 |
| 组织学习（映射）效应 | 用例 +44%、营收 1.9×、融资 −39.5% | INSEAD/HBS 田野实验 2026 | 10 周、515 家初创 |

---

## 11. 引用与写作警示（综合）

1. **口径先行**：「95% 失败率」（MIT）、「30% 被放弃」（Gartner）、「88% 采用」（McKinsey）三者并不矛盾，分别是**组织零回报率 / PoC 后放弃率 / 至少一职能采用率**。书中引用务必写明分母与阶段。
2. **报告结论 vs 媒体转述**：Fortune 报道 MIT 报告的样本量（150 访谈/350 问卷）与报告原文（52 组织/153 高管）不符；OECD「60% 员工担心被取代」「66%/72% 任务重组」等为二手转述，引用请回到原文或标注二手。
3. **预测 vs 事实**：Gartner/Forrester/WEF 的大部分数字是**前瞻预测或雇主预期**，不是已发生事实；微软 WTI「Frontier Firm」是供应商自定义概念。
4. **样本偏差**：McKinsey/WTI/BCG 的受访者以白领、大企业、主动参与调查者为主；MIT 报告为 52 组织访谈 + 153 高管问卷的小样本初步研究；一切「全球」表述都要检查原始抽样范围。
5. **利益相关**：MIT NANDA 与商业软件（NANDA 框架）关联；微软、BCG、麦肯锡均向企业出售 AI 产品/咨询；引用其结论时可在脚注注明立场。
6. **时间戳**：本书 2026 年 8 月定稿，以上数据截至 2026-08 已核验；引用时应标注「截至 2026 年 8 月」。
