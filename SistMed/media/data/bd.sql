--
-- PostgreSQL database dump
--

-- Started on 2011-11-28 21:57:19

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- TOC entry 419 (class 2612 OID 16386)
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: postgres
--

CREATE PROCEDURAL LANGUAGE plpgsql;


ALTER PROCEDURAL LANGUAGE plpgsql OWNER TO postgres;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 1635 (class 1259 OID 26251)
-- Dependencies: 3
-- Name: GestionTurnos_administrativos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_administrativos" (
    usuarios_ptr_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_administrativos" OWNER TO wyrven;

--
-- TOC entry 1639 (class 1259 OID 26281)
-- Dependencies: 3
-- Name: GestionTurnos_consultorios; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_consultorios" (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL
);


ALTER TABLE public."GestionTurnos_consultorios" OWNER TO wyrven;

--
-- TOC entry 1638 (class 1259 OID 26279)
-- Dependencies: 3 1639
-- Name: GestionTurnos_consultorios_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_consultorios_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_consultorios_id_seq" OWNER TO wyrven;

--
-- TOC entry 2152 (class 0 OID 0)
-- Dependencies: 1638
-- Name: GestionTurnos_consultorios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_consultorios_id_seq" OWNED BY "GestionTurnos_consultorios".id;


--
-- TOC entry 2153 (class 0 OID 0)
-- Dependencies: 1638
-- Name: GestionTurnos_consultorios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_consultorios_id_seq"', 1, false);


--
-- TOC entry 1643 (class 1259 OID 26302)
-- Dependencies: 3
-- Name: GestionTurnos_diasatencion; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_diasatencion" (
    id integer NOT NULL,
    fecha date NOT NULL,
    cant_turno integer NOT NULL,
    medico_id integer NOT NULL,
    horario_atenc_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_diasatencion" OWNER TO wyrven;

--
-- TOC entry 1642 (class 1259 OID 26300)
-- Dependencies: 1643 3
-- Name: GestionTurnos_diasatencion_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_diasatencion_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_diasatencion_id_seq" OWNER TO wyrven;

--
-- TOC entry 2154 (class 0 OID 0)
-- Dependencies: 1642
-- Name: GestionTurnos_diasatencion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_diasatencion_id_seq" OWNED BY "GestionTurnos_diasatencion".id;


--
-- TOC entry 2155 (class 0 OID 0)
-- Dependencies: 1642
-- Name: GestionTurnos_diasatencion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_diasatencion_id_seq"', 1, false);


--
-- TOC entry 1630 (class 1259 OID 26205)
-- Dependencies: 3
-- Name: GestionTurnos_expecialidades; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_expecialidades" (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL
);


ALTER TABLE public."GestionTurnos_expecialidades" OWNER TO wyrven;

--
-- TOC entry 1629 (class 1259 OID 26203)
-- Dependencies: 1630 3
-- Name: GestionTurnos_expecialidades_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_expecialidades_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_expecialidades_id_seq" OWNER TO wyrven;

--
-- TOC entry 2156 (class 0 OID 0)
-- Dependencies: 1629
-- Name: GestionTurnos_expecialidades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_expecialidades_id_seq" OWNED BY "GestionTurnos_expecialidades".id;


--
-- TOC entry 2157 (class 0 OID 0)
-- Dependencies: 1629
-- Name: GestionTurnos_expecialidades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_expecialidades_id_seq"', 11, true);


--
-- TOC entry 1637 (class 1259 OID 26263)
-- Dependencies: 3
-- Name: GestionTurnos_expecialidadesmedicos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_expecialidadesmedicos" (
    id integer NOT NULL,
    codigo_medico_id integer NOT NULL,
    cod_expecialidad_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_expecialidadesmedicos" OWNER TO wyrven;

--
-- TOC entry 1636 (class 1259 OID 26261)
-- Dependencies: 1637 3
-- Name: GestionTurnos_expecialidadesmedicos_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_expecialidadesmedicos_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_expecialidadesmedicos_id_seq" OWNER TO wyrven;

--
-- TOC entry 2158 (class 0 OID 0)
-- Dependencies: 1636
-- Name: GestionTurnos_expecialidadesmedicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_expecialidadesmedicos_id_seq" OWNED BY "GestionTurnos_expecialidadesmedicos".id;


--
-- TOC entry 2159 (class 0 OID 0)
-- Dependencies: 1636
-- Name: GestionTurnos_expecialidadesmedicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_expecialidadesmedicos_id_seq"', 3, true);


--
-- TOC entry 1641 (class 1259 OID 26289)
-- Dependencies: 3
-- Name: GestionTurnos_horarioatencion; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_horarioatencion" (
    id integer NOT NULL,
    dia character varying(4) NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fin time without time zone NOT NULL,
    duracion_turno integer NOT NULL,
    intervalo integer NOT NULL,
    medico_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_horarioatencion" OWNER TO wyrven;

--
-- TOC entry 1640 (class 1259 OID 26287)
-- Dependencies: 3 1641
-- Name: GestionTurnos_horarioatencion_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_horarioatencion_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_horarioatencion_id_seq" OWNER TO wyrven;

--
-- TOC entry 2160 (class 0 OID 0)
-- Dependencies: 1640
-- Name: GestionTurnos_horarioatencion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_horarioatencion_id_seq" OWNED BY "GestionTurnos_horarioatencion".id;


--
-- TOC entry 2161 (class 0 OID 0)
-- Dependencies: 1640
-- Name: GestionTurnos_horarioatencion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_horarioatencion_id_seq"', 3, true);


--
-- TOC entry 1633 (class 1259 OID 26231)
-- Dependencies: 3
-- Name: GestionTurnos_medicos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_medicos" (
    usuarios_ptr_id integer NOT NULL,
    matricula character varying(30) NOT NULL
);


ALTER TABLE public."GestionTurnos_medicos" OWNER TO wyrven;

--
-- TOC entry 1634 (class 1259 OID 26241)
-- Dependencies: 3
-- Name: GestionTurnos_pacientes; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_pacientes" (
    usuarios_ptr_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_pacientes" OWNER TO wyrven;

--
-- TOC entry 1647 (class 1259 OID 26341)
-- Dependencies: 3
-- Name: GestionTurnos_solitudesturnos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_solitudesturnos" (
    id integer NOT NULL,
    fecha_solicitud date NOT NULL,
    fecha_requerida date NOT NULL,
    estado character varying(1) NOT NULL,
    comentarios text NOT NULL,
    codigo_paciente_id integer NOT NULL,
    codigo_medico_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_solitudesturnos" OWNER TO wyrven;

--
-- TOC entry 1646 (class 1259 OID 26339)
-- Dependencies: 1647 3
-- Name: GestionTurnos_solitudesturnos_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_solitudesturnos_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_solitudesturnos_id_seq" OWNER TO wyrven;

--
-- TOC entry 2162 (class 0 OID 0)
-- Dependencies: 1646
-- Name: GestionTurnos_solitudesturnos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_solitudesturnos_id_seq" OWNED BY "GestionTurnos_solitudesturnos".id;


--
-- TOC entry 2163 (class 0 OID 0)
-- Dependencies: 1646
-- Name: GestionTurnos_solitudesturnos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_solitudesturnos_id_seq"', 1, false);


--
-- TOC entry 1628 (class 1259 OID 26197)
-- Dependencies: 3
-- Name: GestionTurnos_tipousuario; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_tipousuario" (
    id integer NOT NULL,
    nombre character varying(15) NOT NULL
);


ALTER TABLE public."GestionTurnos_tipousuario" OWNER TO wyrven;

--
-- TOC entry 1627 (class 1259 OID 26195)
-- Dependencies: 1628 3
-- Name: GestionTurnos_tipousuario_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_tipousuario_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_tipousuario_id_seq" OWNER TO wyrven;

--
-- TOC entry 2164 (class 0 OID 0)
-- Dependencies: 1627
-- Name: GestionTurnos_tipousuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_tipousuario_id_seq" OWNED BY "GestionTurnos_tipousuario".id;


--
-- TOC entry 2165 (class 0 OID 0)
-- Dependencies: 1627
-- Name: GestionTurnos_tipousuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_tipousuario_id_seq"', 6, true);


--
-- TOC entry 1645 (class 1259 OID 26320)
-- Dependencies: 3
-- Name: GestionTurnos_turnos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_turnos" (
    id integer NOT NULL,
    fecha date NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fin time without time zone NOT NULL,
    comentarios text NOT NULL,
    paciente_id integer NOT NULL,
    medico_id integer NOT NULL
);


ALTER TABLE public."GestionTurnos_turnos" OWNER TO wyrven;

--
-- TOC entry 1644 (class 1259 OID 26318)
-- Dependencies: 1645 3
-- Name: GestionTurnos_turnos_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_turnos_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_turnos_id_seq" OWNER TO wyrven;

--
-- TOC entry 2166 (class 0 OID 0)
-- Dependencies: 1644
-- Name: GestionTurnos_turnos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_turnos_id_seq" OWNED BY "GestionTurnos_turnos".id;


--
-- TOC entry 2167 (class 0 OID 0)
-- Dependencies: 1644
-- Name: GestionTurnos_turnos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_turnos_id_seq"', 1, false);


--
-- TOC entry 1632 (class 1259 OID 26213)
-- Dependencies: 3
-- Name: GestionTurnos_usuarios; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "GestionTurnos_usuarios" (
    id integer NOT NULL,
    dni integer NOT NULL,
    sexo character varying(1) NOT NULL,
    telefono character varying(20) NOT NULL,
    direccion character varying(60) NOT NULL,
    tipo_usuario_id integer NOT NULL,
    user_id integer NOT NULL,
    tipo_doc character varying(5)
);


