--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: usertypes; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.usertypes AS ENUM (
    'client',
    'moderator'
);


ALTER TYPE public.usertypes OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    id integer NOT NULL,
    nickname text,
    password text,
    type public.usertypes
);


ALTER TABLE public.client OWNER TO postgres;

--
-- Name: client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.client_id_seq OWNER TO postgres;

--
-- Name: client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.client_id_seq OWNED BY public.client.id;


--
-- Name: refresh_token_storage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.refresh_token_storage (
    id integer NOT NULL,
    refresh_token text,
    expired timestamp without time zone
);


ALTER TABLE public.refresh_token_storage OWNER TO postgres;

--
-- Name: refresh_token_storage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.refresh_token_storage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.refresh_token_storage_id_seq OWNER TO postgres;

--
-- Name: refresh_token_storage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.refresh_token_storage_id_seq OWNED BY public.refresh_token_storage.id;


--
-- Name: result; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.result (
    id integer NOT NULL,
    text_id integer,
    user_id integer,
    correct_rate integer,
    speed integer
);


ALTER TABLE public.result OWNER TO postgres;

--
-- Name: result_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.result_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.result_id_seq OWNER TO postgres;

--
-- Name: result_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.result_id_seq OWNED BY public.result.id;


--
-- Name: text; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.text (
    id integer NOT NULL,
    text text,
    tier integer
);


ALTER TABLE public.text OWNER TO postgres;

--
-- Name: text_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.text_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.text_id_seq OWNER TO postgres;

--
-- Name: text_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.text_id_seq OWNED BY public.text.id;


--
-- Name: tier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tier (
    id integer NOT NULL,
    name text,
    correct_rate_ratio double precision,
    speed_ratio double precision
);


ALTER TABLE public.tier OWNER TO postgres;

--
-- Name: tier_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tier_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tier_id_seq OWNER TO postgres;

--
-- Name: tier_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tier_id_seq OWNED BY public.tier.id;


--
-- Name: client id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client ALTER COLUMN id SET DEFAULT nextval('public.client_id_seq'::regclass);


--
-- Name: refresh_token_storage id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refresh_token_storage ALTER COLUMN id SET DEFAULT nextval('public.refresh_token_storage_id_seq'::regclass);


--
-- Name: result id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.result ALTER COLUMN id SET DEFAULT nextval('public.result_id_seq'::regclass);


--
-- Name: text id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.text ALTER COLUMN id SET DEFAULT nextval('public.text_id_seq'::regclass);


