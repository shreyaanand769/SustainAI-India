'use client';

import { motion } from 'framer-motion';
import { Activity, AlertTriangle, Bot, BrainCircuit, Building2, Gauge, Globe2, IndianRupee, Map, Radar, Satellite, ShieldCheck, Waves, type LucideIcon } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { causalNodes, districtRisks, interventions, riskTimeline } from '../lib/demo-data';

const nav = ['National Command Center', 'State Explorer', 'District Intelligence', 'Risk Radar', 'Simulations Lab', 'Solution Engine', 'Execution Planner', 'Policy Optimizer', 'Resource Command Center'];
const riskCards: Array<[string, string, string, string, LucideIcon]> = [
  ['Heatwave Risk', '86', '+12%', 'High confidence', AlertTriangle],
  ['AQI Crisis', '95', '+8%', 'Escalating in NCR', Activity],
  ['Water Scarcity', '91', '+16%', 'Critical aquifers', Waves],
  ['Flood Threat', '84', '+5%', 'Coastal clusters', Radar],
  ['Agriculture Stress', '74', '+9%', 'Rainfall sensitive', Globe2],
  ['Population Pressure', '93', '+11%', 'Urban expansion', Building2]
];

export function CommandShell() {
  const nationalScore = Math.round(districtRisks.reduce((sum, d) => sum + d.sustainability, 0) / districtRisks.length);
  return (
    <main className="grid-overlay min-h-screen overflow-hidden">
      <aside className="fixed left-0 top-0 hidden h-screen w-72 border-r border-white/10 bg-command/80 p-5 backdrop-blur-xl xl:block">
        <div className="mb-8 flex items-center gap-3">
          <div className="rounded-2xl bg-emeraldA/15 p-3 text-emeraldA"><BrainCircuit /></div>
          <div><p className="text-sm uppercase tracking-[0.35em] text-emeraldA">BharatSustain</p><h1 className="text-xl font-bold">AI Command OS</h1></div>
        </div>
        <nav className="space-y-2">
          {nav.map((item, i) => <a key={item} className={`block rounded-xl px-4 py-3 text-sm transition ${i === 0 ? 'bg-emeraldA/15 text-emeraldA shadow-glow' : 'text-slate-300 hover:bg-white/5'}`}>{item}</a>)}
        </nav>
        <div className="absolute bottom-5 left-5 right-5 rounded-2xl border border-emeraldA/25 bg-emeraldA/10 p-4">
          <p className="text-xs uppercase tracking-[0.3em] text-emeraldA">Living Model</p>
          <p className="mt-2 text-sm text-slate-300">Streaming weather, policy, satellite, citizen, and economic signals trigger adaptive re-scoring.</p>
        </div>
      </aside>

      <section className="xl:ml-72">
        <header className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6">
          <div>
            <p className="text-sm uppercase tracking-[0.4em] text-emeraldA">India adaptive sustainability intelligence</p>
            <h2 className="mt-2 text-3xl font-black md:text-5xl">Predict. Explain. Simulate. Execute.</h2>
          </div>
          <button className="hidden rounded-full border border-emeraldA/40 px-5 py-3 text-sm text-emeraldA md:block">Voice: “Show groundwater risk in Maharashtra”</button>
        </header>

        <section className="mx-auto grid max-w-7xl gap-6 px-6 lg:grid-cols-[1.25fr_.75fr]">
          <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} className="relative overflow-hidden rounded-[2rem] border border-white/10 bg-white/[0.04] p-6 shadow-2xl">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_55%_30%,rgba(39,243,164,.18),transparent_30%)]" />
            <div className="relative z-10 flex flex-wrap items-start justify-between gap-4">
              <div><p className="text-sm uppercase tracking-[0.3em] text-amberRisk">National Command Center</p><h3 className="mt-2 text-4xl font-black">Live India Risk Mesh</h3><p className="mt-3 max-w-2xl text-slate-300">Geospatial overlays unify heat, AQI, groundwater, flood, crop health, infrastructure stress, resource depletion, and demographic vulnerability.</p></div>
              <div className="rounded-2xl border border-white/10 bg-black/30 p-4 text-center"><p className="text-xs text-slate-400">Sustainability Score</p><p className="text-5xl font-black text-emeraldA">{nationalScore}</p></div>
            </div>
            <div className="relative z-10 mt-8 grid min-h-[430px] place-items-center rounded-[1.5rem] border border-emeraldA/20 bg-[#071527]">
              <div className="absolute h-80 w-72 rounded-[48%] border border-emeraldA/30 bg-emeraldA/10 blur-[1px]" />
              {districtRisks.map((d, i) => <div key={d.district} className="absolute rounded-full border border-white/40 bg-amberRisk/80 shadow-[0_0_28px_rgba(255,159,28,.55)]" style={{ width: 14 + d.water / 10, height: 14 + d.water / 10, left: `${20 + (i * 9) % 55}%`, top: `${20 + (i * 13) % 58}%` }} title={d.district} />)}
              <Map className="h-56 w-56 text-emeraldA/60" />
              <div className="absolute bottom-4 left-4 flex flex-wrap gap-2 text-xs">{['Heat', 'AQI', 'Water Stress', 'Flood', 'Groundwater', 'Crop Health', 'Infrastructure'].map(x => <span className="rounded-full bg-white/10 px-3 py-1" key={x}>{x}</span>)}</div>
            </div>
          </motion.div>

          <div className="grid gap-6">
            <Panel title="Adaptive Intelligence Engine" icon={<Bot />}>
              <div className="space-y-4 text-sm text-slate-300">
                <p>Event-driven recalculation loop: ingest → detect anomaly → update risk → re-rank interventions → revise execution plan.</p>
                <div className="grid grid-cols-2 gap-3">
                  {['Online learning', 'Redis/Kafka streams', 'Scheduled retraining', 'Policy drift detection'].map(x => <div key={x} className="rounded-xl bg-white/5 p-3">{x}</div>)}
                </div>
              </div>
            </Panel>
            <Panel title="Emergency Preparedness" icon={<ShieldCheck />}>
              <ResponsiveContainer width="100%" height={180}><BarChart data={districtRisks.slice(0, 5)}><Tooltip contentStyle={{ background: '#081527', border: '1px solid rgba(255,255,255,.12)' }} /><XAxis dataKey="district" hide /><YAxis hide /><Bar dataKey="flood" fill="#ff9f1c" radius={[8,8,0,0]} /><Bar dataKey="heat" fill="#27f3a4" radius={[8,8,0,0]} /></BarChart></ResponsiveContainer>
            </Panel>
          </div>
        </section>

        <section className="mx-auto mt-6 grid max-w-7xl gap-4 px-6 md:grid-cols-2 xl:grid-cols-3">
          {riskCards.map(([name, score, trend, note, Icon]) => <Panel key={name} title={name} icon={<Icon />}><div className="flex items-end justify-between"><span className="text-5xl font-black">{score}</span><span className="text-amberRisk">{trend}</span></div><p className="mt-2 text-sm text-slate-400">{note}</p><MiniTrend /></Panel>)}
        </section>

        <section className="mx-auto mt-6 grid max-w-7xl gap-6 px-6 lg:grid-cols-2">
          <Panel title="District Digital Twin Leaderboard" icon={<Satellite />}>
            <div className="space-y-3">{districtRisks.map(d => <div key={d.district} className="grid grid-cols-[1fr_auto] gap-3 rounded-xl bg-white/5 p-3"><div><p className="font-semibold">{d.district}, {d.state}</p><p className="text-xs text-slate-400">Trend: {d.trend} · Heat {d.heat} · Water {d.water} · AQI {d.aqi}</p></div><span className="text-2xl font-black text-emeraldA">{d.sustainability}</span></div>)}</div>
          </Panel>
          <Panel title="Risk Escalation Forecast" icon={<Gauge />}>
            <ResponsiveContainer width="100%" height={315}><LineChart data={riskTimeline}><CartesianGrid stroke="rgba(255,255,255,.08)" /><XAxis dataKey="horizon" stroke="#94a3b8" /><YAxis stroke="#94a3b8" /><Tooltip contentStyle={{ background: '#081527', border: '1px solid rgba(255,255,255,.12)' }} /><Line type="monotone" dataKey="heat" stroke="#ff9f1c" strokeWidth={3} /><Line type="monotone" dataKey="water" stroke="#27f3a4" strokeWidth={3} /><Line type="monotone" dataKey="aqi" stroke="#60a5fa" strokeWidth={3} /></LineChart></ResponsiveContainer>
          </Panel>
        </section>

        <section className="mx-auto mt-6 grid max-w-7xl gap-6 px-6 pb-10 lg:grid-cols-[.9fr_1.1fr]">
          <Panel title="Root Cause Web" icon={<BrainCircuit />}>
            <div className="space-y-3">{causalNodes.map(([a,b,w]) => <div key={`${a}-${b}`} className="rounded-xl border border-white/10 bg-black/20 p-3"><p className="text-sm"><span className="text-amberRisk">{a}</span> ← {b}</p><div className="mt-2 h-2 rounded-full bg-white/10"><div className="h-2 rounded-full bg-emeraldA" style={{ width: `${Number(w) * 100}%` }} /></div></div>)}</div>
          </Panel>
          <Panel title="Intervention Marketplace + Climate ROI" icon={<IndianRupee />}>
            <div className="grid gap-3">{interventions.map(s => <div key={s.name} className="rounded-2xl border border-white/10 bg-white/5 p-4"><div className="flex flex-wrap justify-between gap-3"><div><p className="font-bold">{s.name}</p><p className="text-xs text-slate-400">{s.domain} · speed {s.speed} · ROI {s.roi}</p></div><span className="rounded-full bg-emeraldA/15 px-3 py-1 text-emeraldA">Impact {s.impact}</span></div><div className="mt-3 grid grid-cols-3 gap-2 text-center text-xs"><span className="rounded-lg bg-black/20 p-2">{s.cost}</span><span className="rounded-lg bg-black/20 p-2">{s.carbon}</span><span className="rounded-lg bg-black/20 p-2">Scalable</span></div></div>)}</div>
          </Panel>
        </section>
      </section>
    </main>
  );
}

function Panel({ title, icon, children }: { title: string; icon: React.ReactNode; children: React.ReactNode }) {
  return <section className="rounded-[1.5rem] border border-white/10 bg-white/[0.045] p-5 shadow-xl backdrop-blur"><div className="mb-4 flex items-center gap-3 text-emeraldA"><span className="rounded-xl bg-emeraldA/10 p-2">{icon}</span><h3 className="font-bold text-white">{title}</h3></div>{children}</section>;
}

function MiniTrend() {
  return <div className="mt-4 h-20"><ResponsiveContainer width="100%" height="100%"><AreaChart data={riskTimeline}><Area type="monotone" dataKey="water" stroke="#27f3a4" fill="rgba(39,243,164,.18)" /></AreaChart></ResponsiveContainer></div>;
}