ALTER TABLE public."GestionTurnos_usuarios" OWNER TO wyrven;

--
-- TOC entry 1631 (class 1259 OID 26211)
-- Dependencies: 1632 3
-- Name: GestionTurnos_usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "GestionTurnos_usuarios_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."GestionTurnos_usuarios_id_seq" OWNER TO wyrven;

--
-- TOC entry 2168 (class 0 OID 0)
-- Dependencies: 1631
-- Name: GestionTurnos_usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "GestionTurnos_usuarios_id_seq" OWNED BY "GestionTurnos_usuarios".id;


--
-- TOC entry 2169 (class 0 OID 0)
-- Dependencies: 1631
-- Name: GestionTurnos_usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"GestionTurnos_usuarios_id_seq"', 11, true);


--
-- TOC entry 1651 (class 1259 OID 26380)
-- Dependencies: 3
-- Name: HistoriaClinica_antecedentesperinatales; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_antecedentesperinatales" (
    id integer NOT NULL,
    hist_clinica_id integer NOT NULL,
    enbarazo_nro integer NOT NULL,
    duracion_embarazo integer NOT NULL,
    controles character varying(1) NOT NULL,
    parto_normal character varying(1) NOT NULL,
    peso double precision NOT NULL,
    talla double precision NOT NULL,
    patologias character varying(1) NOT NULL,
    atencion_medica character varying(1) NOT NULL,
    otros_datos text NOT NULL
);


ALTER TABLE public."HistoriaClinica_antecedentesperinatales" OWNER TO wyrven;

--
-- TOC entry 1650 (class 1259 OID 26378)
-- Dependencies: 3 1651
-- Name: HistoriaClinica_antecedentesperinatales_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_antecedentesperinatales_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_antecedentesperinatales_id_seq" OWNER TO wyrven;

--
-- TOC entry 2170 (class 0 OID 0)
-- Dependencies: 1650
-- Name: HistoriaClinica_antecedentesperinatales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_antecedentesperinatales_id_seq" OWNED BY "HistoriaClinica_antecedentesperinatales".id;


--
-- TOC entry 2171 (class 0 OID 0)
-- Dependencies: 1650
-- Name: HistoriaClinica_antecedentesperinatales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_antecedentesperinatales_id_seq"', 1, false);


--
-- TOC entry 1659 (class 1259 OID 26459)
-- Dependencies: 3
-- Name: HistoriaClinica_cabeza; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_cabeza" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    craneo character varying(1) NOT NULL,
    fontanelas_y_suturas character varying(1) NOT NULL,
    facie character varying(1) NOT NULL,
    parpados character varying(1) NOT NULL,
    conjuntivas character varying(1) NOT NULL,
    globo_ocular_mov character varying(1) NOT NULL,
    vision character varying(1) NOT NULL,
    nariz_fosas_nasales character varying(1) NOT NULL,
    labios character varying(1) NOT NULL,
    dientes character varying(1) NOT NULL,
    lengua character varying(1) NOT NULL,
    mucosa_bucofaringea character varying(1) NOT NULL,
    amigdalas character varying(1) NOT NULL,
    pabellones_auriculares character varying(1) NOT NULL,
    cond_audit_externo character varying(1) NOT NULL,
    timpanos character varying(1) NOT NULL,
    audicion character varying(1) NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public."HistoriaClinica_cabeza" OWNER TO wyrven;

--
-- TOC entry 1658 (class 1259 OID 26457)
-- Dependencies: 3 1659
-- Name: HistoriaClinica_cabeza_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_cabeza_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_cabeza_id_seq" OWNER TO wyrven;

--
-- TOC entry 2172 (class 0 OID 0)
-- Dependencies: 1658
-- Name: HistoriaClinica_cabeza_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_cabeza_id_seq" OWNED BY "HistoriaClinica_cabeza".id;


--
-- TOC entry 2173 (class 0 OID 0)
-- Dependencies: 1658
-- Name: HistoriaClinica_cabeza_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_cabeza_id_seq"', 2, true);


--
-- TOC entry 1667 (class 1259 OID 26543)
-- Dependencies: 3
-- Name: HistoriaClinica_consultamedica; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_consultamedica" (
    id integer NOT NULL,
    hist_clinica_id integer NOT NULL,
    fecha timestamp with time zone NOT NULL,
    observaciones text NOT NULL,
    medico_id integer NOT NULL
);


ALTER TABLE public."HistoriaClinica_consultamedica" OWNER TO wyrven;

--
-- TOC entry 1666 (class 1259 OID 26541)
-- Dependencies: 1667 3
-- Name: HistoriaClinica_consultamedica_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_consultamedica_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_consultamedica_id_seq" OWNER TO wyrven;

--
-- TOC entry 2174 (class 0 OID 0)
-- Dependencies: 1666
-- Name: HistoriaClinica_consultamedica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_consultamedica_id_seq" OWNED BY "HistoriaClinica_consultamedica".id;


--
-- TOC entry 2175 (class 0 OID 0)
-- Dependencies: 1666
-- Name: HistoriaClinica_consultamedica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_consultamedica_id_seq"', 1, false);


--
-- TOC entry 1661 (class 1259 OID 26475)
-- Dependencies: 3
-- Name: HistoriaClinica_cuello; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_cuello" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    inspecion character varying(250) NOT NULL,
    palpacion character varying(250) NOT NULL,
    percucion character varying(250) NOT NULL,
    ausculacion character varying(250) NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public."HistoriaClinica_cuello" OWNER TO wyrven;

--
-- TOC entry 1660 (class 1259 OID 26473)
-- Dependencies: 1661 3
-- Name: HistoriaClinica_cuello_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_cuello_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_cuello_id_seq" OWNER TO wyrven;

--
-- TOC entry 2176 (class 0 OID 0)
-- Dependencies: 1660
-- Name: HistoriaClinica_cuello_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_cuello_id_seq" OWNED BY "HistoriaClinica_cuello".id;


--
-- TOC entry 2177 (class 0 OID 0)
-- Dependencies: 1660
-- Name: HistoriaClinica_cuello_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_cuello_id_seq"', 2, true);


--
-- TOC entry 1665 (class 1259 OID 26527)
-- Dependencies: 3
-- Name: HistoriaClinica_diagnostico; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_diagnostico" (
    id integer NOT NULL,
    hist_clinica_id integer NOT NULL,
    fecha date NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public."HistoriaClinica_diagnostico" OWNER TO wyrven;

--
-- TOC entry 1664 (class 1259 OID 26525)
-- Dependencies: 3 1665
-- Name: HistoriaClinica_diagnostico_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_diagnostico_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_diagnostico_id_seq" OWNER TO wyrven;

--
-- TOC entry 2178 (class 0 OID 0)
-- Dependencies: 1664
-- Name: HistoriaClinica_diagnostico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_diagnostico_id_seq" OWNED BY "HistoriaClinica_diagnostico".id;


--
-- TOC entry 2179 (class 0 OID 0)
-- Dependencies: 1664
-- Name: HistoriaClinica_diagnostico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_diagnostico_id_seq"', 1, false);


--
-- TOC entry 1655 (class 1259 OID 26425)
-- Dependencies: 3
-- Name: HistoriaClinica_examenbase; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_examenbase" (
    id integer NOT NULL,
    hist_clinica_id integer NOT NULL,
    fecha timestamp with time zone NOT NULL,
    temp_corporal double precision NOT NULL,
    pres_art_sist integer NOT NULL,
    pres_art_diast integer NOT NULL,
    frec_respiratoria integer NOT NULL,
    pulso integer NOT NULL,
    peso_medio double precision NOT NULL,
    altura_media double precision NOT NULL,
    peso double precision NOT NULL,
    altura double precision NOT NULL,
    talla character varying(30) NOT NULL,
    bmi double precision NOT NULL,
    imprecion_general text NOT NULL
);


ALTER TABLE public."HistoriaClinica_examenbase" OWNER TO wyrven;

--
-- TOC entry 1654 (class 1259 OID 26423)
-- Dependencies: 3 1655
-- Name: HistoriaClinica_examenbase_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_examenbase_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_examenbase_id_seq" OWNER TO wyrven;

--
-- TOC entry 2180 (class 0 OID 0)
-- Dependencies: 1654
-- Name: HistoriaClinica_examenbase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_examenbase_id_seq" OWNED BY "HistoriaClinica_examenbase".id;


--
-- TOC entry 2181 (class 0 OID 0)
-- Dependencies: 1654
-- Name: HistoriaClinica_examenbase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_examenbase_id_seq"', 2, true);


--
-- TOC entry 1669 (class 1259 OID 26565)
-- Dependencies: 3
-- Name: HistoriaClinica_habitostoxicos; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_habitostoxicos" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    fecha timestamp with time zone NOT NULL,
    alcohol character varying(1) NOT NULL,
    tabaco character varying(1) NOT NULL,
    drogas character varying(1) NOT NULL,
    infuciones character varying(1) NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public."HistoriaClinica_habitostoxicos" OWNER TO wyrven;

--
-- TOC entry 1668 (class 1259 OID 26563)
-- Dependencies: 1669 3
-- Name: HistoriaClinica_habitostoxicos_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_habitostoxicos_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_habitostoxicos_id_seq" OWNER TO wyrven;

