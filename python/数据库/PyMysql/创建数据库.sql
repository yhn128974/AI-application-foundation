-- 创建一个演示数据库。
-- IF NOT EXISTS 表示：如果 ai_work_demo 已经存在，就不重复创建。
-- DEFAULT CHARSET utf8mb4 表示：默认使用 utf8mb4 字符集，方便保存中文。
CREATE DATABASE IF NOT EXISTS ai_work_demo DEFAULT CHARSET utf8mb4;

-- 进入 ai_work_demo 数据库。
-- 后面的建表、插入数据都会在这个数据库中执行。
USE ai_work_demo;

-- 删除旧的 ai_tools 表。
-- 这样每次录屏前都能得到一份干净的数据，避免之前练习留下的数据影响演示。
-- 注意：DROP TABLE 会删除整张表，真实项目中不能随意执行。
DROP TABLE IF EXISTS ai_tools;

-- 创建 AI 工具表。
-- id：工具编号，主键，自增。
-- name：AI 工具名称，例如 ChatGPT、DeepSeek、Dify。
-- scene：工具的使用场景，例如代码解释、工作流编排。
-- status：工具状态，0 表示未启用，1 表示已启用。
CREATE TABLE ai_tools (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    scene VARCHAR(100) NOT NULL,
    status TINYINT NOT NULL DEFAULT 0
);

-- 插入课堂演示数据。
-- 这几条数据贴近 AI 工作场景，学生容易理解。
-- status 为 1 表示已经启用，status 为 0 表示暂时未启用。
INSERT INTO ai_tools(name, scene, status) VALUES
('ChatGPT', '代码解释和文案生成', 1),
('DeepSeek', '代码生成和知识问答', 1),
('Dify', 'AI 工作流编排', 0),
('LangChain', 'Agent 工具调用开发', 0);

