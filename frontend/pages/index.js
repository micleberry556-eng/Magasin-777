import { useState } from "react";

export default function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const testEvaluator = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/v1/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          base_price: 1000.0,
          params: {
            rating: 4.8,
            sales_velocity: 50,
            category: "electronics",
          },
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ error: err.message });
    }
    setLoading(false);
  };

  return (
    <div style={{ fontFamily: "sans-serif", maxWidth: 800, margin: "0 auto", padding: 40 }}>
      <h1>LocalMarket</h1>
      <p style={{ color: "#666" }}>
        Микросервисная платформа маркетплейса — MVP
      </p>

      <hr />

      <h2>Сервисы</h2>
      <ul>
        <li><strong>Evaluator API:</strong> <code>/api/v1/evaluate</code></li>
        <li><strong>Catalog API:</strong> <code>/api/catalog</code> (заглушка)</li>
        <li><strong>Auth API:</strong> <code>/api/auth</code> (заглушка)</li>
      </ul>

      <h2>Тест сервиса оценки</h2>
      <button
        onClick={testEvaluator}
        disabled={loading}
        style={{
          padding: "10px 20px",
          fontSize: 16,
          cursor: "pointer",
          background: "#0070f3",
          color: "#fff",
          border: "none",
          borderRadius: 6,
        }}
      >
        {loading ? "Загрузка..." : "Оценить товар"}
      </button>

      {result && (
        <pre style={{
          marginTop: 20,
          padding: 20,
          background: "#f5f5f5",
          borderRadius: 8,
          overflow: "auto",
        }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}

      <hr />
      <p style={{ color: "#999", fontSize: 14 }}>
        LocalMarket MVP &copy; 2025
      </p>
    </div>
  );
}