--
-- TOC entry 2182 (class 0 OID 0)
-- Dependencies: 1668
-- Name: HistoriaClinica_habitostoxicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_habitostoxicos_id_seq" OWNED BY "HistoriaClinica_habitostoxicos".id;


--
-- TOC entry 2183 (class 0 OID 0)
-- Dependencies: 1668
-- Name: HistoriaClinica_habitostoxicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_habitostoxicos_id_seq"', 1, false);


--
-- TOC entry 1671 (class 1259 OID 26600)
-- Dependencies: 3
-- Name: HistoriaClinica_imagen; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_imagen" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    descripcion text NOT NULL,
    imagen character varying(100) NOT NULL
);


ALTER TABLE public."HistoriaClinica_imagen" OWNER TO wyrven;

--
-- TOC entry 1670 (class 1259 OID 26598)
-- Dependencies: 3 1671
-- Name: HistoriaClinica_imagen_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_imagen_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_imagen_id_seq" OWNER TO wyrven;

--
-- TOC entry 2184 (class 0 OID 0)
-- Dependencies: 1670
-- Name: HistoriaClinica_imagen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_imagen_id_seq" OWNED BY "HistoriaClinica_imagen".id;


--
-- TOC entry 2185 (class 0 OID 0)
-- Dependencies: 1670
-- Name: HistoriaClinica_imagen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_imagen_id_seq"', 2, true);


--
-- TOC entry 1649 (class 1259 OID 26362)
-- Dependencies: 3
-- Name: HistoriaClinica_informacionbasica; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_informacionbasica" (
    id integer NOT NULL,
    fecha_nacimiento timestamp with time zone NOT NULL,
    lugar_nacimiento character varying(60) NOT NULL,
    grupo_sanguineo character varying(3) NOT NULL,
    padre character varying(120) NOT NULL,
    madre character varying(120) NOT NULL,
    obra_social character varying(30) NOT NULL,
    nro_afiliado character varying(10) NOT NULL,
    estado_civil character varying(1) NOT NULL,
    ocupacion character varying(30) NOT NULL,
    religion character varying(30) NOT NULL,
    motivo_consulta text NOT NULL,
    antecedentes_enfermedad_actual text NOT NULL,
    paciente_id integer NOT NULL
);


ALTER TABLE public."HistoriaClinica_informacionbasica" OWNER TO wyrven;

--
-- TOC entry 1648 (class 1259 OID 26360)
-- Dependencies: 1649 3
-- Name: HistoriaClinica_informacionbasica_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_informacionbasica_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_informacionbasica_id_seq" OWNER TO wyrven;

--
-- TOC entry 2186 (class 0 OID 0)
-- Dependencies: 1648
-- Name: HistoriaClinica_informacionbasica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_informacionbasica_id_seq" OWNED BY "HistoriaClinica_informacionbasica".id;


--
-- TOC entry 2187 (class 0 OID 0)
-- Dependencies: 1648
-- Name: HistoriaClinica_informacionbasica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_informacionbasica_id_seq"', 2, true);


--
-- TOC entry 1663 (class 1259 OID 26491)
-- Dependencies: 3
-- Name: HistoriaClinica_otrosestudio; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_otrosestudio" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    fecha date NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public."HistoriaClinica_otrosestudio" OWNER TO wyrven;

--
-- TOC entry 1662 (class 1259 OID 26489)
-- Dependencies: 3 1663
-- Name: HistoriaClinica_otrosestudio_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_otrosestudio_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_otrosestudio_id_seq" OWNER TO wyrven;

--
-- TOC entry 2188 (class 0 OID 0)
-- Dependencies: 1662
-- Name: HistoriaClinica_otrosestudio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_otrosestudio_id_seq" OWNED BY "HistoriaClinica_otrosestudio".id;


--
-- TOC entry 2189 (class 0 OID 0)
-- Dependencies: 1662
-- Name: HistoriaClinica_otrosestudio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_otrosestudio_id_seq"', 1, false);


--
-- TOC entry 1657 (class 1259 OID 26441)
-- Dependencies: 3
-- Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_pielfaneastejidocelularsubcutaneo" (
    id integer NOT NULL,
    examen_fisico_id integer NOT NULL,
    aspecto text NOT NULL,
    dist_pilosa text NOT NULL,
    lesiones text NOT NULL,
    faneras text NOT NULL,
    tejido_cel_subcutaneo text NOT NULL
);


ALTER TABLE public."HistoriaClinica_pielfaneastejidocelularsubcutaneo" OWNER TO wyrven;

--
-- TOC entry 1656 (class 1259 OID 26439)
-- Dependencies: 1657 3
-- Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq" OWNER TO wyrven;

--
-- TOC entry 2190 (class 0 OID 0)
-- Dependencies: 1656
-- Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq" OWNED BY "HistoriaClinica_pielfaneastejidocelularsubcutaneo".id;


--
-- TOC entry 2191 (class 0 OID 0)
-- Dependencies: 1656
-- Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq"', 1, false);


--
-- TOC entry 1653 (class 1259 OID 26412)
-- Dependencies: 3
-- Name: HistoriaClinica_vacuna; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE "HistoriaClinica_vacuna" (
    id integer NOT NULL,
    hist_clinica_id integer NOT NULL,
    fecha timestamp with time zone NOT NULL,
    descripcion character varying(30) NOT NULL,
    tipo_dosis character varying(3) NOT NULL
);


ALTER TABLE public."HistoriaClinica_vacuna" OWNER TO wyrven;

--
-- TOC entry 1652 (class 1259 OID 26410)
-- Dependencies: 1653 3
-- Name: HistoriaClinica_vacuna_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE "HistoriaClinica_vacuna_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."HistoriaClinica_vacuna_id_seq" OWNER TO wyrven;

--
-- TOC entry 2192 (class 0 OID 0)
-- Dependencies: 1652
-- Name: HistoriaClinica_vacuna_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE "HistoriaClinica_vacuna_id_seq" OWNED BY "HistoriaClinica_vacuna".id;


--
-- TOC entry 2193 (class 0 OID 0)
-- Dependencies: 1652
-- Name: HistoriaClinica_vacuna_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('"HistoriaClinica_vacuna_id_seq"', 1, true);


--
-- TOC entry 1611 (class 1259 OID 26063)
-- Dependencies: 3
-- Name: auth_group; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO wyrven;

--
-- TOC entry 1610 (class 1259 OID 26061)
-- Dependencies: 3 1611
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO wyrven;

--
-- TOC entry 2194 (class 0 OID 0)
-- Dependencies: 1610
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- TOC entry 2195 (class 0 OID 0)
-- Dependencies: 1610
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 1609 (class 1259 OID 26048)
-- Dependencies: 3
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO wyrven;

--
-- TOC entry 1608 (class 1259 OID 26046)
-- Dependencies: 1609 3
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO wyrven;

--
-- TOC entry 2196 (class 0 OID 0)
-- Dependencies: 1608
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- TOC entry 2197 (class 0 OID 0)
-- Dependencies: 1608
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 1619 (class 1259 OID 26128)
-- Dependencies: 3
-- Name: auth_message; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_message (
    id integer NOT NULL,
    user_id integer NOT NULL,
    message text NOT NULL
);


ALTER TABLE public.auth_message OWNER TO wyrven;

--
-- TOC entry 1618 (class 1259 OID 26126)
-- Dependencies: 3 1619
-- Name: auth_message_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_message_id_seq OWNER TO wyrven;

--
-- TOC entry 2198 (class 0 OID 0)
-- Dependencies: 1618
-- Name: auth_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_message_id_seq OWNED BY auth_message.id;


--
-- TOC entry 2199 (class 0 OID 0)
-- Dependencies: 1618
-- Name: auth_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_message_id_seq', 2, true);


--
-- TOC entry 1607 (class 1259 OID 26038)
-- Dependencies: 3
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO wyrven;

--
-- TOC entry 1606 (class 1259 OID 26036)
-- Dependencies: 3 1607
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO wyrven;

--
-- TOC entry 2200 (class 0 OID 0)
-- Dependencies: 1606
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- TOC entry 2201 (class 0 OID 0)
-- Dependencies: 1606
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_permission_id_seq', 96, true);


--
-- TOC entry 1617 (class 1259 OID 26108)
-- Dependencies: 3
-- Name: auth_user; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO wyrven;

--
-- TOC entry 1615 (class 1259 OID 26093)
-- Dependencies: 3
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO wyrven;

--
-- TOC entry 1614 (class 1259 OID 26091)
-- Dependencies: 3 1615
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO wyrven;

--
-- TOC entry 2202 (class 0 OID 0)
-- Dependencies: 1614
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- TOC entry 2203 (class 0 OID 0)
-- Dependencies: 1614
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 1616 (class 1259 OID 26106)
-- Dependencies: 3 1617
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO wyrven;

--
-- TOC entry 2204 (class 0 OID 0)
-- Dependencies: 1616
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- TOC entry 2205 (class 0 OID 0)
-- Dependencies: 1616
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_user_id_seq', 12, true);


--
-- TOC entry 1613 (class 1259 OID 26078)
-- Dependencies: 3
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO wyrven;

--
-- TOC entry 1612 (class 1259 OID 26076)
-- Dependencies: 1613 3
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO wyrven;

--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 1612
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 1612
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 1626 (class 1259 OID 26175)
-- Dependencies: 1959 3
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO wyrven;

--
-- TOC entry 1625 (class 1259 OID 26173)
-- Dependencies: 1626 3
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO wyrven;

