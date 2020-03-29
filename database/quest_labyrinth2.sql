DROP DATABASE IF EXISTS "quest_labyrinth";

CREATE DATABASE "quest_labyrinth" WITH ENCODING = 'UTF8';

--\c "postgres"


CREATE TABLE actions_for_state (
    id integer NOT NULL,
    coordinate_x bigint NOT NULL,
    coordinate_y bigint NOT NULL,
    possible_action_id integer NOT NULL
);




CREATE SEQUENCE actions_for_state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



CREATE TABLE actions_id (
    action_id integer NOT NULL,
    action_name character varying(50) NOT NULL
);



CREATE SEQUENCE actions_id_action_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



CREATE TABLE screenplay_for_state (
    id integer NOT NULL,
    coordinate_x bigint NOT NULL,
    coordinate_y bigint NOT NULL,
    current_screenplay_part_id smallint NOT NULL
);



CREATE SEQUENCE screenplay_for_state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



CREATE TABLE screenplay_id (
    screenplay_part_id integer NOT NULL,
    screenplay_part_text character varying(50) NOT NULL
);



CREATE SEQUENCE screenplay_id_screenplay_part_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



CREATE TABLE user_inventory (
    id integer NOT NULL,
    user_id integer NOT NULL,
    item_name character varying(50) NOT NULL
);



CREATE SEQUENCE user_inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



CREATE TABLE user_state (
    user_id integer NOT NULL,
    user_name character varying(50) NOT NULL,
    coordinate_x bigint NOT NULL,
    coordinate_y bigint NOT NULL,
    time_before_attack bigint NOT NULL
);



CREATE SEQUENCE user_state_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



ALTER TABLE ONLY actions_id
    ADD CONSTRAINT actions_id_pkey PRIMARY KEY (action_id);




ALTER TABLE ONLY screenplay_for_state
    ADD CONSTRAINT screenplay_for_state_pkey PRIMARY KEY (id);




ALTER TABLE ONLY screenplay_id
    ADD CONSTRAINT screenplay_id_pkey PRIMARY KEY (screenplay_part_id);




ALTER TABLE ONLY user_inventory
    ADD CONSTRAINT user_inventory_pkey PRIMARY KEY (id);




ALTER TABLE ONLY user_state
    ADD CONSTRAINT user_state_pkey PRIMARY KEY (user_id);



