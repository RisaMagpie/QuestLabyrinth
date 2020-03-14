DROP DATABASE IF EXISTS "quest_labyrinth";

CREATE DATABASE "quest_labyrinth" WITH ENCODING = 'UTF8';

--\c "postgres"




CREATE TABLE actions_for_state (
    id smallint NOT NULL,
    coordinate_x smallint NOT NULL,
    coordinate_y smallint NOT NULL,
    possible_action_id integer NOT NULL
);



CREATE TABLE actions_id (
    id smallint NOT NULL,
    action_id integer NOT NULL,
    action_name character varying(50) NOT NULL
);



CREATE TABLE screenplay_for_state (
    id smallint NOT NULL,
    coordinate_x smallint NOT NULL,
    coordinate_y smallint NOT NULL,
    current_screenplay_part_id smallint NOT NULL
);



CREATE TABLE screenplay_id (
    id smallint NOT NULL,
    screenplay_part_id integer NOT NULL,
    screenplay_part_text character varying(50) NOT NULL
);



CREATE TABLE user_inventory (
    id smallint NOT NULL,
    user_id integer NOT NULL,
    item_name character varying(50) NOT NULL
);



CREATE TABLE user_state (
    id smallint NOT NULL,
    user_id integer NOT NULL,
    user_name character varying(50) NOT NULL,
    coordinate_x smallint NOT NULL,
    coordinate_y smallint NOT NULL,
    time_before_attack smallint NOT NULL
);




ALTER TABLE ONLY actions_for_state
    ADD CONSTRAINT actions_for_state_pkey PRIMARY KEY (id);


ALTER TABLE ONLY actions_id
    ADD CONSTRAINT actions_id_pkey PRIMARY KEY (id);


ALTER TABLE ONLY screenplay_for_state
    ADD CONSTRAINT screenplay_for_state_current_screenplay_part_id_key UNIQUE (current_screenplay_part_id);


ALTER TABLE ONLY screenplay_for_state
    ADD CONSTRAINT screenplay_for_state_pkey PRIMARY KEY (id);


ALTER TABLE ONLY screenplay_id
    ADD CONSTRAINT screenplay_id_pkey PRIMARY KEY (id);



ALTER TABLE ONLY user_inventory
    ADD CONSTRAINT user_inventory_pkey PRIMARY KEY (id);



ALTER TABLE ONLY user_state
    ADD CONSTRAINT user_state_pkey PRIMARY KEY (id);