--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 1625
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 1625
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 4, true);


--
-- TOC entry 1621 (class 1259 OID 26144)
-- Dependencies: 3
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO wyrven;

--
-- TOC entry 1620 (class 1259 OID 26142)
-- Dependencies: 1621 3
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO wyrven;

--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 1620
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 2211 (class 0 OID 0)
-- Dependencies: 1620
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('django_content_type_id_seq', 32, true);


--
-- TOC entry 1622 (class 1259 OID 26157)
-- Dependencies: 3
-- Name: django_session; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO wyrven;

--
-- TOC entry 1624 (class 1259 OID 26167)
-- Dependencies: 3
-- Name: django_site; Type: TABLE; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO wyrven;

--
-- TOC entry 1623 (class 1259 OID 26165)
-- Dependencies: 1624 3
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: wyrven
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO wyrven;

--
-- TOC entry 2212 (class 0 OID 0)
-- Dependencies: 1623
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyrven
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- TOC entry 2213 (class 0 OID 0)
-- Dependencies: 1623
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyrven
--

SELECT pg_catalog.setval('django_site_id_seq', 1, false);


--
-- TOC entry 1964 (class 2604 OID 26284)
-- Dependencies: 1639 1638 1639
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_consultorios" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_consultorios_id_seq"'::regclass);


--
-- TOC entry 1966 (class 2604 OID 26305)
-- Dependencies: 1643 1642 1643
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_diasatencion" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_diasatencion_id_seq"'::regclass);


--
-- TOC entry 1961 (class 2604 OID 26208)
-- Dependencies: 1630 1629 1630
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_expecialidades" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_expecialidades_id_seq"'::regclass);


--
-- TOC entry 1963 (class 2604 OID 26266)
-- Dependencies: 1637 1636 1637
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_expecialidadesmedicos" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_expecialidadesmedicos_id_seq"'::regclass);


--
-- TOC entry 1965 (class 2604 OID 26292)
-- Dependencies: 1641 1640 1641
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_horarioatencion" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_horarioatencion_id_seq"'::regclass);


--
-- TOC entry 1968 (class 2604 OID 26344)
-- Dependencies: 1647 1646 1647
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_solitudesturnos" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_solitudesturnos_id_seq"'::regclass);


--
-- TOC entry 1960 (class 2604 OID 26200)
-- Dependencies: 1628 1627 1628
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_tipousuario" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_tipousuario_id_seq"'::regclass);


--
-- TOC entry 1967 (class 2604 OID 26323)
-- Dependencies: 1645 1644 1645
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_turnos" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_turnos_id_seq"'::regclass);


--
-- TOC entry 1962 (class 2604 OID 26216)
-- Dependencies: 1632 1631 1632
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "GestionTurnos_usuarios" ALTER COLUMN id SET DEFAULT nextval('"GestionTurnos_usuarios_id_seq"'::regclass);


--
-- TOC entry 1970 (class 2604 OID 26383)
-- Dependencies: 1651 1650 1651
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_antecedentesperinatales" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_antecedentesperinatales_id_seq"'::regclass);


--
-- TOC entry 1974 (class 2604 OID 26462)
-- Dependencies: 1658 1659 1659
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_cabeza" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_cabeza_id_seq"'::regclass);


--
-- TOC entry 1978 (class 2604 OID 26546)
-- Dependencies: 1667 1666 1667
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_consultamedica" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_consultamedica_id_seq"'::regclass);


--
-- TOC entry 1975 (class 2604 OID 26478)
-- Dependencies: 1660 1661 1661
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_cuello" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_cuello_id_seq"'::regclass);


--
-- TOC entry 1977 (class 2604 OID 26530)
-- Dependencies: 1664 1665 1665
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_diagnostico" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_diagnostico_id_seq"'::regclass);


--
-- TOC entry 1972 (class 2604 OID 26428)
-- Dependencies: 1654 1655 1655
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_examenbase" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_examenbase_id_seq"'::regclass);


--
-- TOC entry 1979 (class 2604 OID 26568)
-- Dependencies: 1668 1669 1669
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_habitostoxicos" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_habitostoxicos_id_seq"'::regclass);


--
-- TOC entry 1980 (class 2604 OID 26603)
-- Dependencies: 1671 1670 1671
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_imagen" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_imagen_id_seq"'::regclass);


--
-- TOC entry 1969 (class 2604 OID 26365)
-- Dependencies: 1649 1648 1649
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_informacionbasica" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_informacionbasica_id_seq"'::regclass);


--
-- TOC entry 1976 (class 2604 OID 26494)
-- Dependencies: 1662 1663 1663
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_otrosestudio" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_otrosestudio_id_seq"'::regclass);


--
-- TOC entry 1973 (class 2604 OID 26444)
-- Dependencies: 1656 1657 1657
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_pielfaneastejidocelularsubcutaneo" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_pielfaneastejidocelularsubcutaneo_id_seq"'::regclass);


--
-- TOC entry 1971 (class 2604 OID 26415)
-- Dependencies: 1652 1653 1653
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE "HistoriaClinica_vacuna" ALTER COLUMN id SET DEFAULT nextval('"HistoriaClinica_vacuna_id_seq"'::regclass);


--
-- TOC entry 1951 (class 2604 OID 26066)
-- Dependencies: 1611 1610 1611
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- TOC entry 1950 (class 2604 OID 26051)
-- Dependencies: 1609 1608 1609
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 1955 (class 2604 OID 26131)
-- Dependencies: 1619 1618 1619
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_message ALTER COLUMN id SET DEFAULT nextval('auth_message_id_seq'::regclass);


--
-- TOC entry 1949 (class 2604 OID 26041)
-- Dependencies: 1607 1606 1607
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- TOC entry 1954 (class 2604 OID 26111)
-- Dependencies: 1617 1616 1617
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- TOC entry 1953 (class 2604 OID 26096)
-- Dependencies: 1615 1614 1615
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- TOC entry 1952 (class 2604 OID 26081)
-- Dependencies: 1613 1612 1613
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 1958 (class 2604 OID 26178)
-- Dependencies: 1626 1625 1626
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- TOC entry 1956 (class 2604 OID 26147)
-- Dependencies: 1621 1620 1621
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 1957 (class 2604 OID 26170)
-- Dependencies: 1624 1623 1624
-- Name: id; Type: DEFAULT; Schema: public; Owner: wyrven
--

ALTER TABLE django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- TOC entry 2128 (class 0 OID 26251)
-- Dependencies: 1635
-- Data for Name: GestionTurnos_administrativos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_administrativos" (usuarios_ptr_id) FROM stdin;
1
11
\.


--
-- TOC entry 2130 (class 0 OID 26281)
-- Dependencies: 1639
-- Data for Name: GestionTurnos_consultorios; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_consultorios" (id, nombre) FROM stdin;
\.


--
-- TOC entry 2132 (class 0 OID 26302)
-- Dependencies: 1643
-- Data for Name: GestionTurnos_diasatencion; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_diasatencion" (id, fecha, cant_turno, medico_id, horario_atenc_id) FROM stdin;
\.


--
-- TOC entry 2124 (class 0 OID 26205)
-- Dependencies: 1630
-- Data for Name: GestionTurnos_expecialidades; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_expecialidades" (id, nombre) FROM stdin;
1	Odontologo
2	Traumatologo
3	Psicologo
4	Pediatra
5	Neurologo
6	Oftalmologo
7	Podologo
8	Psiquiatra
9	Nutricionista
10	Medico de Guardia
11	Cardiologo
\.


--
-- TOC entry 2129 (class 0 OID 26263)
-- Dependencies: 1637
-- Data for Name: GestionTurnos_expecialidadesmedicos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_expecialidadesmedicos" (id, codigo_medico_id, cod_expecialidad_id) FROM stdin;
1	10	10
3	10	11
\.


--
-- TOC entry 2131 (class 0 OID 26289)
-- Dependencies: 1641
-- Data for Name: GestionTurnos_horarioatencion; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_horarioatencion" (id, dia, hora_inicio, hora_fin, duracion_turno, intervalo, medico_id) FROM stdin;
1	LUN	08:00:00	12:00:00	15	0	10
2	MAR	08:00:00	12:00:00	15	0	10
3	JUE	16:00:00	20:00:00	15	0	10
\.


--
-- TOC entry 2126 (class 0 OID 26231)
-- Dependencies: 1633
-- Data for Name: GestionTurnos_medicos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_medicos" (usuarios_ptr_id, matricula) FROM stdin;
10	77634
\.


--
-- TOC entry 2127 (class 0 OID 26241)
-- Dependencies: 1634
-- Data for Name: GestionTurnos_pacientes; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_pacientes" (usuarios_ptr_id) FROM stdin;
2
3
6
7
8
\.


--
-- TOC entry 2134 (class 0 OID 26341)
-- Dependencies: 1647
-- Data for Name: GestionTurnos_solitudesturnos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_solitudesturnos" (id, fecha_solicitud, fecha_requerida, estado, comentarios, codigo_paciente_id, codigo_medico_id) FROM stdin;
\.


--
-- TOC entry 2123 (class 0 OID 26197)
-- Dependencies: 1628
-- Data for Name: GestionTurnos_tipousuario; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_tipousuario" (id, nombre) FROM stdin;
4	Paciente
5	Medico
6	Administrativo
\.


--
-- TOC entry 2133 (class 0 OID 26320)
-- Dependencies: 1645
-- Data for Name: GestionTurnos_turnos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_turnos" (id, fecha, hora_inicio, hora_fin, comentarios, paciente_id, medico_id) FROM stdin;
\.


