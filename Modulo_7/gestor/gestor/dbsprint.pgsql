--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Ubuntu 15.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 15.3 (Ubuntu 15.3-1.pgdg20.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: clinicapp_funcionario; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.clinicapp_funcionario (
    rut character varying(11) NOT NULL,
    nombre character varying(40) NOT NULL,
    apellidos character varying(70) NOT NULL,
    "género" character varying(20) NOT NULL,
    fono character varying(15) NOT NULL,
    "dirección" character varying(50) NOT NULL,
    mail character varying(60) NOT NULL,
    "contraseña" character varying(32) NOT NULL,
    cargo character varying(100) NOT NULL,
    especialidad character varying(100) NOT NULL,
    vigencia boolean NOT NULL
);


ALTER TABLE public.clinicapp_funcionario OWNER TO admin;

--
-- Name: clinicapp_paciente; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.clinicapp_paciente (
    rut character varying(11) NOT NULL,
    nombre character varying(40) NOT NULL,
    apellidos character varying(70) NOT NULL,
    "género" character varying(20) NOT NULL,
    fono character varying(15) NOT NULL,
    "dirección" character varying(50) NOT NULL,
    mail character varying(60) NOT NULL,
    "previsión" character varying(20) NOT NULL,
    convenio character varying(40) NOT NULL
);


ALTER TABLE public.clinicapp_paciente OWNER TO admin;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: gestor_app_prioridad; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.gestor_app_prioridad (
    id bigint NOT NULL,
    nombre character varying(5)
);


ALTER TABLE public.gestor_app_prioridad OWNER TO admin;

--
-- Name: gestor_app_prioridad_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.gestor_app_prioridad ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.gestor_app_prioridad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: gestor_app_tarea; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.gestor_app_tarea (
    id bigint NOT NULL,
    "título" character varying(30) NOT NULL,
    "descripción" character varying(200) NOT NULL,
    estado character varying(11) NOT NULL,
    "categoría" character varying(7) NOT NULL,
    usuario_id integer,
    vencimiento_fecha date,
    vencimiento_hora time without time zone,
    "observación" character varying(1024),
    prioridad_id bigint
);


ALTER TABLE public.gestor_app_tarea OWNER TO admin;

--
-- Name: gestor_app_tarea_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.gestor_app_tarea ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.gestor_app_tarea_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
1	usuario_normal
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	33
2	1	34
3	1	35
4	1	36
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add funcionario	7	add_funcionario
26	Can change funcionario	7	change_funcionario
27	Can delete funcionario	7	delete_funcionario
28	Can view funcionario	7	view_funcionario
29	Can add paciente	8	add_paciente
30	Can change paciente	8	change_paciente
31	Can delete paciente	8	delete_paciente
32	Can view paciente	8	view_paciente
33	Can add tarea	9	add_tarea
34	Can change tarea	9	change_tarea
35	Can delete tarea	9	delete_tarea
36	Can view tarea	9	view_tarea
37	Can add prioridad	10	add_prioridad
38	Can change prioridad	10	change_prioridad
39	Can delete prioridad	10	delete_prioridad
40	Can view prioridad	10	view_prioridad
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$rreXcB0qOv2aTzIb0WmRCE$StlJFyZtV9+zhwj7XIfugnWUZCEfsuHY6dCfgz3OYwo=	2023-07-21 22:48:59.642392-04	t	admin				t	t	2023-06-22 21:31:39.730076-04
2	pbkdf2_sha256$600000$35XmEdr70J4NBw9wVVxchF$uePxd2rwkXUFp0fnFK30QJHTBEYCRWClG+dfmlYtIdQ=	2023-07-21 22:49:26.106739-04	f	rodrigolfh	Rodrigo	Fuenzalida	dr.rodrigofuenzalida@gmail.com	t	t	2023-06-24 18:36:46-04
3	pbkdf2_sha256$600000$dPEVJACDQpMOjvr1oPb8af$5PFpxwQaS3gFtgwOuefbB85gBDfTblMyNmHALhHv3dU=	\N	f	rodrigolfh123	Rodrigo	Fuenzalida	dr.rodrigofuenzalida@gmail.com	f	t	2023-06-24 18:50:05.56039-04
5	pbkdf2_sha256$600000$jLUbb8qmMaGVEkTL5nY1SE$H2kM7lks7nclRj8giv4P0gOb9VcWIr+GHxSaJa0sjHU=	\N	f	rodrigo2	rodrigo	fuenzalida	nonoknk@gmail.com	f	t	2023-06-27 15:20:12.439404-04
4	pbkdf2_sha256$600000$5xmYHYoSpgXiFA4udAoEWZ$v5e9sdiQ8yp4lwBV2SFIwrQSD4x1R797ws36L4cP+0s=	2023-07-02 20:11:59.468329-04	f	rodrigo	Rodrigo	Fuenzalida	rodrigo@gomail.com	f	t	2023-06-27 15:19:39.093326-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
1	3	1
2	4	1
3	5	1
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: clinicapp_funcionario; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.clinicapp_funcionario (rut, nombre, apellidos, "género", fono, "dirección", mail, "contraseña", cargo, especialidad, vigencia) FROM stdin;
\.


--
-- Data for Name: clinicapp_paciente; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.clinicapp_paciente (rut, nombre, apellidos, "género", fono, "dirección", mail, "previsión", convenio) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-06-24 18:33:22.361199-04	1	usuario_normal	1	[{"added": {}}]	3	1
2	2023-06-27 10:30:45.860843-04	2	rodrigolfh	2	[{"changed": {"fields": ["password"]}}]	4	1
3	2023-06-27 10:31:27.451215-04	2	rodrigolfh	2	[{"changed": {"fields": ["Staff status"]}}]	4	1
4	2023-07-21 22:21:22.411009-04	1	Prioridad object (1)	1	[{"added": {}}]	10	1
5	2023-07-21 22:21:29.286273-04	2	Prioridad object (2)	1	[{"added": {}}]	10	1
6	2023-07-21 22:21:34.445214-04	3	Prioridad object (3)	1	[{"added": {}}]	10	1
7	2023-07-21 22:25:24.974394-04	4	Alta	1	[{"added": {}}]	10	1
8	2023-07-21 22:25:30.272037-04	5	Media	1	[{"added": {}}]	10	1
9	2023-07-21 22:25:35.224886-04	6	Baja	1	[{"added": {}}]	10	1
10	2023-07-21 22:25:49.403314-04	3	B	3		10	1
11	2023-07-21 22:25:49.420669-04	2	M	3		10	1
12	2023-07-21 22:25:49.432008-04	1	A	3		10	1
13	2023-07-21 22:28:14.129513-04	22	oihihoih2	2	[{"changed": {"fields": ["Prioridad"]}}]	9	1
14	2023-07-21 22:28:19.528171-04	19	INTENTO	2	[{"changed": {"fields": ["Prioridad"]}}]	9	1
15	2023-07-21 22:28:48.047725-04	19	INTENTO	3		9	1
16	2023-07-21 22:28:48.056323-04	18	una tarea	3		9	1
17	2023-07-21 22:28:48.067549-04	17	otra tarea	3		9	1
18	2023-07-21 22:28:48.078516-04	16	otra tarea 123	3		9	1
19	2023-07-21 22:28:48.089695-04	15	una tarea	3		9	1
20	2023-07-21 22:28:48.100889-04	10	una tareabla bla	3		9	1
21	2023-07-21 22:28:48.112122-04	9	noknokn	3		9	1
22	2023-07-21 22:28:48.123275-04	8	tarea	3		9	1
23	2023-07-21 22:28:48.134603-04	5	bla bla	3		9	1
24	2023-07-21 22:28:48.145827-04	4	bla bla	3		9	1
25	2023-07-21 22:28:48.157038-04	3	Una tarea	3		9	1
26	2023-07-21 22:28:48.168341-04	2	Una tarea	3		9	1
27	2023-07-21 22:28:48.179576-04	1	Una tarea	3		9	1
28	2023-07-21 22:28:52.824388-04	22	oihihoih2	2	[]	9	1
29	2023-07-21 22:28:58.990767-04	21	oijojojoij	2	[{"changed": {"fields": ["Prioridad"]}}]	9	1
30	2023-07-21 22:29:08.446192-04	20	ohoihoih	2	[{"changed": {"fields": ["Usuario", "Prioridad"]}}]	9	1
31	2023-07-21 22:29:12.573902-04	22	oihihoih2	2	[]	9	1
32	2023-07-21 22:43:12.738073-04	6	Baja	3		10	1
33	2023-07-21 22:49:04.862862-04	7	Baja	1	[{"added": {}}]	10	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	clinicapp	funcionario
8	clinicapp	paciente
9	gestor_app	tarea
10	gestor_app	prioridad
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-06-22 21:29:49.629119-04
2	auth	0001_initial	2023-06-22 21:29:50.264795-04
3	admin	0001_initial	2023-06-22 21:29:50.412923-04
4	admin	0002_logentry_remove_auto_add	2023-06-22 21:29:50.452776-04
5	admin	0003_logentry_add_action_flag_choices	2023-06-22 21:29:50.486293-04
6	contenttypes	0002_remove_content_type_name	2023-06-22 21:29:50.556018-04
7	auth	0002_alter_permission_name_max_length	2023-06-22 21:29:50.585509-04
8	auth	0003_alter_user_email_max_length	2023-06-22 21:29:50.619052-04
9	auth	0004_alter_user_username_opts	2023-06-22 21:29:50.653229-04
10	auth	0005_alter_user_last_login_null	2023-06-22 21:29:50.68475-04
11	auth	0006_require_contenttypes_0002	2023-06-22 21:29:50.702696-04
12	auth	0007_alter_validators_add_error_messages	2023-06-22 21:29:50.736045-04
13	auth	0008_alter_user_username_max_length	2023-06-22 21:29:50.794083-04
14	auth	0009_alter_user_last_name_max_length	2023-06-22 21:29:50.831564-04
15	auth	0010_alter_group_name_max_length	2023-06-22 21:29:50.873577-04
16	auth	0011_update_proxy_permissions	2023-06-22 21:29:50.914766-04
17	auth	0012_alter_user_first_name_max_length	2023-06-22 21:29:50.95192-04
18	clinicapp	0001_initial	2023-06-22 21:29:51.277349-04
19	sessions	0001_initial	2023-06-22 21:29:51.392517-04
20	gestor_app	0001_initial	2023-06-24 18:30:35.003889-04
21	gestor_app	0002_tarea_usuario	2023-06-24 21:05:43.420703-04
22	gestor_app	0003_remove_tarea_vencimiento	2023-06-26 02:21:11.829829-04
23	gestor_app	0004_tarea_vencimiento_fecha_tarea_vencimiento_hora_and_more	2023-06-29 21:43:51.680111-04
24	gestor_app	0005_tarea_observación	2023-07-03 18:24:21.947342-04
25	gestor_app	0006_prioridad_tarea_prioridad	2023-07-21 22:19:18.032775-04
26	gestor_app	0007_alter_prioridad_nombre	2023-07-21 22:25:03.047257-04
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
cnhgxm4b0eeb2vx3upxxoicguui81uzr	.eJxVjMsOwiAQRf-FtSF0eLt07zeQYQCpGkhKuzL-uzbpQrf3nHNfLOC21rCNvIQ5sTMDdvrdItIjtx2kO7Zb59TbusyR7wo_6ODXnvLzcrh_BxVH_dYCXEENaHSOxkgFxnrvLBTtJnJSiSllhSCLKwk8SBOzBRI6aVVMJGLvD7xQN08:1qN2gQ:3gTFUT_zYq8QnIklfxKbAtqBZ5PCRdQ5vEDgLSS4mvc	2023-08-04 22:49:26.120389-04
4lt9zhulnz2dh5zawpjb3mz2pir2tvl6	.eJxVjEEOwiAQRe_C2pCODQO4dO8ZyDADUjWQlHbVeHdt0oVu_3vvbyrQupSw9jSHSdRFgTr9bpH4meoO5EH13jS3usxT1LuiD9r1rUl6XQ_376BQL9_aWATJoyAxOuv9QGDFRbSChn2WnMEnipjGczZk0AEiAA_oWZIBVu8P6e44Hg:1qEFMR:OxE7LJz_DINIl__8sPne7o1vXjdFFDF6KOAz-fMMSEE	2023-07-11 16:32:27.429298-04
nfpvnf30q0lw2gylis7nzuyj2baxesnl	.eJxVjDsOwjAQBe_iGln-ZY0p6XMGy7tr4wBypDipEHeHSCmgfTPzXiKmba1x63mJE4uLcOL0u2GiR2474Htqt1nS3NZlQrkr8qBdjjPn5_Vw_w5q6vVbF3YOFJH2A7NVxqYChiCgDUoprzlnC4jsyZKDAECDgVII7BmVDijeH-KnN84:1qEwfb:itjdQ-1_3qZ5SsZZbFNqNrwjbOBcw60F_aiYWCTb0KM	2023-07-13 14:47:07.539774-04
bcfedvdszseoqnw3b7oeiaytlz1653h2	.eJxVjEEOwiAQRe_C2pCODQO4dO8ZyDADUjWQlHbVeHdt0oVu_3vvbyrQupSw9jSHSdRFgTr9bpH4meoO5EH13jS3usxT1LuiD9r1rUl6XQ_376BQL9_aWATJoyAxOuv9QGDFRbSChn2WnMEnipjGczZk0AEiAA_oWZIBVu8P6e44Hg:1qGS4G:2HIpa878o9LKuwvrq1eF7FmzQ4cCxZaN2m7Yp_QP55A	2023-07-17 18:30:48.727431-04
u3c7hc13cn5q0jf9zbwmb13820b1lcso	.eJxVjEEOwiAQRe_C2pCODQO4dO8ZyDADUjWQlHbVeHdt0oVu_3vvbyrQupSw9jSHSdRFgTr9bpH4meoO5EH13jS3usxT1LuiD9r1rUl6XQ_376BQL9_aWATJoyAxOuv9QGDFRbSChn2WnMEnipjGczZk0AEiAA_oWZIBVu8P6e44Hg:1qGlfi:SO5aK-7zuGXO6go8w_1J_BcRpACr9O6Dno_UqsOZg-E	2023-07-18 15:26:46.619667-04
p9hnlzi3x836whoyx0i7vnjxt9ynt5q8	.eJxVjEEOwiAQRe_C2pCODQO4dO8ZyDADUjWQlHbVeHdt0oVu_3vvbyrQupSw9jSHSdRFgTr9bpH4meoO5EH13jS3usxT1LuiD9r1rUl6XQ_376BQL9_aWATJoyAxOuv9QGDFRbSChn2WnMEnipjGczZk0AEiAA_oWZIBVu8P6e44Hg:1qN23e:3o-6pJogETC4i-7ExF5lR8HXhqA9sKtSsabDi7pU-ho	2023-08-04 22:09:22.994718-04
\.


--
-- Data for Name: gestor_app_prioridad; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.gestor_app_prioridad (id, nombre) FROM stdin;
4	Alta
5	Media
7	Baja
\.


--
-- Data for Name: gestor_app_tarea; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.gestor_app_tarea (id, "título", "descripción", estado, "categoría", usuario_id, vencimiento_fecha, vencimiento_hora, "observación", prioridad_id) FROM stdin;
21	oijojojoij	ojojpjpj	PENDIENTE	TRABAJO	2	2023-07-13	00:00:00	oihoih	7
22	oihihoih2	oihiohoih	PENDIENTE	HOGAR	2	2023-07-04	00:00:00	ohoihoihioh	4
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 4, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 3, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 33, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: gestor_app_prioridad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.gestor_app_prioridad_id_seq', 7, true);


--
-- Name: gestor_app_tarea_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.gestor_app_tarea_id_seq', 22, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: clinicapp_funcionario clinicapp_funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.clinicapp_funcionario
    ADD CONSTRAINT clinicapp_funcionario_pkey PRIMARY KEY (rut);


--
-- Name: clinicapp_paciente clinicapp_paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.clinicapp_paciente
    ADD CONSTRAINT clinicapp_paciente_pkey PRIMARY KEY (rut);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: gestor_app_prioridad gestor_app_prioridad_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gestor_app_prioridad
    ADD CONSTRAINT gestor_app_prioridad_pkey PRIMARY KEY (id);


--
-- Name: gestor_app_tarea gestor_app_tarea_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gestor_app_tarea
    ADD CONSTRAINT gestor_app_tarea_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: clinicapp_funcionario_rut_a9074c36_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX clinicapp_funcionario_rut_a9074c36_like ON public.clinicapp_funcionario USING btree (rut varchar_pattern_ops);


--
-- Name: clinicapp_paciente_rut_2d893690_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX clinicapp_paciente_rut_2d893690_like ON public.clinicapp_paciente USING btree (rut varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: gestor_app_tarea_prioridad_id_6eaaae62; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX gestor_app_tarea_prioridad_id_6eaaae62 ON public.gestor_app_tarea USING btree (prioridad_id);


--
-- Name: gestor_app_tarea_usuario_id_0467a52e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX gestor_app_tarea_usuario_id_0467a52e ON public.gestor_app_tarea USING btree (usuario_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gestor_app_tarea gestor_app_tarea_prioridad_id_6eaaae62_fk_gestor_ap; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gestor_app_tarea
    ADD CONSTRAINT gestor_app_tarea_prioridad_id_6eaaae62_fk_gestor_ap FOREIGN KEY (prioridad_id) REFERENCES public.gestor_app_prioridad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gestor_app_tarea gestor_app_tarea_usuario_id_0467a52e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gestor_app_tarea
    ADD CONSTRAINT gestor_app_tarea_usuario_id_0467a52e_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
GRANT ALL ON SCHEMA public TO admin;


--
-- PostgreSQL database dump complete
--