--
-- Name: tier id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tier ALTER COLUMN id SET DEFAULT nextval('public.tier_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
7917fa4dd6cf
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client (id, nickname, password, type) FROM stdin;
\.


--
-- Data for Name: refresh_token_storage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.refresh_token_storage (id, refresh_token, expired) FROM stdin;
\.


--
-- Data for Name: result; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.result (id, text_id, user_id, correct_rate, speed) FROM stdin;
\.


--
-- Data for Name: text; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.text (id, text, tier) FROM stdin;
47	В последнее время все больше людей стали задумываться о своем здоровье и начали вести более активный образ жизни. Это очень важно, так как здоровье - основа всего. Нужно заботиться о себе, правильно питаться, заниматься спортом и регулярно проходить медицинские обследования. Здоровый образ жизни поможет избежать многих болезней и улучшить качество жизни.	1
48	Осенью природа удивляет своей красотой. Листья деревьев меняют свой цвет на яркий оранжевый, красный и желтый. Это создает неповторимую атмосферу и делает осень очень привлекательным временем года. Прогулки по паркам и лесам осенью принесут массу удовольствия и положительных эмоций.	1
49	наше время технологии развиваются очень быстро. Каждый день появляются новые гаджеты, приложения и программы, которые упрощают нашу жизнь. Однако, важно помнить, что технологии не заменят настоящего общения и человеческого тепла. Важно находить баланс между использованием технологий и общением в реальной жизни.	1
50	Путешествия - это один из самых увлекательных видов отдыха. Они позволяют увидеть новые места, познакомиться с разными культурами и традициями, а также отдохнуть от повседневной суеты и стресса. Путешествия помогают расширить кругозор и получить новые впечатления.	2
51	Образование играет очень важную роль в жизни каждого человека. Оно помогает развивать мышление, получать новые знания и навыки, а также строить успешную карьеру. Поэтому важно не пренебрегать образованием и постоянно совершенствовать себя.	2
52	Семья - это основа жизни каждого человека. Она дает нам поддержку, любовь и уверенность в завтрашнем дне. Важно уделять достаточно времени своим близким, заботиться о них и ценить каждый момент, проведенный вместе.	2
53	Здоровое питание - залог хорошего самочувствия и красивой фигуры. Важно следить за своим рационом, употреблять больше овощей, фруктов, злаков и ограничивать потребление жирной и сладкой пищи.	2
54	Время - самый ценный ресурс, который нельзя вернуть назад. Поэтому важно уметь ценить каждую минуту, проводить время с пользой, заниматься любимым делом и находить радость в мелочах.	3
55	Дружба - это одно из самых ценных чувств в жизни каждого человека. Настоящие друзья всегда поддержат в трудную минуту, порадуют успехами и будут рядом в любой ситуации.	3
56	Любовь - это то, что делает нашу жизнь яркой и запоминающейся. Важно уметь любить и быть любимым, ценить каждый момент вместе и радоваться возможности быть рядом.	3
57	Спорт - это не только здоровый образ жизни, но и возможность развивать свое тело, добиваться новых результатов и укреплять духовное состояние. Занятия спортом помогают выйти из зоны комфорта, научиться преодолевать трудности и становиться сильнее.	3
58	Музыка - это уникальное явление, способное вызывать разные эмоции, вдохновлять и поднимать настроение. Слушание музыки помогает расслабиться, отдохнуть от повседневных забот и насладиться моментом.	3
59	Работа - это не только способ заработать деньги, но и возможность реализовать свои таланты, достичь поставленных целей и получить удовлетворение от своего труда.	3
60	Культура - это то, что делает нашу жизнь более насыщенной и интересной. Посещение театров, музеев, выставок помогает расширить кругозор, познакомиться с новыми творческими произведениями и получить новые впечатления.	3
61	Развитие личности - это постоянный процесс самосовершенствования, который позволяет стать лучше, умнее и успешнее. Важно постоянно учиться, развивать свои навыки и стремиться к самореализации.	3
62	Животные - это наши верные друзья, которые приносят радость и позитивные эмоции в нашу жизнь. Важно заботиться о животных, любить их и создавать для них комфортные условия.	3
63	Экология - это забота о будущем нашей планеты. Важно бережно относиться к окружающей природе, экономно использовать ресурсы и бороться с загрязнением окружающей среды.	3
64	Религия - это один из основных аспектов жизни многих людей, который помогает им находить внутренний покой, верить в лучшее и следовать нравственным принципам.	3
65	Искусство - это форма самовыражения, способ передать свои чувства и эмоции через различные художественные произведения. Искусство помогает украсить нашу жизнь и делает ее более яркой.	3
66	Творчество - это возможность выразить себя через различные виды творчества: живопись, литература, музыка, танец и др. Творчество помогает раскрыть свой потенциал и найти новые способы самовыражения.	3
67	Граф Илья Андреич вышел из предводителей, потому что эта должность была сопряжена с слишком большими расходами. Но дела его всё не поправлялись. Часто Наташа и Николай видели тайные, беспокойные переговоры родителей.	2
68	Петя! Петька! - закричала она ему, - вези меня вниз. - Петя подбежал к ней и подставил спину. Она вскочила на него, обхватив его шею руками и он подпрыгивая побежал с ней. - Нет, не надо - остров Мадагаскар, - проговорила она и, соскочив с него, пошла вниз.	1
69	Осенью 1814-го года Николай женился на княжне Марье и с женой, матерью и Соней переехал на житье в Лысые Горы. В три года он, не продавая именья жены, уплатил оставшиеся долги и, получив небольшое наследство после умершей кузины, заплатил и долг Пьеру.	2
\.


--
-- Data for Name: tier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tier (id, name, correct_rate_ratio, speed_ratio) FROM stdin;
1	hard	0.5	0.75
2	middle	0.3	0.5
3	easy	0.15	0.3
\.


--
-- Name: client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.client_id_seq', 1, false);


--
-- Name: refresh_token_storage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.refresh_token_storage_id_seq', 1, false);


--
-- Name: result_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.result_id_seq', 1, false);


--
-- Name: text_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.text_id_seq', 69, true);


--
-- Name: tier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tier_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: client client_nickname_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_nickname_key UNIQUE (nickname);


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- Name: refresh_token_storage refresh_token_storage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.refresh_token_storage
    ADD CONSTRAINT refresh_token_storage_pkey PRIMARY KEY (id);


--
-- Name: result result_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_pkey PRIMARY KEY (id);


--
-- Name: text text_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.text
    ADD CONSTRAINT text_pkey PRIMARY KEY (id);


--
-- Name: tier tier_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tier
    ADD CONSTRAINT tier_pkey PRIMARY KEY (id);


--
-- Name: result result_text_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_text_id_fkey FOREIGN KEY (text_id) REFERENCES public.text(id);


--
-- Name: result result_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.client(id);


--
-- Name: text text_tier_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.text
    ADD CONSTRAINT text_tier_fkey FOREIGN KEY (tier) REFERENCES public.tier(id);


--
-- PostgreSQL database dump complete
--