--
-- TOC entry 2125 (class 0 OID 26213)
-- Dependencies: 1632
-- Data for Name: GestionTurnos_usuarios; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "GestionTurnos_usuarios" (id, dni, sexo, telefono, direccion, tipo_usuario_id, user_id, tipo_doc) FROM stdin;
2	32987654	M	387-44123456	aden	4	2	\N
3	25789541	M		Aden Castle	4	4	\N
6	0	M			4	7	\N
7	659874132	F			4	8	\N
8	32793572	M	387-4494307		4	9	DNI
10	15786234	M	387-4673675		5	11	DNI
11	0	F			6	12	--
1	6478123	-	1234	Admin Ksa	6	1	DNI
\.


--
-- TOC entry 2136 (class 0 OID 26380)
-- Dependencies: 1651
-- Data for Name: HistoriaClinica_antecedentesperinatales; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_antecedentesperinatales" (id, hist_clinica_id, enbarazo_nro, duracion_embarazo, controles, parto_normal, peso, talla, patologias, atencion_medica, otros_datos) FROM stdin;
\.


--
-- TOC entry 2140 (class 0 OID 26459)
-- Dependencies: 1659
-- Data for Name: HistoriaClinica_cabeza; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_cabeza" (id, examen_fisico_id, craneo, fontanelas_y_suturas, facie, parpados, conjuntivas, globo_ocular_mov, vision, nariz_fosas_nasales, labios, dientes, lengua, mucosa_bucofaringea, amigdalas, pabellones_auriculares, cond_audit_externo, timpanos, audicion, observaciones) FROM stdin;
1	1	N	N	N	N	A	N	N	N	N	A	A	N	N	N	N	A	N	solo toy probando
2	2	N	N	N	N	N	N	A	N	N	N	N	N	N	N	N	N	N	toy ciego.. jajaj
\.


--
-- TOC entry 2144 (class 0 OID 26543)
-- Dependencies: 1667
-- Data for Name: HistoriaClinica_consultamedica; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_consultamedica" (id, hist_clinica_id, fecha, observaciones, medico_id) FROM stdin;
\.


--
-- TOC entry 2141 (class 0 OID 26475)
-- Dependencies: 1661
-- Data for Name: HistoriaClinica_cuello; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_cuello" (id, examen_fisico_id, inspecion, palpacion, percucion, ausculacion, observaciones) FROM stdin;
1	1	normal	nuse que poner	tun tun	lalalal	sarasasa 
2	2	aafasf	afaffa	 asfa	faff	Normal
\.


--
-- TOC entry 2143 (class 0 OID 26527)
-- Dependencies: 1665
-- Data for Name: HistoriaClinica_diagnostico; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_diagnostico" (id, hist_clinica_id, fecha, observaciones) FROM stdin;
\.


--
-- TOC entry 2138 (class 0 OID 26425)
-- Dependencies: 1655
-- Data for Name: HistoriaClinica_examenbase; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_examenbase" (id, hist_clinica_id, fecha, temp_corporal, pres_art_sist, pres_art_diast, frec_respiratoria, pulso, peso_medio, altura_media, peso, altura, talla, bmi, imprecion_general) FROM stdin;
1	1	2011-11-25 03:00:00+00	0	0	0	0	0	0	0	0	0		0	test
2	2	2011-11-28 03:00:00+00	0	0	0	0	0	1.76	75	94	1.8600000000000001	43	0	normal
\.


--
-- TOC entry 2145 (class 0 OID 26565)
-- Dependencies: 1669
-- Data for Name: HistoriaClinica_habitostoxicos; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_habitostoxicos" (id, examen_fisico_id, fecha, alcohol, tabaco, drogas, infuciones, observaciones) FROM stdin;
\.


--
-- TOC entry 2146 (class 0 OID 26600)
-- Dependencies: 1671
-- Data for Name: HistoriaClinica_imagen; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_imagen" (id, examen_fisico_id, titulo, descripcion, imagen) FROM stdin;
2	2	ffafaf	fasffafa afa	estudios/imagenes/90820879521320861989.jpeg
1	2	faffasff	ffasfafaf	estudios/imagenes/Homer_radiografia.gif
\.


--
-- TOC entry 2135 (class 0 OID 26362)
-- Dependencies: 1649
-- Data for Name: HistoriaClinica_informacionbasica; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_informacionbasica" (id, fecha_nacimiento, lugar_nacimiento, grupo_sanguineo, padre, madre, obra_social, nro_afiliado, estado_civil, ocupacion, religion, motivo_consulta, antecedentes_enfermedad_actual, paciente_id) FROM stdin;
1	1985-06-06 03:00:00+00	Las Lajitas	O+					C					2
2	1987-06-20 03:00:00+00	J.V.Gonzales	A-	Maria Evelia Nuñez	Sergio Ricardo Quiroga	IPS	123456789	S	Estudiante	Ninguna	me duele el higado :P		8
\.


--
-- TOC entry 2142 (class 0 OID 26491)
-- Dependencies: 1663
-- Data for Name: HistoriaClinica_otrosestudio; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_otrosestudio" (id, examen_fisico_id, fecha, descripcion) FROM stdin;
\.


--
-- TOC entry 2139 (class 0 OID 26441)
-- Dependencies: 1657
-- Data for Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_pielfaneastejidocelularsubcutaneo" (id, examen_fisico_id, aspecto, dist_pilosa, lesiones, faneras, tejido_cel_subcutaneo) FROM stdin;
\.


--
-- TOC entry 2137 (class 0 OID 26412)
-- Dependencies: 1653
-- Data for Name: HistoriaClinica_vacuna; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY "HistoriaClinica_vacuna" (id, hist_clinica_id, fecha, descripcion, tipo_dosis) FROM stdin;
1	1	1995-05-20 03:00:00+00	BCG	1ra
\.


--
-- TOC entry 2114 (class 0 OID 26063)
-- Dependencies: 1611
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 2113 (class 0 OID 26048)
-- Dependencies: 1609
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2118 (class 0 OID 26128)
-- Dependencies: 1619
-- Data for Name: auth_message; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_message (id, user_id, message) FROM stdin;
\.


--
-- TOC entry 2112 (class 0 OID 26038)
-- Dependencies: 1607
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add message	4	add_message
11	Can change message	4	change_message
12	Can delete message	4	delete_message
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add log entry	8	add_logentry
23	Can change log entry	8	change_logentry
24	Can delete log entry	8	delete_logentry
25	Can add tipo usuario	9	add_tipousuario
26	Can change tipo usuario	9	change_tipousuario
27	Can delete tipo usuario	9	delete_tipousuario
28	Can add expecialidades	10	add_expecialidades
29	Can change expecialidades	10	change_expecialidades
30	Can delete expecialidades	10	delete_expecialidades
31	Can add usuarios	11	add_usuarios
32	Can change usuarios	11	change_usuarios
33	Can delete usuarios	11	delete_usuarios
34	Can add medicos	12	add_medicos
35	Can change medicos	12	change_medicos
36	Can delete medicos	12	delete_medicos
37	Can add pacientes	13	add_pacientes
38	Can change pacientes	13	change_pacientes
39	Can delete pacientes	13	delete_pacientes
40	Can add administrativos	14	add_administrativos
41	Can change administrativos	14	change_administrativos
42	Can delete administrativos	14	delete_administrativos
43	Can add expecialidades medicos	15	add_expecialidadesmedicos
44	Can change expecialidades medicos	15	change_expecialidadesmedicos
45	Can delete expecialidades medicos	15	delete_expecialidadesmedicos
46	Can add consultorios	16	add_consultorios
47	Can change consultorios	16	change_consultorios
48	Can delete consultorios	16	delete_consultorios
49	Can add horario atencion	17	add_horarioatencion
50	Can change horario atencion	17	change_horarioatencion
51	Can delete horario atencion	17	delete_horarioatencion
52	Can add dias atencion	18	add_diasatencion
53	Can change dias atencion	18	change_diasatencion
54	Can delete dias atencion	18	delete_diasatencion
55	Can add turnos	19	add_turnos
56	Can change turnos	19	change_turnos
57	Can delete turnos	19	delete_turnos
58	Can add solitudes turnos	20	add_solitudesturnos
59	Can change solitudes turnos	20	change_solitudesturnos
60	Can delete solitudes turnos	20	delete_solitudesturnos
61	Can add informacion basica	21	add_informacionbasica
62	Can change informacion basica	21	change_informacionbasica
63	Can delete informacion basica	21	delete_informacionbasica
64	Can add antecedentes perinatales	22	add_antecedentesperinatales
65	Can change antecedentes perinatales	22	change_antecedentesperinatales
66	Can delete antecedentes perinatales	22	delete_antecedentesperinatales
67	Can add habitos toxicos	23	add_habitostoxicos
68	Can change habitos toxicos	23	change_habitostoxicos
69	Can delete habitos toxicos	23	delete_habitostoxicos
70	Can add vacuna	24	add_vacuna
71	Can change vacuna	24	change_vacuna
72	Can delete vacuna	24	delete_vacuna
73	Can add examen base	25	add_examenbase
74	Can change examen base	25	change_examenbase
75	Can delete examen base	25	delete_examenbase
76	Can add piel faneas tejido celular subcutaneo	26	add_pielfaneastejidocelularsubcutaneo
77	Can change piel faneas tejido celular subcutaneo	26	change_pielfaneastejidocelularsubcutaneo
78	Can delete piel faneas tejido celular subcutaneo	26	delete_pielfaneastejidocelularsubcutaneo
79	Can add cabeza	27	add_cabeza
80	Can change cabeza	27	change_cabeza
81	Can delete cabeza	27	delete_cabeza
82	Can add cuello	28	add_cuello
83	Can change cuello	28	change_cuello
84	Can delete cuello	28	delete_cuello
85	Can add otros estudio	29	add_otrosestudio
86	Can change otros estudio	29	change_otrosestudio
87	Can delete otros estudio	29	delete_otrosestudio
88	Can add imagen	30	add_imagen
89	Can change imagen	30	change_imagen
90	Can delete imagen	30	delete_imagen
91	Can add diagnostico	31	add_diagnostico
92	Can change diagnostico	31	change_diagnostico
93	Can delete diagnostico	31	delete_diagnostico
94	Can add consulta medica	32	add_consultamedica
95	Can change consulta medica	32	change_consultamedica
96	Can delete consulta medica	32	delete_consultamedica
\.


