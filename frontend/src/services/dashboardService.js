import client from "../api/client";

export const getDashboardSummary = async () => {
  const token = localStorage.getItem("token");

  const response = await client.get("/dashboard/summary", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};

