CREATE TABLE journals (
  journal_id SERIAL PRIMARY KEY,
  journal_number TEXT,
  publication_date DATE,
  class TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE proprietors (
  proprietor_id SERIAL PRIMARY KEY,
  name TEXT,
  address TEXT,
  registration_info TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE agents (
  agent_id SERIAL PRIMARY KEY,
  name TEXT,
  address TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE trademarks (
  trademark_id SERIAL PRIMARY KEY,
  application_number TEXT,
  application_date DATE,
  logo_url TEXT,
  usage_status TEXT,
  first_used_date DATE,
  usage_location TEXT,
  mark_description TEXT,
  mark_disclaimer TEXT,
  journal_id INTEGER REFERENCES journals(journal_id),
  proprietor_id INTEGER REFERENCES proprietors(proprietor_id),
  agent_id INTEGER REFERENCES agents(agent_id)
);