--
-- TOC entry 2117 (class 0 OID 26108)
-- Dependencies: 1617
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
2	elpion85	Eduardo	Friaz	elpion85@hotmail.com	sha1$0b024$0f85488896f9d6fd3da8fa95c6ec02d618558079	f	t	f	2011-11-25 02:26:13.884+00	2011-11-25 02:26:13.884+00
4	demian	Christian Demian	Castro		sha1$13ce1$9a2d896a6f999a85c93c456d7b058e9cfe26b858	f	t	f	2011-11-25 02:30:13.48+00	2011-11-25 02:30:13.48+00
7	einer	Joni	de Ciudadela		sha1$0e995$3aa760d7ad94824358e55f7baa982a940c95fbba	f	t	f	2011-11-25 02:34:42.736+00	2011-11-25 02:34:42.736+00
8	hatsume	Miku	Hatzume	hatzume_miku@vocaloid.com	sha1$6cd11$d11680f6b66a93475e6d70b64e561172bcc82e5c	f	t	f	2011-11-25 02:35:36.591+00	2011-11-25 02:35:36.591+00
9	wyrven	Ricardo D.	Quiroga		sha1$6dd5e$16495c256ceedb916ade48e5c4188c244069ade4	f	t	f	2011-11-25 02:36:32.272+00	2011-11-25 02:36:32.272+00
12	adm_01	Arbalez	Seruzel		sha1$5434e$30c2ff5500bee7d82b76a0f111030c117f849321	f	t	f	2011-11-25 03:40:01.394+00	2011-11-25 03:40:01.394+00
1	admin	Light	yagami	amd@gmail.com	sha1$327b4$5265e0cdd48f4a6ae71daf59a3b5b339da3d83fd	t	t	t	2011-11-28 21:44:25.429+00	2011-11-25 02:17:10.291+00
11	medico	Don	Perignion		sha1$6d933$e15ac037eb67f9ce567cd53b8cf8007a413dfcf1	f	t	f	2011-11-28 21:55:00.434+00	2011-11-25 03:32:19.12+00
\.


--
-- TOC entry 2116 (class 0 OID 26093)
-- Dependencies: 1615
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 2115 (class 0 OID 26078)
-- Dependencies: 1613
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2122 (class 0 OID 26175)
-- Dependencies: 1626
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2011-11-25 02:26:42.232+00	1	9	3	Administrativo	3	
2	2011-11-25 02:26:42.235+00	1	9	2	Medico	3	
3	2011-11-25 02:26:42.236+00	1	9	1	Paciente	3	
4	2011-11-25 02:27:57.456+00	1	13	2	Pac - elpion85	1	
\.


--
-- TOC entry 2119 (class 0 OID 26144)
-- Dependencies: 1621
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	message	auth	message
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	log entry	admin	logentry
9	tipo usuario	GestionTurnos	tipousuario
10	expecialidades	GestionTurnos	expecialidades
11	usuarios	GestionTurnos	usuarios
12	medicos	GestionTurnos	medicos
13	pacientes	GestionTurnos	pacientes
14	administrativos	GestionTurnos	administrativos
15	expecialidades medicos	GestionTurnos	expecialidadesmedicos
16	consultorios	GestionTurnos	consultorios
17	horario atencion	GestionTurnos	horarioatencion
18	dias atencion	GestionTurnos	diasatencion
19	turnos	GestionTurnos	turnos
20	solitudes turnos	GestionTurnos	solitudesturnos
21	informacion basica	HistoriaClinica	informacionbasica
22	antecedentes perinatales	HistoriaClinica	antecedentesperinatales
23	habitos toxicos	HistoriaClinica	habitostoxicos
24	vacuna	HistoriaClinica	vacuna
25	examen base	HistoriaClinica	examenbase
26	piel faneas tejido celular subcutaneo	HistoriaClinica	pielfaneastejidocelularsubcutaneo
27	cabeza	HistoriaClinica	cabeza
28	cuello	HistoriaClinica	cuello
29	otros estudio	HistoriaClinica	otrosestudio
30	imagen	HistoriaClinica	imagen
31	diagnostico	HistoriaClinica	diagnostico
32	consulta medica	HistoriaClinica	consultamedica
\.


--
-- TOC entry 2120 (class 0 OID 26157)
-- Dependencies: 1622
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
3f3b57492f885f87b5bb4bfa3f3c4ff7	gAJ9cQEuNjY1YjIwYmI3NjgwMjc3NDc0NWUxNmViZDY3YTc1OGI=\n	2011-12-09 02:20:17.701+00
429eece5cc4dd7153b8d275634b07c5c	gAJ9cQEoVQt1c3VhcmlvX3JvbHECWAYAAABNZWRpY29xA1UNX2F1dGhfdXNlcl9pZHEESwtVBGFy\nZWFxBVUFRmFsc2VxBlUHdXN1YXJpb3EHWAYAAABtZWRpY29xCFUSX2F1dGhfdXNlcl9iYWNrZW5k\ncQlVKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQpVCnVzdWFyaW9f\naWRxC0sKdS5kNjJkZGU5MTkwMDY0NGI2ZmRiOTMyNjRlZGM1Y2M5Mw==\n	2011-12-09 04:04:31.441+00
904b83c578ed8a009df2e0b3b6f8fcd1	gAJ9cQEoVQt1c3VhcmlvX3JvbHECWAYAAABNZWRpY29xA1UNX2F1dGhfdXNlcl9pZHEESwtVB3Vz\ndWFyaW9xBVgGAAAAbWVkaWNvcQZVBGFyZWFxB1UFRmFsc2VxCFUSX2F1dGhfdXNlcl9iYWNrZW5k\ncQlVKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQpVCnVzdWFyaW9f\naWRxC0sKdS4zNGUxMjA1NmFkYTczNDgyZWNhM2VlZjJlYmNmOTU4Mw==\n	2011-12-12 22:07:47.706+00
\.


--
-- TOC entry 2121 (class 0 OID 26167)
-- Dependencies: 1624
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: wyrven
--

COPY django_site (id, domain, name) FROM stdin;
\.


--
-- TOC entry 2030 (class 2606 OID 26255)
-- Dependencies: 1635 1635
-- Name: GestionTurnos_administrativos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_administrativos"
    ADD CONSTRAINT "GestionTurnos_administrativos_pkey" PRIMARY KEY (usuarios_ptr_id);


--
-- TOC entry 2034 (class 2606 OID 26286)
-- Dependencies: 1639 1639
-- Name: GestionTurnos_consultorios_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_consultorios"
    ADD CONSTRAINT "GestionTurnos_consultorios_pkey" PRIMARY KEY (id);


--
-- TOC entry 2038 (class 2606 OID 26307)
-- Dependencies: 1643 1643
-- Name: GestionTurnos_diasatencion_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_diasatencion"
    ADD CONSTRAINT "GestionTurnos_diasatencion_pkey" PRIMARY KEY (id);


--
-- TOC entry 2020 (class 2606 OID 26210)
-- Dependencies: 1630 1630
-- Name: GestionTurnos_expecialidades_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_expecialidades"
    ADD CONSTRAINT "GestionTurnos_expecialidades_pkey" PRIMARY KEY (id);


--
-- TOC entry 2032 (class 2606 OID 26268)
-- Dependencies: 1637 1637
-- Name: GestionTurnos_expecialidadesmedicos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_expecialidadesmedicos"
    ADD CONSTRAINT "GestionTurnos_expecialidadesmedicos_pkey" PRIMARY KEY (id);


--
-- TOC entry 2036 (class 2606 OID 26294)
-- Dependencies: 1641 1641
-- Name: GestionTurnos_horarioatencion_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_horarioatencion"
    ADD CONSTRAINT "GestionTurnos_horarioatencion_pkey" PRIMARY KEY (id);


--
-- TOC entry 2026 (class 2606 OID 26235)
-- Dependencies: 1633 1633
-- Name: GestionTurnos_medicos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_medicos"
    ADD CONSTRAINT "GestionTurnos_medicos_pkey" PRIMARY KEY (usuarios_ptr_id);


--
-- TOC entry 2028 (class 2606 OID 26245)
-- Dependencies: 1634 1634
-- Name: GestionTurnos_pacientes_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_pacientes"
    ADD CONSTRAINT "GestionTurnos_pacientes_pkey" PRIMARY KEY (usuarios_ptr_id);


--
-- TOC entry 2042 (class 2606 OID 26349)
-- Dependencies: 1647 1647
-- Name: GestionTurnos_solitudesturnos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_solitudesturnos"
    ADD CONSTRAINT "GestionTurnos_solitudesturnos_pkey" PRIMARY KEY (id);


--
-- TOC entry 2018 (class 2606 OID 26202)
-- Dependencies: 1628 1628
-- Name: GestionTurnos_tipousuario_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_tipousuario"
    ADD CONSTRAINT "GestionTurnos_tipousuario_pkey" PRIMARY KEY (id);


--
-- TOC entry 2040 (class 2606 OID 26328)
-- Dependencies: 1645 1645
-- Name: GestionTurnos_turnos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_turnos"
    ADD CONSTRAINT "GestionTurnos_turnos_pkey" PRIMARY KEY (id);


--
-- TOC entry 2022 (class 2606 OID 26218)
-- Dependencies: 1632 1632
-- Name: GestionTurnos_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_usuarios"
    ADD CONSTRAINT "GestionTurnos_usuarios_pkey" PRIMARY KEY (id);


--
-- TOC entry 2024 (class 2606 OID 26220)
-- Dependencies: 1632 1632
-- Name: GestionTurnos_usuarios_user_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "GestionTurnos_usuarios"
    ADD CONSTRAINT "GestionTurnos_usuarios_user_id_key" UNIQUE (user_id);


--
-- TOC entry 2048 (class 2606 OID 26388)
-- Dependencies: 1651 1651
-- Name: HistoriaClinica_antecedentesperinatales_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_antecedentesperinatales"
    ADD CONSTRAINT "HistoriaClinica_antecedentesperinatales_pkey" PRIMARY KEY (id);


--
-- TOC entry 2058 (class 2606 OID 26467)
-- Dependencies: 1659 1659
-- Name: HistoriaClinica_cabeza_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_cabeza"
    ADD CONSTRAINT "HistoriaClinica_cabeza_pkey" PRIMARY KEY (id);


--
-- TOC entry 2068 (class 2606 OID 26551)
-- Dependencies: 1667 1667
-- Name: HistoriaClinica_consultamedica_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_consultamedica"
    ADD CONSTRAINT "HistoriaClinica_consultamedica_pkey" PRIMARY KEY (id);


--
-- TOC entry 2060 (class 2606 OID 26483)
-- Dependencies: 1661 1661
-- Name: HistoriaClinica_cuello_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_cuello"
    ADD CONSTRAINT "HistoriaClinica_cuello_pkey" PRIMARY KEY (id);


--
-- TOC entry 2066 (class 2606 OID 26535)
-- Dependencies: 1665 1665
-- Name: HistoriaClinica_diagnostico_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_diagnostico"
    ADD CONSTRAINT "HistoriaClinica_diagnostico_pkey" PRIMARY KEY (id);


--
-- TOC entry 2052 (class 2606 OID 26433)
-- Dependencies: 1655 1655
-- Name: HistoriaClinica_examenbase_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_examenbase"
    ADD CONSTRAINT "HistoriaClinica_examenbase_pkey" PRIMARY KEY (id);


--
-- TOC entry 2071 (class 2606 OID 26573)
-- Dependencies: 1669 1669
-- Name: HistoriaClinica_habitostoxicos_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_habitostoxicos"
    ADD CONSTRAINT "HistoriaClinica_habitostoxicos_pkey" PRIMARY KEY (id);


--
-- TOC entry 2074 (class 2606 OID 26608)
-- Dependencies: 1671 1671
-- Name: HistoriaClinica_imagen_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_imagen"
    ADD CONSTRAINT "HistoriaClinica_imagen_pkey" PRIMARY KEY (id);


--
-- TOC entry 2044 (class 2606 OID 26372)
-- Dependencies: 1649 1649
-- Name: HistoriaClinica_informacionbasica_paciente_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_informacionbasica"
    ADD CONSTRAINT "HistoriaClinica_informacionbasica_paciente_id_key" UNIQUE (paciente_id);


--
-- TOC entry 2046 (class 2606 OID 26370)
-- Dependencies: 1649 1649
-- Name: HistoriaClinica_informacionbasica_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_informacionbasica"
    ADD CONSTRAINT "HistoriaClinica_informacionbasica_pkey" PRIMARY KEY (id);


--
-- TOC entry 2062 (class 2606 OID 26501)
-- Dependencies: 1663 1663
-- Name: HistoriaClinica_otrosestudio_examen_fisico_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_otrosestudio"
    ADD CONSTRAINT "HistoriaClinica_otrosestudio_examen_fisico_id_key" UNIQUE (examen_fisico_id);


--
-- TOC entry 2064 (class 2606 OID 26499)
-- Dependencies: 1663 1663
-- Name: HistoriaClinica_otrosestudio_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_otrosestudio"
    ADD CONSTRAINT "HistoriaClinica_otrosestudio_pkey" PRIMARY KEY (id);


--
-- TOC entry 2054 (class 2606 OID 26451)
-- Dependencies: 1657 1657
-- Name: HistoriaClinica_pielfaneastejidocelularsub_examen_fisico_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_pielfaneastejidocelularsubcutaneo"
    ADD CONSTRAINT "HistoriaClinica_pielfaneastejidocelularsub_examen_fisico_id_key" UNIQUE (examen_fisico_id);


--
-- TOC entry 2056 (class 2606 OID 26449)
-- Dependencies: 1657 1657
-- Name: HistoriaClinica_pielfaneastejidocelularsubcutaneo_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_pielfaneastejidocelularsubcutaneo"
    ADD CONSTRAINT "HistoriaClinica_pielfaneastejidocelularsubcutaneo_pkey" PRIMARY KEY (id);


--
-- TOC entry 2050 (class 2606 OID 26417)
-- Dependencies: 1653 1653
-- Name: HistoriaClinica_vacuna_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY "HistoriaClinica_vacuna"
    ADD CONSTRAINT "HistoriaClinica_vacuna_pkey" PRIMARY KEY (id);


--
-- TOC entry 1990 (class 2606 OID 26070)
-- Dependencies: 1611 1611
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 1986 (class 2606 OID 26055)
-- Dependencies: 1609 1609 1609
-- Name: auth_group_permissions_group_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_key UNIQUE (group_id, permission_id);


--
-- TOC entry 1988 (class 2606 OID 26053)
-- Dependencies: 1609 1609
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 1992 (class 2606 OID 26068)
-- Dependencies: 1611 1611
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2006 (class 2606 OID 26136)
-- Dependencies: 1619 1619
-- Name: auth_message_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_pkey PRIMARY KEY (id);


--
-- TOC entry 1982 (class 2606 OID 26045)
-- Dependencies: 1607 1607 1607
-- Name: auth_permission_content_type_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_key UNIQUE (content_type_id, codename);


--
-- TOC entry 1984 (class 2606 OID 26043)
-- Dependencies: 1607 1607
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 1998 (class 2606 OID 26098)
-- Dependencies: 1615 1615
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 2000 (class 2606 OID 26100)
-- Dependencies: 1615 1615 1615
-- Name: auth_user_groups_user_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_key UNIQUE (user_id, group_id);


--
-- TOC entry 2002 (class 2606 OID 26113)
-- Dependencies: 1617 1617
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 1994 (class 2606 OID 26083)
-- Dependencies: 1613 1613
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 1996 (class 2606 OID 26085)
-- Dependencies: 1613 1613 1613
-- Name: auth_user_user_permissions_user_id_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_key UNIQUE (user_id, permission_id);


--
-- TOC entry 2004 (class 2606 OID 26115)
-- Dependencies: 1617 1617
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 2016 (class 2606 OID 26184)
-- Dependencies: 1626 1626
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2008 (class 2606 OID 26151)
-- Dependencies: 1621 1621 1621
-- Name: django_content_type_app_label_key; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_key UNIQUE (app_label, model);


--
-- TOC entry 2010 (class 2606 OID 26149)
-- Dependencies: 1621 1621
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2012 (class 2606 OID 26164)
-- Dependencies: 1622 1622
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2014 (class 2606 OID 26172)
-- Dependencies: 1624 1624
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: wyrven; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- TOC entry 2069 (class 1259 OID 26579)
-- Dependencies: 1669
-- Name: HistoriaClinica_habitostoxicos_examen_fisico_id; Type: INDEX; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE INDEX "HistoriaClinica_habitostoxicos_examen_fisico_id" ON "HistoriaClinica_habitostoxicos" USING btree (examen_fisico_id);


--
-- TOC entry 2072 (class 1259 OID 26614)
-- Dependencies: 1671
-- Name: HistoriaClinica_imagen_examen_fisico_id; Type: INDEX; Schema: public; Owner: wyrven; Tablespace: 
--

CREATE INDEX "HistoriaClinica_imagen_examen_fisico_id" ON "HistoriaClinica_imagen" USING btree (examen_fisico_id);


--
-- TOC entry 2089 (class 2606 OID 26256)
-- Dependencies: 2021 1635 1632
-- Name: GestionTurnos_administrativos_usuarios_ptr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_administrativos"
    ADD CONSTRAINT "GestionTurnos_administrativos_usuarios_ptr_id_fkey" FOREIGN KEY (usuarios_ptr_id) REFERENCES "GestionTurnos_usuarios"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2094 (class 2606 OID 26313)
-- Dependencies: 1641 2035 1643
-- Name: GestionTurnos_diasatencion_horario_atenc_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_diasatencion"
    ADD CONSTRAINT "GestionTurnos_diasatencion_horario_atenc_id_fkey" FOREIGN KEY (horario_atenc_id) REFERENCES "GestionTurnos_horarioatencion"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2093 (class 2606 OID 26308)
-- Dependencies: 2025 1633 1643
-- Name: GestionTurnos_diasatencion_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_diasatencion"
    ADD CONSTRAINT "GestionTurnos_diasatencion_medico_id_fkey" FOREIGN KEY (medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2091 (class 2606 OID 26274)
-- Dependencies: 2019 1637 1630
-- Name: GestionTurnos_expecialidadesmedicos_cod_expecialidad_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_expecialidadesmedicos"
    ADD CONSTRAINT "GestionTurnos_expecialidadesmedicos_cod_expecialidad_id_fkey" FOREIGN KEY (cod_expecialidad_id) REFERENCES "GestionTurnos_expecialidades"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2090 (class 2606 OID 26269)
-- Dependencies: 2025 1633 1637
-- Name: GestionTurnos_expecialidadesmedicos_codigo_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_expecialidadesmedicos"
    ADD CONSTRAINT "GestionTurnos_expecialidadesmedicos_codigo_medico_id_fkey" FOREIGN KEY (codigo_medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2092 (class 2606 OID 26295)
-- Dependencies: 2025 1641 1633
-- Name: GestionTurnos_horarioatencion_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_horarioatencion"
    ADD CONSTRAINT "GestionTurnos_horarioatencion_medico_id_fkey" FOREIGN KEY (medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2087 (class 2606 OID 26236)
-- Dependencies: 1632 1633 2021
-- Name: GestionTurnos_medicos_usuarios_ptr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_medicos"
    ADD CONSTRAINT "GestionTurnos_medicos_usuarios_ptr_id_fkey" FOREIGN KEY (usuarios_ptr_id) REFERENCES "GestionTurnos_usuarios"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2088 (class 2606 OID 26246)
-- Dependencies: 2021 1632 1634
-- Name: GestionTurnos_pacientes_usuarios_ptr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_pacientes"
    ADD CONSTRAINT "GestionTurnos_pacientes_usuarios_ptr_id_fkey" FOREIGN KEY (usuarios_ptr_id) REFERENCES "GestionTurnos_usuarios"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2098 (class 2606 OID 26355)
-- Dependencies: 2025 1633 1647
-- Name: GestionTurnos_solitudesturnos_codigo_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_solitudesturnos"
    ADD CONSTRAINT "GestionTurnos_solitudesturnos_codigo_medico_id_fkey" FOREIGN KEY (codigo_medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2097 (class 2606 OID 26350)
-- Dependencies: 2027 1647 1634
-- Name: GestionTurnos_solitudesturnos_codigo_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_solitudesturnos"
    ADD CONSTRAINT "GestionTurnos_solitudesturnos_codigo_paciente_id_fkey" FOREIGN KEY (codigo_paciente_id) REFERENCES "GestionTurnos_pacientes"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2096 (class 2606 OID 26334)
-- Dependencies: 1645 1633 2025
-- Name: GestionTurnos_turnos_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_turnos"
    ADD CONSTRAINT "GestionTurnos_turnos_medico_id_fkey" FOREIGN KEY (medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2095 (class 2606 OID 26329)
-- Dependencies: 1634 1645 2027
-- Name: GestionTurnos_turnos_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_turnos"
    ADD CONSTRAINT "GestionTurnos_turnos_paciente_id_fkey" FOREIGN KEY (paciente_id) REFERENCES "GestionTurnos_pacientes"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2085 (class 2606 OID 26221)
-- Dependencies: 1632 2017 1628
-- Name: GestionTurnos_usuarios_tipo_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_usuarios"
    ADD CONSTRAINT "GestionTurnos_usuarios_tipo_usuario_id_fkey" FOREIGN KEY (tipo_usuario_id) REFERENCES "GestionTurnos_tipousuario"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2086 (class 2606 OID 26226)
-- Dependencies: 1617 1632 2001
-- Name: GestionTurnos_usuarios_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "GestionTurnos_usuarios"
    ADD CONSTRAINT "GestionTurnos_usuarios_user_id_fkey" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2100 (class 2606 OID 26389)
-- Dependencies: 1649 2045 1651
-- Name: HistoriaClinica_antecedentesperinatales_hist_clinica_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_antecedentesperinatales"
    ADD CONSTRAINT "HistoriaClinica_antecedentesperinatales_hist_clinica_id_fkey" FOREIGN KEY (hist_clinica_id) REFERENCES "HistoriaClinica_informacionbasica"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2104 (class 2606 OID 26468)
-- Dependencies: 1659 1655 2051
-- Name: HistoriaClinica_cabeza_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_cabeza"
    ADD CONSTRAINT "HistoriaClinica_cabeza_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2108 (class 2606 OID 26552)
-- Dependencies: 1667 1649 2045
-- Name: HistoriaClinica_consultamedica_hist_clinica_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_consultamedica"
    ADD CONSTRAINT "HistoriaClinica_consultamedica_hist_clinica_id_fkey" FOREIGN KEY (hist_clinica_id) REFERENCES "HistoriaClinica_informacionbasica"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2109 (class 2606 OID 26557)
-- Dependencies: 2025 1633 1667
-- Name: HistoriaClinica_consultamedica_medico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_consultamedica"
    ADD CONSTRAINT "HistoriaClinica_consultamedica_medico_id_fkey" FOREIGN KEY (medico_id) REFERENCES "GestionTurnos_medicos"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2105 (class 2606 OID 26484)
-- Dependencies: 1655 2051 1661
-- Name: HistoriaClinica_cuello_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_cuello"
    ADD CONSTRAINT "HistoriaClinica_cuello_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2107 (class 2606 OID 26536)
-- Dependencies: 1665 2045 1649
-- Name: HistoriaClinica_diagnostico_hist_clinica_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_diagnostico"
    ADD CONSTRAINT "HistoriaClinica_diagnostico_hist_clinica_id_fkey" FOREIGN KEY (hist_clinica_id) REFERENCES "HistoriaClinica_informacionbasica"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2102 (class 2606 OID 26434)
-- Dependencies: 1655 2045 1649
-- Name: HistoriaClinica_examenbase_hist_clinica_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_examenbase"
    ADD CONSTRAINT "HistoriaClinica_examenbase_hist_clinica_id_fkey" FOREIGN KEY (hist_clinica_id) REFERENCES "HistoriaClinica_informacionbasica"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2110 (class 2606 OID 26574)
-- Dependencies: 1669 2051 1655
-- Name: HistoriaClinica_habitostoxicos_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_habitostoxicos"
    ADD CONSTRAINT "HistoriaClinica_habitostoxicos_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2111 (class 2606 OID 26609)
-- Dependencies: 1671 2051 1655
-- Name: HistoriaClinica_imagen_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_imagen"
    ADD CONSTRAINT "HistoriaClinica_imagen_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2099 (class 2606 OID 26373)
-- Dependencies: 2027 1649 1634
-- Name: HistoriaClinica_informacionbasica_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_informacionbasica"
    ADD CONSTRAINT "HistoriaClinica_informacionbasica_paciente_id_fkey" FOREIGN KEY (paciente_id) REFERENCES "GestionTurnos_pacientes"(usuarios_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2106 (class 2606 OID 26502)
-- Dependencies: 1655 1663 2051
-- Name: HistoriaClinica_otrosestudio_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_otrosestudio"
    ADD CONSTRAINT "HistoriaClinica_otrosestudio_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2103 (class 2606 OID 26452)
-- Dependencies: 1655 2051 1657
-- Name: HistoriaClinica_pielfaneastejidocelularsu_examen_fisico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_pielfaneastejidocelularsubcutaneo"
    ADD CONSTRAINT "HistoriaClinica_pielfaneastejidocelularsu_examen_fisico_id_fkey" FOREIGN KEY (examen_fisico_id) REFERENCES "HistoriaClinica_examenbase"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2101 (class 2606 OID 26418)
-- Dependencies: 1653 1649 2045
-- Name: HistoriaClinica_vacuna_hist_clinica_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY "HistoriaClinica_vacuna"
    ADD CONSTRAINT "HistoriaClinica_vacuna_hist_clinica_id_fkey" FOREIGN KEY (hist_clinica_id) REFERENCES "HistoriaClinica_informacionbasica"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2076 (class 2606 OID 26056)
-- Dependencies: 1983 1607 1609
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2082 (class 2606 OID 26137)
-- Dependencies: 2001 1617 1619
-- Name: auth_message_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2080 (class 2606 OID 26101)
-- Dependencies: 1611 1991 1615
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2078 (class 2606 OID 26086)
-- Dependencies: 1607 1613 1983
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2075 (class 2606 OID 26152)
-- Dependencies: 2009 1607 1621
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2084 (class 2606 OID 26190)
-- Dependencies: 2009 1621 1626
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2083 (class 2606 OID 26185)
-- Dependencies: 2001 1617 1626
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2077 (class 2606 OID 26071)
-- Dependencies: 1991 1611 1609
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2081 (class 2606 OID 26121)
-- Dependencies: 1617 1615 2001
-- Name: user_id_refs_id_7ceef80f; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2079 (class 2606 OID 26116)
-- Dependencies: 2001 1617 1613
-- Name: user_id_refs_id_dfbab7d; Type: FK CONSTRAINT; Schema: public; Owner: wyrven
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2151 (class 0 OID 0)
-- Dependencies: 3
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2011-11-28 21:57:20

--
-- PostgreSQL database dump complete
--

